import requests
import math
from ..models import Car, Truck, TruckPhoto, CarPhoto, CarColor, CarBody, CarManufacturer
import asyncio
import aiohttp
from parser.parsers.raw_parser import car_korean_dict
from django.db import transaction
from datetime import date, timedelta
import traceback
import time
import os
from dotenv import load_dotenv
from aiohttp_socks import ProxyConnector

load_dotenv()

diagnosis = 'https://api.encar.com/v1/readside/diagnosis/vehicle/40286929'

car_info = 'https://api.encar.com/v1/readside/vehicle/39813971'

photos = 'https://ci.encar.com/carpicture/carpicture03/pic4003/40034021_001.jpg?impolicy=heightRate&rh=696&cw=1160&ch=696&cg=Center&wtmk=https://ci.encar.com/wt_mark/w_mark_04.png'




class AsyncCarParser():
    def __init__(self):
        self.batch_size = 100
        self.encar_api_url = 'https://api.encar.com/v1/readside/vehicle/'
        self.car_count = Car.objects.all().count()
        self.encar_ids = list(map(lambda x: x['encar_id'], Car.objects.all().values('encar_id')))
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Accept": "application/json, text/plain, */*",
            "Referer": "https://www.encar.com/",
            "Origin": "https://www.encar.com"
        }

        self.batch = []
        self.results = []
        self.counter = 1
        self.color_list = CarColor.objects.all()
        self.body_list = CarBody.objects.all()
        self.manufacturer_list = CarManufacturer.objects.all()

    def run(self):
        self.get_cookies()
        print('Куки получены')
        self.batching_query()
        self.session.close()


    def batching_query(self):
        '''Функция прохода через все батчи легковых машин'''
        for i in range(math.ceil(self.car_count/self.batch_size)):
            self.batch = Car.objects.filter(encar_id__in=self.encar_ids[i*self.batch_size:(i+1)*self.batch_size], manufacturer=None, model=None, version=None, version_details=None)
            self.go_through_batch()
            self.save_to_db()


    def go_through_batch(self):
        list_api_urls = []
        for car in self.batch:
            list_api_urls.append(f'{self.encar_api_url}{car.encar_id}')
        print(f'Запуск {self.counter}')
        self.counter += 1
        self.results = asyncio.run(self.get_info(list_api_urls))
        
    

    async def fetch(self, session, url):
        try:
            async with session.get(url, timeout=10) as response:
                print(response.status)
                print(response.headers)
                text = await response.text()
                print(text)
                photos_urls = list(map(lambda x: x['path'], response['photos']))
                if response['manage']['dummy'] == True: dummy_id = response['vehicleId']
                else: dummy_id = int(url.split('/')[-1])
                detail_dict = {
                    'encar_id': int(url.split('/')[-1]), 
                    'manufacturer': response['category']['manufacturerEnglishName'],
                    'model': response['category']['modelGroupEnglishName'],
                    'version': response['category']['gradeEnglishName'],
                    'version_details': response['category']['gradeDetailEnglishName'],
                    'options': response['options']['standard'],
                    'color': response['spec']['colorName'],
                    'engine_capacity': response['spec']['displacement'],
                    'photos_urls': photos_urls,
                    'korean_number': response['vehicleNo'],
                    'dummy_id': dummy_id,
                    'encar_diag': response['view']['encarDiagnosis'],
                    'body_name': response['spec']['bodyName'],
                    'release_date': response['category']['yearMonth'],
                }
                return detail_dict
        except:
            print(traceback.format_exc())
            time.sleep(20)
            return None


    async def get_info(self, batch):
        proxy_connector = ProxyConnector.from_url(os.getenv('PROXY_URL'))
        async with aiohttp.ClientSession(headers=self.headers, cookies=self.session.cookies, connector=proxy_connector) as session:
            tasks = [self.fetch(session, url) for url in batch]
            results = await asyncio.gather(*tasks)
            return results
    

    def get_cookies(self):
        self.session.get("https://www.encar.com", headers=self.headers) 


    def get_color(self, dict_color, raw_color):
        if not dict_color:
            print(f'Не нашлось цвета {raw_color}')
            return None
        color_to_send = self.color_list.filter(value_key=dict_color[0]).first()
        if not color_to_send:
            new_color = CarColor.objects.create(value_key=dict_color[0], value_name=dict_color[1])
            self.color_list = CarColor.objects.all()
            return new_color
        else:
            return color_to_send
        

    def get_body(self, dict_body, raw_body):
        if not dict_body:
            print(f'Не нашлось цвета {raw_body}')
            return None
        body_to_send = self.body_list.filter(value_key=dict_body[0]).first()
        if not body_to_send:
            new_body = CarBody.objects.create(value_key=dict_body[0], value_name=dict_body[1])
            self.body_list = CarBody.objects.all()
            return new_body
        else:
            return body_to_send
        

    def get_manufacturer(self, raw_manufacturer:str):
        if not raw_manufacturer:
            print(f'Не нашлось производителя {raw_manufacturer}')
            return None
        manufacturer_to_send = self.manufacturer_list.filter(value_name=raw_manufacturer).first()
        if not manufacturer_to_send:
            key_manufacturer = raw_manufacturer.lower().replace(' ', '_').replace('(', '').replace(')', '').replace('/', '').replace('&', '').replace('-', '_')
            new_manufacturer = CarManufacturer.objects.create(value_key=key_manufacturer, value_name=raw_manufacturer)
            self.manufacturer_list = CarManufacturer.objects.all()
            return new_manufacturer
        else:
            return manufacturer_to_send
        

    def check_is_valid(self, release_date, manufacturer_is_foreign):
        is_valid = False
        if release_date:
            year = int(int(release_date) // 100)
            month = int(int(release_date) % 100)
            car_date = date(year, month, 1)
            if manufacturer_is_foreign:
                car_date = car_date - timedelta(days=120)
            else:
                car_date = car_date - timedelta(days=30)
            today = date.today()
            diff_months = (today.year - car_date.year) * 12 + (today.month - car_date.month)
            is_valid = 36 <= diff_months <= 60
            if int(car_date.month) < 10:
                release_date = int(f'{car_date.year}0{car_date.month}')
            else:
                release_date = int(f'{car_date.year}{car_date.month}')
        return release_date, is_valid


    @transaction.atomic
    def save_to_db(self):
        photos_obj = []
        self.updated_batch = []
        for result in self.results:
            if result:
                car_to_update = self.batch.get(encar_id=int(result['encar_id']))
                car_to_update.manufacturer = self.get_manufacturer(result['manufacturer'])
                car_to_update.release_date, car_to_update.is_valid = self.check_is_valid(result['release_date'], car_to_update.manufacturer.is_foreign)
                car_to_update.model = result['model']
                car_to_update.version = result['version']
                car_to_update.version_details = result['version_details']
                car_to_update.options = result['options']
                car_to_update.engine_capacity = result['engine_capacity']
                car_to_update.korean_number = result['korean_number']
                car_to_update.dummy_id = result['dummy_id']
                car_to_update.encar_diag = result['encar_diag']
                car_to_update.color = self.get_color(car_korean_dict['COLOR'].get(result['color'], None), result['color'])
                car_to_update.body_name = self.get_body(car_korean_dict['BODY_NAME'].get(result['body_name'], None), result['body_name'])
                self.updated_batch.append(car_to_update)
                sorted_urls = sorted(set(result['photos_urls']), key=lambda x: int(x[-7:-4]))
                for number, url in enumerate(sorted_urls, 1):
                    photos_obj.append(CarPhoto(
                        order_number = number,
                        link = f'https://ci.encar.com{url}?impolicy=heightRate&rh=696&cw=1160&ch=696&cg=Center&wtmk=https://ci.encar.com/wt_mark/w_mark_04.png',
                        car = car_to_update
                    ))
            else:
                print('нет машины')
        Car.objects.bulk_update(fields=['manufacturer', 
                                        'model', 
                                        'version', 
                                        'version_details', 
                                        'engine_capacity', 
                                        'color', 
                                        'options', 
                                        'korean_number', 
                                        'dummy_id', 
                                        'encar_diag',
                                        'body_name',
                                        'release_date',
                                        'is_valid'], objs=self.updated_batch)
        CarPhoto.objects.bulk_create(photos_obj, ignore_conflicts=True)
        self.results = []




class CarDuplicateClearer():
    def __init__(self):
        self.unique_dummy_ids = self.get_unique_dummy_ids()
        self.all_cars = Car.objects.all().values('dummy_id', 'encar_id')
        self.encar_ids_to_delete = []


    def go_through_unique_dummy_ids(self):
        for dummy_id in self.unique_dummy_ids:
            duplicates = self.all_cars.filter(dummy_id=dummy_id).values('encar_id')
            if len(duplicates) != 1 and duplicates[0]['encar_id'] == dummy_id:
                self.encar_ids_to_delete.append(duplicates[0]['encar_id'])
            elif len(duplicates) != 1 and duplicates[1]['encar_id'] == dummy_id:
                self.encar_ids_to_delete.append(duplicates[1]['encar_id'])
        for i in range(math.ceil(len(self.encar_ids_to_delete) / 1000)):
            Car.objects.filter(encar_id__in=self.encar_ids_to_delete[i*1000:(i+1)*1000]).delete()
        Car.objects.filter(manufacturer__value_name__in=['Others', 'etc', '']).delete() #удаление неизвестных encar'u машин (others-others-others)
        CarManufacturer.objects.filter(value_name__in=['Others', 'etc', '']).delete()
        Car.objects.exclude(sell_type__in=['Обычная покупка', 'Лизинг']).delete()
        Car.objects.filter(engine_capacity__lt=900, fuel_type__value_key__in=['G', 'D', 'GE', 'DE']).delete()
        Car.objects.filter(engine_capacity__isnull=True, fuel_type__value_key__in=['G', 'D', 'GE', 'DE']).delete()
        Car.objects.filter(fuel_type__value_key=None).delete()
        Car.objects.filter(engine_capacity__gt=9999).delete()
        Car.objects.filter(engine_capacity=None).delete()
        list_manufacturers = CarManufacturer.objects.all()
        for manufacturer in list_manufacturers:
            manufacturer.car_count = Car.objects.filter(manufacturer=manufacturer).count()
        CarManufacturer.objects.bulk_update(fields=['car_count'], objs=list_manufacturers)
        cars_valid_check_list = list(Car.objects.filter(release_date__gt=0).values('encar_id'))
        for i in range(math.ceil(len(cars_valid_check_list) / 1000)):
            car_batch = cars_valid_check_list[i*1000:(i+1)*1000]
            cars_to_update = Car.objects.filter(encar_id__in=list(map(lambda x: x['encar_id'], car_batch)))
            for car in cars_to_update:
                year = int(car.release_date // 100)
                month = int(car.release_date % 100)
                car_date = date(year, month, 1)
                today = date.today()
                diff_months = (today.year - car_date.year) * 12 + (today.month - car_date.month)
                car.is_valid = 36 <= diff_months <= 60
            Car.objects.bulk_update(fields=['is_valid'], objs=cars_to_update)

        


    



    def get_unique_dummy_ids(self):
        c = Car.objects.all().values('dummy_id')
        set1 = set()
        for elem in c:
            set1.add(elem['dummy_id'])
        print(len(set1))
        return list(set1)
        
    

    













class AsyncTruckParser():
    def __init__(self):
        self.batch_size = 1000
        self.session = requests.Session()
        self.encar_api_url = 'https://api.encar.com/v1/readside/vehicle/'
        self.truck_count = Truck.objects.all().count()
        self.encar_ids = list(map(lambda x: x['encar_id'], Truck.objects.all().values('encar_id')))
        self.headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
                    "Referer": "https://www.encar.com/",
                    "Accept": "application/json, text/plain, */*",
        }
        self.batch = []
        self.results = []
        self.counter = 1

    def run(self):
        self.get_cookies()
        print('Куки получены')
        self.batching_query()
        self.session.close()


    def batching_query(self):
        '''Функция прохода через все батчи легковых машин'''
        for i in range(math.ceil(self.truck_count/self.batch_size)):
            self.batch = Truck.objects.filter(encar_id__in=self.encar_ids[i*self.batch_size:(i+1)*self.batch_size], color=None, horse_power=None, options=None, engine_capacity=None)
            self.go_through_batch()
            self.save_to_db()


    def go_through_batch(self):
        list_api_urls = []
        for truck in self.batch:
            list_api_urls.append(f'{self.encar_api_url}{truck.encar_id}')
        print(f'Запуск {self.counter}')
        self.counter += 1
        self.results = asyncio.run(self.get_info(list_api_urls))
        
    

    async def fetch(self, session, url):
        try:
            async with session.get(url, timeout=10) as response:
                response = await response.json()
                photos_urls = list(map(lambda x: x['path'], response['photos']))
                if response['manage']['dummy'] == True: dummy_id = response['vehicleId']
                else: dummy_id = int(url.split('/')[-1])
                detail_dict = {
                    'encar_id': int(url.split('/')[-1]),
                    'options': response['options']['standard'],
                    'color': response['spec']['colorName'],
                    'engine_capacity': response['spec']['displacement'],
                    'photos_urls': photos_urls,
                    'horse_power': response['spec']['horsePower'],
                    'korean_number': response['vehicleNo'],
                    'dummy_id': dummy_id,
                    'encar_diag': response['view']['encarDiagnosis'],
                    
                }
                return detail_dict
        except:
            return None


    async def get_info(self, batch):
        async with aiohttp.ClientSession(headers=self.headers, cookies=self.session.cookies) as session:
            tasks = [self.fetch(session, url) for url in batch]
            results = await asyncio.gather(*tasks)
            return results
    

    def get_cookies(self):
        self.session.get("https://www.encar.com", headers=self.headers) 


    def save_to_db(self):
        self.updated_batch = []
        photos_obj = []
        for result in self.results:
            if result:
                truck_to_update = self.batch.get(encar_id=result['encar_id'])
                truck_to_update.options = result['options']
                truck_to_update.color = car_korean_dict['COLOR'].get(result['color'], result['color'])
                truck_to_update.engine_capacity = result['engine_capacity']
                truck_to_update.horse_power = result['horse_power']
                truck_to_update.korean_number = result['korean_number']
                truck_to_update.encar_id = result['encar_id']
                truck_to_update.encar_diag = result['encar_diag']
                truck_to_update.dummy_id = result['dummy_id']
                self.updated_batch.append(truck_to_update)
                sorted_urls = sorted(set(result['photos_urls']), key=lambda x: int(x[-7:-4]))
                for number, url in enumerate(sorted_urls, 1):
                    photos_obj.append(TruckPhoto(
                        order_number = number,
                        link = f'https://ci.encar.com{url}?impolicy=heightRate&rh=696&cw=1160&ch=696&cg=Center&wtmk=https://ci.encar.com/wt_mark/w_mark_04.png',
                        truck = truck_to_update
                    ))
            else:
                print('нет машины')
        TruckPhoto.objects.bulk_create(photos_obj, ignore_conflicts=True)
        Truck.objects.bulk_update(fields=['encar_id', 'encar_diag', 'dummy_id', 'horse_power', 'engine_capacity', 'color', 'options', 'korean_number'], objs=self.updated_batch)
        self.results = []



