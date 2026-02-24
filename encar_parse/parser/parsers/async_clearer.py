import requests
import math
from ..models import Car, Truck
import asyncio
import aiohttp
from django.db import transaction
from parser import cookie_grabber
import os
from dotenv import load_dotenv
from aiohttp_socks import ProxyConnector

load_dotenv()

diagnosis = 'https://api.encar.com/v1/readside/diagnosis/vehicle/40286929'

car_info = 'https://api.encar.com/v1/readside/vehicle/40294388'

photos = 'https://ci.encar.com/carpicture/carpicture03/pic4003/40034021_001.jpg?impolicy=heightRate&rh=696&cw=1160&ch=696&cg=Center&wtmk=https://ci.encar.com/wt_mark/w_mark_04.png'




class AsyncCarClearer():
    def __init__(self):
        self.batch_size = 100
        self.session = requests.Session()
        self.encar_api_url = 'https://api.encar.com/v1/readside/vehicle/'
        self.car_count = Car.objects.all().count()
        self.encar_ids = list(map(lambda x: x['encar_id'], Car.objects.all().values('encar_id')))
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
        self.get_number_of_results()
        print('Куки получены')
        self.batching_query()
        self.session.close()


    def batching_query(self):
        '''Функция прохода через все батчи легковых машин'''
        for i in range(math.ceil(self.car_count/self.batch_size)):
            self.batch = Car.objects.filter(encar_id__in=self.encar_ids[i*self.batch_size:(i+1)*self.batch_size])
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
                response = await response.json()
                if response['advertisement']['status'] == 'ADVERTISE':
                        return int(url.split('/')[-1]), True, response['advertisement']['price']
                return int(url.split('/')[-1]), False
        except:
            return int(url.split('/')[-1]), False 


    async def get_info(self, batch):
        proxy_connector = ProxyConnector.from_url(os.getenv('PROXY_URL'))
        async with aiohttp.ClientSession(headers=self.session.headers, cookies=self.session.cookies, connector=proxy_connector) as session:
            tasks = [self.fetch(session, url) for url in batch]
            results = await asyncio.gather(*tasks)
            return results
    

    def get_cookies(self):
        self.session.get("https://www.encar.com", headers=self.headers) 


    def get_number_of_results(self): #он может найти больше 23 тысяч результатов, но в query никогда их не выдаст, потолок - 10000
        current_api_url_list = ['https://api.encar.com/search/car/list/premium?count=True&q=(And.Hidden.N._.CarType.A._.GreenType.Y._.(Or.Separation.A._.Separation.B.)_.Mileage.range(', '0', '..', '10000', ').)&sr=%7CModifiedDate%7C', '0', '%7C1000']
        try:
            print(''.join(current_api_url_list), 'идет по адресу для сбора куков на всякий')
            number_of_cars = self.session.get(''.join(current_api_url_list)).json()['Count']
        except:
            cookies = cookie_grabber.get_new_encar_cookies()
            for c in cookies:
                self.session.cookies.set(c['name'], c['value'])
            self.session.headers.update({"User-Agent": (
                                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                                            "Chrome/126.0.6478.127 Safari/537.36"
                                        )
                                    })
        response = self.session.get(''.join(current_api_url_list))
        number_of_cars = response.json()['Count'] #чтобы усли что встало на ошибке и не пошло все подряд удалять
        print('код:', response.status_code)
        print('текст', response.text[:20])


    @transaction.atomic
    def save_to_db(self):
        self.cars_ids_to_delete = []
        car_ids_to_update_price = []
        if not any(x[1] for x in self.results):
            print('хочет удалить все машины')
            return
        for result in self.results:
            if result[1] == False:
                self.cars_ids_to_delete.append(result[0])
            else:
                car_ids_to_update_price.append((result[0], result[2]))
        car_ids_to_update_price = sorted(car_ids_to_update_price, key=lambda x: x[0])
        cars_to_update = list(Car.objects.filter(encar_id__in=list(map(lambda x: x[0], car_ids_to_update_price))).order_by('encar_id'))
        for i in range(len(cars_to_update)):
            if cars_to_update[i].price != car_ids_to_update_price[i][1]:
                cars_to_update[i].price = car_ids_to_update_price[i][1]
        Car.objects.bulk_update(fields=['price'], objs=cars_to_update)
        if self.cars_ids_to_delete:
            print(self.cars_ids_to_delete)
            Car.objects.filter(encar_id__in=self.cars_ids_to_delete).delete()
        self.results = []





class AsyncTruckClearer():
    def __init__(self):
        self.batch_size = 1000
        self.session = requests.Session()
        self.encar_api_url = 'https://api.encar.com/v1/readside/vehicle/'
        self.car_count = Truck.objects.all().count()
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
        self.get_number_of_results()
        print('Куки получены')
        self.batching_query()
        self.session.close()


    def batching_query(self):
        '''Функция прохода через все батчи легковых машин'''
        for i in range(math.ceil(self.car_count/self.batch_size)):
            self.batch = Truck.objects.filter(encar_id__in=self.encar_ids[i*self.batch_size:(i+1)*self.batch_size])
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
                response = await response.json()
                if response['advertisement']['status'] == 'ADVERTISE':
                        return int(url.split('/')[-1]), True
                return int(url.split('/')[-1]), False
        except:
            return int(url.split('/')[-1]), False 


    async def get_info(self, batch):
        async with aiohttp.ClientSession(headers=self.session.headers, cookies=self.session.cookies) as session:
            tasks = [self.fetch(session, url) for url in batch]
            results = await asyncio.gather(*tasks)
            return results
    

    def get_cookies(self):
        self.session.get("https://www.encar.com", headers=self.headers) 



    def get_number_of_results(self): #он может найти больше 23 тысяч результатов, но в query никогда их не выдаст, потолок - 10000
        current_api_url_list = ['https://api.encar.com/search/car/list/premium?count=True&q=(And.Hidden.N._.CarType.A._.GreenType.Y._.(Or.Separation.A._.Separation.B.)_.Mileage.range(', '0', '..', '10000', ').)&sr=%7CModifiedDate%7C', '0', '%7C1000']
        try:
            print(''.join(current_api_url_list), 'идет по адресу для сбора куков на всякий')
            number_of_cars = self.session.get(''.join(current_api_url_list)).json()['Count']
        except:
            cookies = cookie_grabber.get_new_encar_cookies()
            for c in cookies:
                self.session.cookies.set(c['name'], c['value'])
            self.session.headers.update({"User-Agent": (
                                            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                            "AppleWebKit/537.36 (KHTML, like Gecko) "
                                            "Chrome/126.0.6478.127 Safari/537.36"
                                        )
                                    })
        response = self.session.get(''.join(current_api_url_list))
        number_of_cars = response.json()['Count'] #чтобы eсли что встало на ошибке и не пошло все подряд удалять
        print('код:', response.status_code)
        print('текст', response.text[:20])


    @transaction.atomic
    def save_to_db(self):
        self.cars_ids_to_delete = []
        for result in self.results:
            if result[1] == False:
                self.cars_ids_to_delete.append(result[0])
        if self.cars_ids_to_delete:
            print(self.cars_ids_to_delete)
            Truck.objects.filter(encar_id__in=self.cars_ids_to_delete).delete()
        self.results = []