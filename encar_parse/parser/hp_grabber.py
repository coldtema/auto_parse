import requests
import aiohttp
import asyncio
from .models import Car, HorsePower
import math
import time
import re
from unicodedata import normalize
from django.db.models import Q
from django.utils import timezone

class HorsePowerParser():
    def __init__(self):
        self.batch_size = 100
        self.results = None

    def run(self):
        self.batching_query_local()
        self.batching_query_zefir()
        self.batching_query_local()


    def batching_query_local(self):
        '''Функция прохода через все батчи легковых машин'''
        self.car_count = Car.objects.all().count()
        print(self.car_count)
        self.encar_ids = list(map(lambda x: x['encar_id'], Car.objects.all().values('encar_id')))
        for i in range(math.ceil(self.car_count/self.batch_size)):
            self.batch = Car.objects.filter(encar_id__in=self.encar_ids[i*self.batch_size:(i+1)*self.batch_size]).select_related('manufacturer')
            self.results = self.check_db_hp(self.batch)
            self.save_to_db_local()


    def batching_query_zefir(self):
        '''Функция прохода через все батчи легковых машин'''
        self.car_count = Car.objects.filter(Q(hp=0, fuel_type__value_key__in=['GE', 'G', 'D', 'DE']) | Q(kw=0, hp_in_kw=0, fuel_type__value_key__in=['GE', 'DE'])).count()
        print(self.car_count)
        self.batch_size = 10
        t = timezone.now()
        if int(t.day) % 2 == 0:
            car_query = Car.objects.filter(Q(hp=0, fuel_type__value_key__in=['GE', 'G', 'D', 'DE']) | Q(kw=0, hp_in_kw=0, fuel_type__value_key__in=['GE', 'DE'])).order_by('-updated')
        else:
            car_query = Car.objects.filter(Q(hp=0, fuel_type__value_key__in=['GE', 'G', 'D', 'DE']) | Q(kw=0, hp_in_kw=0, fuel_type__value_key__in=['GE', 'DE'])).order_by('updated')

        car_dict = dict()
        for car in car_query:
            value_name = self.norm(car.manufacturer.value_name)
            model = self.norm(car.model)
            model_year = self.norm(car.model_year)
            version = self.norm(car.version)
            engine_capacity = self.norm(car.engine_capacity)
            car_dict.setdefault(f'{value_name}{model}{model_year}{version}{engine_capacity}', car.encar_id)

        self.encar_ids = list(car_dict.values())
        self.car_count = len(self.encar_ids)
        print(self.car_count)
        
        for i in range(math.ceil(self.car_count/self.batch_size)):
            self.batch = Car.objects.filter(encar_id__in=self.encar_ids[i*self.batch_size:(i+1)*self.batch_size]).select_related('manufacturer')
            temp = list(map(lambda x: {'encar_id': x.encar_id, 'dummy_id': x.dummy_id}, self.batch))
            self.results = asyncio.run(self.get_info(temp))
            self.save_to_db_zefir()


    def check_db_hp(self, batch: list[Car]):
        for car in batch:
            value_name = self.norm(car.manufacturer.value_name)
            model = self.norm(car.model)
            model_year = self.norm(car.model_year)
            version = self.norm(car.version)
            engine_capacity = self.norm(car.engine_capacity)
            # string = self.normalize_key(value_name, model, model_year, version, engine_capacity)

            hp = HorsePower.objects.filter(value_name=value_name, model=model, model_year=model_year, version=version, engine_capacity=engine_capacity).first()

            if hp:
                car.hp = hp.hp
                car.hp_in_kw = hp.hp_in_kw
                car.kw = hp.kw
        return batch

     

    async def fetch(self, session, car: Car):
        try:
            async with session.get(f'https://zefir.pan-auto.ru/api/cars/{car["encar_id"]}/', timeout=30) as response:
                data = await response.json()
                hp = data["hp"]
                ckw = data.get('ckw', 0)
                bkw = data.get('bkw', 0)
                if not ckw: ckw = 0
                if not bkw: bkw = 0
                if hp:
                    return (hp, ckw, bkw)
                else:
                    raise Exception
        except:
            try:
                async with session.get(f'https://zefir.pan-auto.ru/api/cars/{car["dummy_id"]}/', timeout=30) as response:
                    data = await response.json()
                    hp = data["hp"]
                    ckw = data.get('ckw', 0)
                    bkw = data.get('bkw', 0)
                    if not ckw: ckw = 0
                    if not bkw: bkw = 0
                    if hp:
                        return (hp, ckw, bkw)
                    else:
                        raise Exception
            except:
                return (0, 0, 0)
            

    async def get_info(self, car_batch):
        async with aiohttp.ClientSession() as session:
            tasks = [self.fetch(session, car) for car in car_batch]
            results = await asyncio.gather(*tasks)
            return results
        

    def save_to_db_local(self):
        Car.objects.bulk_update(fields=['hp', 'hp_in_kw', 'kw'], objs=self.results)
        self.batch = []
        self.results = []

    def save_to_db_zefir(self):
        # print(self.results)
        for i in range(len(self.results)):
            # print(self.batch[i])
            self.batch[i].hp = self.results[i][0]
            self.batch[i].hp_in_kw = self.results[i][1]
            self.batch[i].kw = self.results[i][2]
            value_name = self.norm(self.batch[i].manufacturer.value_name)
            model = self.norm(self.batch[i].model)
            model_year = self.norm(self.batch[i].model_year)
            version = self.norm(self.batch[i].version)
            engine_capacity = self.norm(self.batch[i].engine_capacity)
            # string = self.normalize_key(value_name, model, model_year, version, engine_capacity)
            if HorsePower.objects.filter(value_name=value_name, model=model, model_year=model_year, version=version, engine_capacity=engine_capacity).first() and self.results[i][1] != 0:
                HorsePower.objects.filter(value_name=value_name, model=model, model_year=model_year, version=version, engine_capacity=engine_capacity).delete()
                print(f'Нашлась в БД: {value_name} {model} {model_year} {version} {engine_capacity}')


            if not HorsePower.objects.filter(value_name=value_name, model=model, model_year=model_year, version=version, engine_capacity=engine_capacity).first() and self.results[i][0] != 0:
                HorsePower.objects.create(value_name=value_name, model=model, model_year=model_year, version=version, engine_capacity=engine_capacity, hp=self.results[i][0], hp_in_kw=self.results[i][1], kw=self.results[i][2])

        Car.objects.bulk_update(fields=['hp', 'hp_in_kw', 'kw'], objs=self.batch)
        self.batch = []


    def norm(self, s: str | int | None):
        if s is None:
            return None
        s = str(s).strip().lower()
        s = normalize('NFKD', s)
        s = re.sub(r'\s+', ' ', s)
        return s