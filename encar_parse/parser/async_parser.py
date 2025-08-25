import requests
import math
from .models import Car, Truck
import asyncio
import aiohttp
from parser.raw_parser import car_korean_dict

diagnosis = 'https://api.encar.com/v1/readside/diagnosis/vehicle/40286929'

car_info = 'https://api.encar.com/v1/readside/vehicle/39752647'

photos = 'https://ci.encar.com/carpicture/carpicture03/pic4003/40034021_001.jpg?impolicy=heightRate&rh=696&cw=1160&ch=696&cg=Center&wtmk=https://ci.encar.com/wt_mark/w_mark_04.png'




class AsyncCarParser():
    def __init__(self):
        self.batch_size = 100
        self.session = requests.Session()
        self.encar_api_url = 'https://api.encar.com/v1/readside/vehicle/'
        self.car_count = Car.objects.all().count()
        self.encar_ids = Car.objects.all().values('encar_id')
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
        async with session.get(url, timeout=10) as response:
            response = await response.json()
            photos_list = list(map(lambda x: int(x['code']), response['photos']))
            if not photos_list: number_of_photos = 0
            else: number_of_photos = max(photos_list)
            detail_dict = {
                'encar_id': url.split('/')[-1], 
                'manufacturer': response['category']['manufacturerEnglishName'],
                'model': response['category']['modelGroupEnglishName'],
                'version': response['category']['gradeEnglishName'],
                'version_details': response['category']['gradeDetailEnglishName'],
                'options': response['options']['standard'],
                'color': response['spec']['colorName'],
                'engine_capacity': response['spec']['displacement'],
                'number_of_photos': number_of_photos
            }
            return detail_dict


    async def get_info(self, batch):
        async with aiohttp.ClientSession(headers=self.headers, cookies=self.session.cookies) as session:
            tasks = [self.fetch(session, url) for url in batch]
            results = await asyncio.gather(*tasks)
            return results
    

    def get_cookies(self):
        self.session.get("https://www.encar.com", headers=self.headers) 


    def save_to_db(self):
        self.updated_batch = []
        for result in self.results:
            car_to_update = self.batch.get(encar_id=result['encar_id'])
            car_to_update.manufacturer = result['manufacturer']
            car_to_update.model = result['model']
            car_to_update.version = result['version']
            car_to_update.version_details = result['version_details']
            car_to_update.options = result['options']
            car_to_update.color = car_korean_dict['COLOR'].get(result['color'], result['color'])
            car_to_update.engine_capacity = result['engine_capacity']
            car_to_update.number_of_photos = result['number_of_photos']
            self.updated_batch.append(car_to_update)
        Car.objects.bulk_update(fields=['manufacturer', 'model', 'version', 'version_details', 'engine_capacity', 'color', 'options', 'number_of_photos'], objs=self.updated_batch)
        self.results = []




class AsyncTruckParser():
    ...