class TruckDuplicateClearer():
    def __init__(self):
        self.unique_dummy_ids = self.get_unique_dummy_ids()
        self.all_cars = Truck.objects.all().values('dummy_id', 'encar_id')
        self.encar_ids_to_delete = []


    def go_through_unique_dummy_ids(self):
        for dummy_id in self.unique_dummy_ids:
            duplicates = self.all_cars.filter(dummy_id=dummy_id).values('encar_id')
            if len(duplicates) != 1 and duplicates[0]['encar_id'] == dummy_id:
                self.encar_ids_to_delete.append(duplicates[0]['encar_id'])
            elif len(duplicates) != 1 and duplicates[1]['encar_id'] == dummy_id:
                self.encar_ids_to_delete.append(duplicates[1]['encar_id'])
        for i in range(math.ceil(len(self.encar_ids_to_delete) / 1000)):
            Truck.objects.filter(encar_id__in=self.encar_ids_to_delete[i*1000:(i+1)*1000]).delete()
        Truck.objects.filter(manufacturer__in=['Others', 'etc', 'Other', '']).delete() #удаление неизвестных encar'u машин (others-others-others)
        Truck.objects.filter(engine_capacity__lt=900, fuel_type__in=['G', 'D']).delete()
        Truck.objects.filter(engine_capacity__gt=9999).delete()



    def get_unique_dummy_ids(self):
        c = Truck.objects.all().values('dummy_id')
        set1 = set()
        for elem in c:
            set1.add(elem['dummy_id'])
        print(len(set1))
        return list(set1)