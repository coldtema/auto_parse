from .models import Car
import math
import requests
import time
from datetime import date
one_eur = 1614.69 #(kor w)



class RuPriceCalc:
    def __init__(self):
        self.currency_checker_url = 'https://www.cbr-xml-daily.ru/daily_json.js'
        self.currency_dict = dict()
        self.batch_size = 1000
        self.car_count = Car.objects.all().count()
        self.encar_ids = list(map(lambda x: x['encar_id'], Car.objects.all().values('encar_id')))
        self.headers = {
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36",
                    "Referer": "https://www.encar.com/",
                    "Accept": "application/json, text/plain, */*",
        }
        self.batch = []
        self.current_vechile = None
        self.current_vechile_age = 0
        self.current_vechile_ru_price = 0
        self.price_shift = 0.989


    def run(self):
        self.get_currency()
        self.batching_query()


    def get_currency(self):
        response = requests.get(self.currency_checker_url).json()
        self.currency_dict['krw/rub'] = response['Valute']['KRW']['Value']/response['Valute']['KRW']['Nominal']
        self.currency_dict['eur/rub'] = response['Valute']['EUR']['Value']/response['Valute']['EUR']['Nominal']
        self.currency_dict['usd/rub'] = response['Valute']['USD']['Value']/response['Valute']['USD']['Nominal']
        print(self.currency_dict)


    def fuel_type_dispatcher(self):
        if self.current_vechile.fuel_type.value_key == 'E':
            price_customs_duty = self.get_customs_duty_electro()
            excise_tax = self.get_excise_tax()
            recycling_fee = self.get_recycling_fee_electro()
            customs_clearance_fee = self.get_customs_clearance_fee()
            nds_tax = self.get_nds_tax(excise_tax, price_customs_duty)
            return self.get_final_price(price_customs_duty, excise_tax, customs_clearance_fee, nds_tax), recycling_fee
        elif self.current_vechile.fuel_type.value_key in ['D', 'G']:
            price_customs_duty = self.get_customs_duty_gasoline()
            recycling_fee = self.get_recycling_fee_gasoline()
            customs_clearance_fee = self.get_customs_clearance_fee()
            return self.get_final_price(price_customs_duty, customs_clearance_fee), recycling_fee
        elif self.current_vechile.fuel_type.value_key in ['DE', 'GE']:
            price_customs_duty = self.get_customs_duty_gasoline()
            recycling_fee = self.get_recycling_fee_hybrid()
            customs_clearance_fee = self.get_customs_clearance_fee()
            return self.get_final_price(price_customs_duty, customs_clearance_fee), recycling_fee
        return None


    def batching_query(self):
        '''Функция прохода через все батчи легковых машин'''
        for i in range(math.ceil(self.car_count/self.batch_size)):
            self.batch = Car.objects.filter(encar_id__in=self.encar_ids[i*self.batch_size:(i+1)*self.batch_size]).select_related('fuel_type', 'manufacturer')
            self.go_through_batch()
            self.save_to_db()

    
    def go_through_batch(self):
        for car in self.batch:
            self.current_vechile = car
            if self.current_vechile.hp == 0:
                 car.customs_duty = 0
                 car.recycling_fee = 0
                 car.ru_price = 0
                 car.final_price_rub = 0
                 continue
            car.customs_duty, car.recycling_fee = self.fuel_type_dispatcher()
            car.ru_price = self.current_vechile_ru_price
            car.final_price_rub = car.ru_price + car.customs_duty + car.recycling_fee + 212000


    def get_customs_duty_electro(self):
        self.current_vechile_ru_price = math.ceil(self.currency_dict['krw/rub'] * self.current_vechile.price * 10000 * self.price_shift)
        return math.ceil(self.current_vechile_ru_price * 0.15)



    def get_customs_duty_gasoline(self):
        self.current_vechile_ru_price = math.ceil(self.currency_dict['krw/rub'] * self.current_vechile.price * 10000 * self.price_shift)
        vechile_price_in_eur = math.ceil(self.current_vechile_ru_price/self.currency_dict['eur/rub'])
        # print(f'Цена в вонах: {self.current_vechile.price * 10000}')
        # print(f'Цена в рублях: {vechile_price_in_rub}')
        # print(f'Цена в евро: {vechile_price_in_eur}')
        self.current_vechile_age = ((date.today()-date(year=int(str(self.current_vechile.release_date)[:-2]), month=int(str(self.current_vechile.release_date)[-2:]), day=1)).days)//365
        # print(f'Возраст: {self.current_vechile_age}')
        # print(f'Объем двигателя: {self.current_vechile.engine_capacity}')
        if self.current_vechile_age < 3:
            for key, value in customs_duty_dict['LESS_3_YEARS'].items():
                if key[0] <= vechile_price_in_eur <= key[1]:
                    return math.ceil(max(vechile_price_in_eur * value[0], value[1]*self.current_vechile.engine_capacity) * self.currency_dict['eur/rub'])
        elif 3 <= self.current_vechile_age < 5:
            for key, value in customs_duty_dict['FROM_3_TO_5_YEARS'].items():
                if key[0] <= self.current_vechile.engine_capacity <= key[1]:
                    return math.ceil(value * self.current_vechile.engine_capacity * self.currency_dict['eur/rub'])
        elif 5 <= self.current_vechile_age:
            for key, value in customs_duty_dict['MORE_5_YEARS'].items():
                if key[0] <= self.current_vechile.engine_capacity <= key[1]:
                    return math.ceil(value * self.current_vechile.engine_capacity * self.currency_dict['eur/rub'])


    def get_excise_tax(self):
        current_vechile_engine_capacity = horsepower_dict.get(f'{self.current_vechile.manufacturer.value_name} {self.current_vechile.model} {self.current_vechile.version} {self.current_vechile.version_details} {self.current_vechile.model_year}', 0)
        if current_vechile_engine_capacity == 0:
            pass
            # print(f'{self.current_vechile.manufacturer.value_name} {self.current_vechile.model} {self.current_vechile.version} {self.current_vechile.version_details} {self.current_vechile.model_year}', 'не нашлось мощности')
        for key, value in excise_tax_dict.items():
            if key[0] <= current_vechile_engine_capacity <= key[1]:
                return math.ceil(current_vechile_engine_capacity / 0.75 * value)


    def get_recycling_fee_electro(self):
        if 0 <= self.current_vechile_age <= 3:
            return recycling_fee_dict['ELECTRO_LESS_3_YEARS'] * 20000
        else:
            return recycling_fee_dict['ELECTRO_MORE_3_YEARS'] * 20000
        
        
    def get_recycling_fee_hybrid(self):
            if 0 <= self.current_vechile_age < 3:
                for key, value in commercial_recycling_fee_dict['HYBRID_LESS_3_YEARS'].items():
                    if key[0] <= self.current_vechile.hp_in_kw + self.current_vechile.kw <= key[1]:
                        return value
            else:
                for key, value in commercial_recycling_fee_dict['HYBRID_MORE_3_YEARS'].items():
                    if key[0] <= self.current_vechile.hp_in_kw + self.current_vechile.kw <= key[1]:
                        return value
    


    def get_recycling_fee_gasoline(self):
        if self.current_vechile.hp <= 160:
            if 0 <= self.current_vechile_age < 3:
                for key, value in recycling_fee_dict['GASOLINE_LESS_3_YEARS'].items():
                    if key[0] <= self.current_vechile.engine_capacity <= key[1]:
                        return 20000 * value
            else:
                for key, value in recycling_fee_dict['GASOLINE_MORE_3_YEARS'].items():
                    if key[0] <= self.current_vechile.engine_capacity <= key[1]:
                        return 20000 * value
        else:
            if 0 <= self.current_vechile_age < 3:
                if self.current_vechile.engine_capacity <= 2000:
                    for key, value in commercial_recycling_fee_dict['GASOLINE_LESS_3_YEARS']['1-2_litre'].items():
                            if key[0] <= self.current_vechile.hp <= key[1]:
                                return value
                            
                if 2001 <= self.current_vechile.engine_capacity <= 3000:
                    for key, value in commercial_recycling_fee_dict['GASOLINE_LESS_3_YEARS']['2-3_litre'].items():
                            if key[0] <= self.current_vechile.hp <= key[1]:
                                return value
                            
                if 3001 <= self.current_vechile.engine_capacity <= 3500:
                    for key, value in commercial_recycling_fee_dict['GASOLINE_LESS_3_YEARS']['3-3.5_litre'].items():
                            if key[0] <= self.current_vechile.hp <= key[1]:
                                return value
                        
                if 3501 <= self.current_vechile.engine_capacity:
                    for key, value in commercial_recycling_fee_dict['GASOLINE_LESS_3_YEARS']['3.5_and_more_litre'].items():
                            if key[0] <= self.current_vechile.hp <= key[1]:
                                return value
                            
            else:
                if self.current_vechile.engine_capacity <= 2000:
                    for key, value in commercial_recycling_fee_dict['GASOLINE_MORE_3_YEARS']['1-2_litre'].items():
                            if key[0] <= self.current_vechile.hp <= key[1]:
                                return value
                            
                if 2001 <= self.current_vechile.engine_capacity <= 3000:
                    for key, value in commercial_recycling_fee_dict['GASOLINE_MORE_3_YEARS']['2-3_litre'].items():
                            if key[0] <= self.current_vechile.hp <= key[1]:
                                return value
                            
                if 3001 <= self.current_vechile.engine_capacity <= 3500:
                    for key, value in commercial_recycling_fee_dict['GASOLINE_MORE_3_YEARS']['3-3.5_litre'].items():
                            if key[0] <= self.current_vechile.hp <= key[1]:
                                return value
                        
                if 3501 <= self.current_vechile.engine_capacity:
                    for key, value in commercial_recycling_fee_dict['GASOLINE_MORE_3_YEARS']['3.5_and_more_litre'].items():
                            if key[0] <= self.current_vechile.hp <= key[1]:
                                return value



    def get_customs_clearance_fee(self):
        for key, value in customs_clearance_fee_dict.items():
                if key[0] <= self.current_vechile_ru_price <= key[1]:
                    return value
                
    def get_nds_tax(self, excise_tax, price_customs_duty):
        return math.ceil((self.current_vechile_ru_price + excise_tax + price_customs_duty) * 0.20)


    def get_final_price(self, *args):
        return sum(args)


    def save_to_db(self):
        Car.objects.bulk_update(fields=['ru_price', 'recycling_fee', 'customs_duty', 'final_price_rub'], objs=self.batch)
        self.batch = []




#пошлина
customs_duty_dict = {
    'LESS_3_YEARS':{
        (0, 8500): (0.54, 2.5), #(% from cost (in eur), but not less than eur/cm3)
        (8501, 16700): (0.48, 3.5),
        (16701, 42300): (0.48, 5.5),
        (42301, 84500): (0.48, 7.5),
        (84501, 169000): (0.48, 15),
        (169001, 100000000): (0.48, 20),
    },
    'FROM_3_TO_5_YEARS': {
        (0, 999): 1.5, #(eur/cm3)
        (1000, 1499): 1.7,
        (1500, 1799): 2.5,
        (1800, 2299): 2.7,
        (2300, 2999): 3.0,
        (3000, 100000): 3.6,
    },
    'MORE_5_YEARS': {
        (0, 999): 3.0,
        (1000, 1499): 3.2,
        (1500, 1799): 3.5,
        (1800, 2299): 4.8,
        (2300, 2999): 5.0,
        (3000, 100000): 5.7,
    }
}

#оформление
customs_clearance_fee_dict = {
    (0, 200000): 775, #rub
    (200001, 450000): 1550,
    (450001, 1200000): 3100,
    (1200001, 2700000): 8530,
    (2700001, 4200000): 12000,
    (4200001, 5500000): 15500,
    (5500001, 7000000): 20000,
    (7000001, 8000000): 23000,
    (8000001, 9000000): 25000,
    (9000001, 10000000): 27000,
    (10000001, 1000000000): 30000,
}


#акциза
excise_tax_dict = {
    (0, 67.4): 0, #rub/0,75kwt
    (67.5, 112.4): 60,
    (112.5, 149.9): 579,
    (150, 224.9): 948,
    (225, 299.9): 1617,
    (300, 374.9): 1673,
    (375, 100000): 1728,
}

#утиль
commercial_recycling_fee_dict = { #*20000 rub
    'ELECTRO_LESS_3_YEARS': 0.17,
    'ELECTRO_MORE_3_YEARS': 0.26,
    'GASOLINE_LESS_3_YEARS':{
        '1-2_litre':{
            (160, 190): 900_000, 
            (191, 220): 952_800,
            (221, 250): 1_010_400,
            (251, 280): 1_142_400,
            (281, 310): 1_291_200,
            (311, 340): 1_459_200,
            (341, 370): 1_663_200,
            (371, 400): 1_896_000,
            (401, 430): 2_160_000,
            (431, 460): 2_464_800,
            (461, 500): 2_808_000,
            (501, 999999): 3_201_600,
        },
        '2-3_litre':{
            (160, 190): 2_306_800, 
            (191, 220): 2_364_000,
            (221, 250): 2_402_400,
            (251, 280): 2_520_000,
            (281, 310): 2_620_800,
            (311, 340): 2_726_400,
            (341, 370): 2_834_400,
            (371, 400): 2_949_600,
            (401, 430): 3_067_200,
            (431, 460): 3_189_600,
            (461, 500): 3_316_800,
            (501, 999999): 3_448_800,
        },
        '3-3.5_litre':{
            (160, 190): 2_635_200, 
            (191, 220): 2_688_000,
            (221, 250): 2_743_200,
            (251, 280): 2_810_400,
            (281, 310): 2_880_000,
            (311, 340): 3_038_400,
            (341, 370): 3_206_400,
            (371, 400): 3_384_000,
            (401, 430): 3_568_800,
            (431, 460): 3_765_600,
            (461, 500): 3_972_000,
            (501, 999999): 4_190_400,
        },
        '3.5_and_more_litre':{
            (160, 190): 3_345_600, 
            (191, 220): 3_403_200,
            (221, 250): 3_460_800,
            (251, 280): 3_530_400,
            (281, 310): 3_600_000,
            (311, 340): 3_727_200,
            (341, 370): 3_857_600,
            (371, 400): 3_993_600,
            (401, 430): 4_132_800,
            (431, 460): 4_276_800,
            (461, 500): 4_425_600,
            (501, 999999): 4_581_600,
        },
    },
    'GASOLINE_MORE_3_YEARS':{
        '1-2_litre':{
            (160, 190): 1_492_800, 
            (191, 220): 1_584_000,
            (221, 250): 1_677_600,
            (251, 280): 1_838_400,
            (281, 310): 2_011_200,
            (311, 340): 2_203_200,
            (341, 370): 2_412_000,
            (371, 400): 2_640_000,
            (401, 430): 2_892_000,
            (431, 460): 3_168_000,
            (461, 500): 3_468_000,
            (501, 999999): 3_796_800,
        },
        '2-3_litre':{
            (160, 190): 3_456_000, 
            (191, 220): 3_501_600,
            (221, 250): 3_552_000,
            (251, 280): 3_660_000,
            (281, 310): 3_770_400,
            (311, 340): 3_873_600,
            (341, 370): 3_981_600,
            (371, 400): 4_094_400,
            (401, 430): 4_209_600,
            (431, 460): 4_327_200,
            (461, 500): 4_447_200,
            (501, 999999): 4_572_000,
        },
        '3-3.5_litre':{
            (160, 190): 4_000_800, 
            (191, 220): 4_044_000,
            (221, 250): 4_087_200,
            (251, 280): 4_144_800,
            (281, 310): 4_248_000,
            (311, 340): 4_356_000,
            (341, 370): 4_485_600,
            (371, 400): 4_620_000,
            (401, 430): 4_759_200,
            (431, 460): 4_900_800,
            (461, 500): 5_049_600,
            (501, 999999): 5_200_800,
        },
        '3.5_and_more_litre':{
            (160, 190): 4_389_600, 
            (191, 220): 4_456_800,
            (221, 250): 4_524_000,
            (251, 280): 4_627_200,
            (281, 310): 4_732_800,
            (311, 340): 4_992_000,
            (341, 370): 5_268_000,
            (371, 400): 5_558_400,
            (401, 430): 5_863_200,
            (431, 460): 6_187_200,
            (461, 500): 6_528_000,
            (501, 999999): 6_885_600,
        },
    },
    'HYBRID_LESS_3_YEARS':{
        (0, 58.84): 800_800, 
        (58.85, 73.55): 991_200,
        (73.56, 95.61): 1_317_600,
        (95.62, 117.68): 1_560_000,
        (117.69, 139.75): 1_848_000,
        (139.76, 161.81): 2_193_600,
        (161.82, 183.88): 2_599_200,
        (183.89, 205.94): 3_079_200,
        (205.95, 9999999): 3_648_000,
    },
    'HYBRID_MORE_3_YEARS':{
        (0, 58.84): 1_408_800, 
        (58.85, 73.55): 1_641_600,
        (73.56, 95.61): 1_912_800,
        (95.62, 117.68): 2_227_200,
        (117.69, 139.75): 2_594_400,
        (139.76, 161.81): 3_024_000,
        (161.82, 183.88): 3_523_200,
        (183.89, 205.94): 4_104_000,
        (205.95, 9999999): 4_780_800,
    }
}

recycling_fee_dict = { #*20000 rub
    'ELECTRO_LESS_3_YEARS': 0.17,
    'ELECTRO_MORE_3_YEARS': 0.26,
    'GASOLINE_LESS_3_YEARS':{
        (0, 1000): 0.17, 
        (1001, 2000): 0.17,
        (2001, 3000): 0.17,
        (3001, 3500): 107.67,
        (3501, 100000): 137.11,
    },
    'GASOLINE_MORE_3_YEARS': {
        (0, 1000): 0.26,
        (1001, 2000): 0.26,
        (2001, 3000): 0.26,
        (3001, 3500): 164.84,
        (3501, 100000): 180.24,
    },
}




horsepower_dict = {
    'Kia Niro Prestige None 2023': 150,
    'Kia EV4 Long Range 2WD GT-LIne 2026': 150,
    'BMW iX xDrive M60 None 2024': 455,
    'BMW i5 xDrive 40 M Sport Pro None 2025': 250,
    'Kia EV6 Standard 4WD Light 2022': 168,

    'Hyundai Ioniq6 Standard E-Value+ 2025': 170,
    'Kia EV6 Long Range 4WD Air 2022': 239,
    'Kia EV6 Standard 4WD Air 2022': 125,
    'Xin yuan ET Van Pro 2-Seater None 2023': 125,
    "Kia Soul EV None 2015": 81,
    "Mini Countryman ALL4 SE JCW None 2025": 162,   # PHEV суммарно
    "Jaguar I-PACE EV400 First Edition None 2019": 294,
    "Audi e-tron 55 Quattro None 2021": 300,
    "Audi Q4 e-tron 45 Premium None 2025": 210,
    "Peugeot 2008 EV GT None 2021": 100,
    "Mercedes-Benz EQA EQA250 Progressive None 2025": 140,
    "BMW iX1 xDrive 30 xLine None 2023": 230,
    "BMW iX1 xDrive 30 xLine None 2024": 230,
    "Mercedes-Benz EQE EQE500 4MATIC None 2024": 300,
    "Genesis G80 e-AWD None 2022": 272,
    "Genesis G80 e-AWD None 2021": 272,
    'Genesis G80 e-AWD None 2025': 272,
    'Audi Q4 e-tron 45 Premium Sportback None 2025': 210,
    'KG_Mobility_Ssangyong Torres Taxi None 2024': 120,
    'BMW iX xDrive45 M Sport None 2026': 300,
    'Hyundai Casper Cross None 2025': 79,
    'KG_Mobility_Ssangyong Musso Black Edge AWD None 2026': 133,
    "Kia EV3 Long Range 2WD GT-Line 2026": 160,
    "Kia EV3 Long Range 2WD GT-Line 2025": 160,
    "Kia EV3 Long Range 2WD GT-Line 2024": 160,
    "Hyundai Ioniq5 Standard AWD Prestige 2022": 235,
    "Volvo XC40 Twin Ultimate None 2022": 300,
    "Mercedes-Benz EQA EQA250 None 2023": 140,
    "Renault-KoreaSamsung SM3 RE None 2020": 94,
    "Tesla Model Y Long Range None 2024": 317,
    "Tesla Model S 90D None 2017": 310,
    "Hyundai Ioniq5 Long Range Exclusive 2025": 225,
    "Peugeot 2008 EV GT None 2023": 115,
    "Hyundai Ioniq5 Standard Exclusive 2022": 170,
    "Hyundai Ioniq9 Performance Type AWD 6-Seater Calligraphy 2025": 300,
    "Hyundai Ioniq5 Standard Commercial 2022": 170,
    "Volvo EX30 Ultra None 2025": 315,
    "Audi Q8 e-tron 50 Quattro None 2024": 250,
    "Porsche Taycan Turbo S None 2021": 460,
    "Kia RAY EV None 2014": 50,
    "Kia Niro Noblesse None 2021": 150,
    "Hyundai Ioniq5 Standard Commercial 2023": 170,
    "BMW i7 xDrive 60 Design Pure Excellence None 2023": 400,
    "Tesla Model 3 Performance None 2022": 377,
    "Hyundai Ioniq5 Long Range AWD Exclusive 2024": 239,
    "Kia Niro Noblesse None 2020": 150,
    "BMW i7 xDrive 60 M sport None 2024": 400,
    "Kia EV3 Standard 2WD Earth 2025": 150,
    "Audi e-tron 55 Quattro Sportback None 2022": 300,
    "Audi e-tron S None 2022": 370,
    "Mercedes-Benz EQE EQE350+ None 2024": 215,
    "BMW i3 SOL+ None 2016": 125,
    "BMW iX1 xDrive 30 M Sport None 2024": 230,
    "Kia EV6 Standard 4WD Air None 2022": 170,
    "Mini Cooper SE Electric 3rd 2022": 135,
    "Porsche Taycan GTS None 2023": 440,
    "Kia EV6 Long Range 4WD Air None 2022": 239,
    "Audi Q4 e-tron 40 Premium Sportback None 2022": 150,
    "Kia Niro Noblesse None 2022": 150,
    "Porsche Taycan 4S None 2022": 320,
    "Porsche Taycan Turbo None 2025": 460,
    "Kia EV9 Long Range 4WD GT Line 2024": 283,
    "Kia EV9 Long Range 4WD GT Line 2026": 283,
    "BMW iX xDrive50 Sports Plus None 2025": 385,
    "Kia EV6 Long Range 4WD GT Line 2023": 239,
    "BMW i3 LUX None 2020": 135,
    "Hyundai Ioniq5 Long range Exclusive 2023": 225,
    "ChevroletGMDaewoo Bolt EV EV Premier None 2023": 150,
    "Kia Niro Air None 2024": 150,
    "Tesla Model 3 Long Range None 2019": 258,
    "Tesla Model X Long Range None 2025": 311,
    "Lexus UX 2WD None 2022": 150,
    "Kia EV3 Long Range 2WD AIr 2026": 160,
    "Hyundai Ioniq N None 2020": 103,   # PHEV, спорт версия
    "Hyundai Ioniq I None 2018": 88,
    "Kia Niro Earth None 2024": 150,
    "BMW i4 M50 None 2024": 400,
    "Kia EV9 Long Range 4WD Air 2024": 283,
    "Tesla Model Y Long Range None 2023": 317,
    "ChevroletGMDaewoo Bolt EV EV Premier None 2022": 150,
    "Kia EV9 Long Range Earth 2024": 283,
    "BMW i5 eDrive 40 M Sport None 2025": 250,
    "Peugeot 2008 EV GT Line None 2020": 100,
    "Kia EV3 Standard 2WD GT-Line 2025": 150,
    "Nissan Leaf EV SL None 2019": 110,
    "Kia EV6 Long Range Earth 2022": 229,
    "Audi Q8 e-tron 55 Quattro Premium Sportback None 2024": 300,
    "Mercedes-Benz EQS EQS450+ None 2023": 265,
    "Mercedes-Benz EQS EQS53 AMG 4MATIC+ None 2022": 484,
    "Volvo EX30 Ultra None 2024": 315,
    "Porsche Taycan 4S None 2025": 320,
    "Kia RAY Light None 2024": 50,
    "Mercedes-Benz EQA EQA250 AMG Package None 2022": 140,
    "Mercedes-Benz EQA EQA250 AMG Package None 2021": 140,
    "KG_Mobility_Ssangyong Torres E7 None 2024": 207,
    "Volvo C40 Twin Ultimate None 2022": 300,
    "Kia Niro Earth None 2025": 150,
    "Hyundai Ioniq5 Long range Prestige 2022": 225,
    "Audi Q4 e-tron 40 Premium None 2022": 150,
    "Audi Q4 e-tron 40 Premium None 2025": 150,
    "BMW i4 M50 None 2022": 400,
    "BMW i7 xDrive 60 Design Pure Excellence None 2024": 400,
    "Mercedes-Benz EQS EQS450 4MATIC Launch Edition None 2024": 265,
    "Hyundai Ioniq6 Long Range Exclusive 2023": 239,
    "Hyundai Kona Premium None 2019": 150,
    "Audi Q6 e-tron Performance None 2025": 285,
    "Tesla Model Y RWD None 2023": 220,
    'Tesla Model Y RWD None 2021': 220,
    "Hyundai ST1 Cargo Premium 2025": 200,  # ожидаемо
    "Kia EV6 Long Range 2WD GT Line 2025": 229,
    "Tesla Model S Performance None 2020": 450,
    "Kia EV9 Long Range 4WD GT Line 2023": 283,
    "Kia RAY Van 2-Seater AIr 2024": 50,
    "Hyundai Ioniq5 Long range Exclusive 2024": 225,
    "BMW i4 eDrive40 M Sports None 2022": 250,
    "Mercedes-Benz G-Class G580 EQ Technology None 2025": 587,
    "Polestar Polestar 2 Longrange Dualmotor None 2023": 300,
    "Renault-KoreaSamsung SM3 RE None 2016": 57,
    "Volvo XC40 Twin None 2024": 300,
    "Hyundai Ioniq9 Cruise Type AWD 6-Seater Calligraphy 2025": 300,
    "Kia EV6 GT 4WD None 2025": 430,
    "Mercedes-Benz EQS EQS450 4MATIC None 2023": 265,
    "Kia EV6 Standard Air 2023": 170,
    "Mercedes-Benz EQE EQE350+ None 2023": 215,
    "Audi RS e-tron GT GT RS None 2022": 475,
    "Audi RS e-tron GT GT RS None 2023": 475,
    "Ford Mustang AWD None 2018": 230,   # EcoBoost гибрид, общая мощность
    "Tesla Model Y RWD None 2024": 220,
    "Hyundai Ioniq5 Long Range Prestige 2023": 225,
    "Others Others Others EV None 2022": 0,
    "Polestar Polestar 2 Longrange Singlemotor None 2022": 220,
    "Polestar Polestar 4 Long Range Single Moter None 2025": 300,
    "Porsche Macan Base 4 None 2025": 300,
    "Mercedes-Benz EQS EQS450 4MATIC Launch Edition None 2023": 265,
    "Mercedes-Benz EQA EQA250 None 2024": 140,
    'Tesla Model S Long Range None 2019': 389,
    "Tesla Model X 100D None 2018": 311,
    "Porsche Taycan 4S None 2024": 320,
    "Kia Niro Prestige None 2022": 150,
    "Hyundai Kona Modren None 2021": 150,
    "Kia Niro Prestige None 2019": 100,
    "ChevroletGMDaewoo Bolt EV EV None 2017": 150,
    "ChevroletGMDaewoo Bolt EV EV None 2018": 150,
    "ChevroletGMDaewoo Bolt EV EV None 2019": 150,
    "Porsche Taycan Turbo S None 2025": 460,
    "Porsche Taycan Turbo S None 2022": 460,
    "Kia EV9 Long Range Air 2024": 283,
    "Kia Soul Noblesse None 2021": 150,
    "Kia Soul Noblesse None 2020": 150,
    "Others Others Others EV None 2019": 0,
    "Kia Soul Prestige None 2019": 100,
    "BMW i3 SOL+ None 2015": 125,
    "Kia Soul EV None 2016": 81,
    "Others Others Others EV None 2020": 0,
    "Hyundai Kona Premium None 2020": 150,
    "Tesla Model S AWD None 2023": 500,
    "Mercedes-Benz EQS Maybach EQS680 4MATIC None 2025": 484,
    "Mercedes-Benz EQB EQB300 4MATIC AMG Line None 2023": 168,
    "Mercedes-Benz EQB EQB300 4MATIC AMG Line None 2022": 168,
    "Hyundai Kona Long Range Premium 2025": 160,
    "Hyundai Ioniq5 Long Range AWD Prestige 2024": 239,
    "Porsche Taycan 4 Cross Turismo None 2022": 280,
    "Mercedes-Benz G-Class G580 EQ Edition 1 None 2025": 432,
    "Volvo XC40 Twin Ultimate None 2024": 300,
    "Kia EV6 Long Range 4WD Light 2022": 239,
    "Kia EV6 Long Range 4WD Light 2023": 239,
    "Kia EV6 Long Range 4WD Light 2024": 239,
    "Genesis GV70 e-AWD None 2022": 320,
    'Genesis GV70 e-AWD None 2024': 320,
    "Hyundai Ioniq Q None 2020": 45,
    "Renault-KoreaSamsung Zoe Intens Eco None 2021": 100,
    "Tesla Cybertruck Cyberbeast None 2024": 630,
    "BMW i5 M60 xDrive None 2024": 442,
    "BMW iX1 xDrive 30 M Sport None 2023": 230,
    "Tesla Model 3 Long Range None 2020": 340,
    "BMW i3 SOL+ None 2018": 135,
    "Kia EV6 Long Range 4WD Earth 2022": 239,
    "DFSK C35 EV  4-Seater None 2023": 60,
    "DFSK C35 EV  4-Seater None 2022": 60,
    "Mini Cooper SE Electric 3rd 2023": 135,
    "BMW i3 LUX None 2015": 125,
    "Tesla Model 3 Standard Range Plue None 2021": 208,
    "Hyundai Ioniq N None 2019": 45,
    "Mini Cooper SE Favoured None 2024": 135,
    'Mini Cooper SE Favoured None 2025': 135,
    "ChevroletGMDaewoo 볼트 EUV Redline None 2023": 150,
    "Kia Niro Air (Taxi Trim) None 2024": 150,
    "DFSK C35 EV 2 Seater Van None 2023": 60,
    "Hyundai Ioniq Q None 2019": 45,
    "Mercedes-Benz EQB EQB300 4MATIC Electric Art None 2024": 168,
    "Mercedes-Benz EQB EQB300 4MATIC Progressive None 2025": 168,
    "Hyundai Ioniq5 Long Range AWD Exclusive 2022": 239,
    "Renault-KoreaSamsung SM3 RE None 2019": 70,
    "BMW i4 eDrive40 M Sports Pro None 2023": 250,
    "Hyundai Ioniq5 Standard Prestige 2022": 170,
    "Cadillac Lyriq Sport None 2024": 373,
    "Renault-KoreaSamsung Twizy Intens(2-seater) None 2019": 13,
    "BMW i4 eDrive40 M Sports None 2025": 250,
    "Renault-KoreaSamsung Twizy Cargo(1-seater+Trunk) None 2019": 13,
    "Kia EV6 Long Range Earth 2023": 239,
    "Audi Q4 e-tron 40 Premium Sportback None 2024": 150,
    "Kia EV6 Long Range Earth 2024": 239,
    "Renault-KoreaSamsung Twizy Intens(2-seater) None 2018": 13,
    "Renault-KoreaSamsung Twizy Intens(2-seater) None 2020": 13,
    "Mercedes-Benz EQA EQA250 AMG Line None 2025": 140,
    "Nissan Leaf EV SL None 2015": 80,
    "Polestar Polestar 2 Longrange Singlemotor None 2023": 220,
    "Hyundai Ioniq6 Long Range AWD Exclusive + 2023": 239,
    "Hyundai Ioniq6 Long Range AWD Exclusive 2025": 239,
    "Kia EV6 Standard Earth 2022": 170,
    "BMW iX xDrive50 Sports Plus None 2024": 385,
    "BMW i7 xDrive 60 Design Pure Excellence Individual None 2023": 400,
    "Jaguar I-PACE EV400 HSE None 2019": 294,
    "DFSK C35 EV 2 Seater Van None 2022": 60,
    "Porsche Taycan Turbo S None 2023": 460,
    "Mercedes-Benz EQB EQB300 4MATIC AMG Line None 2024": 168,
    "Genesis GV60 Performance AWD None 2023": 320,
    "ChevroletGMDaewoo Bolt EV EV Premier None 2021": 150,
    "Kia RAY Air None 2025": 50,
    "Hyundai Ioniq5 Long range Commercial 2022": 170,
    "Hyundai Ioniq5 Long range Commercial 2023": 170,
    "Audi Q4 e-tron 45 None 2025": 195,
    "Hyundai ST1 Cargo Freezer Container Premium 2025": 80,
    "Mercedes-Benz EQC EQC400 4MATIC None 2021": 300,
    "Mercedes-Benz EQA EQA250 None 2021": 140,
    "Hyundai Casper Premium None 2025": 55,
    "Genesis GV60 Standard AWD None 2023": 234,
    "Mini Cooper SE Classic 3rd 2022": 135,
    "Mini Cooper SE Classic 3rd 2023": 135,
    "Mini Cooper SE Classic 3rd 2024": 135,
    "Mini Cooper SE Classic None 2024": 135,
    "Lotus Eletre R None 2025": 675,
    'Xin yuan ET Van 4 Seater None 2023': 60,
    'Kia EV6 Standard Light 2023': 168,
    'KG_Mobility_Ssangyong Torres TV7 None 2025': 120,
    "Mercedes-Benz EQC EQC400 4MATIC Premium None 2020": 300,
    "Audi e-tron 50 Quattro Sportback None 2022": 230,
    "Hyundai Ioniq6 Long Range AWD Prestige 2025": 239,
    "Mercedes-Benz EQB EQB300 4MATIC None 2024": 168,
    "Mercedes-Benz EQB EQB300 4MATIC None 2025": 168,
    "ChevroletGMDaewoo 볼트 EUV Premier None 2023": 150,
    "Hyundai Ioniq5 Long Range AWD N Line 2025": 239,
    "Hyundai Casper Inspiration None 2025": 55,
    "Porsche Taycan 4S None 2021": 320,
    "Fiat 500 EV None 2024": 87,
    "Tesla Model 3 RWD None 2024": 208,
    "Renault-KoreaSamsung SM3 SE None 2019": 70,
    'Renault-KoreaSamsung SM3 SE None 2014': 70,
    "Kia EV3 Long Range 2WD Earth 2025": 150,
    'Kia EV3 Long Range 2WD Earth 2026': 150,
    "Mini Cooper Resolute Edition 3rd 2023": 135,
    "Renault-KoreaSamsung SM3 RE None 2018": 70,
    "Kia Soul EV None 2017": 81,
    "KG_Mobility_Ssangyong Torres E5 None 2024": 120,
    "Porsche Taycan Turbo Cross Turismo None 2022": 460,
    "BMW i4 eDrive40 M Sports Pro None 2022": 250,
    "BMW iX1 xDrive 30 M Sport None 2025": 230,
    "Hyundai Ioniq N None 2018": 45,   # PHEV
    "Hyundai Ioniq6 Long Range Exclusive + 2023": 239,
    "Tesla Model S 100D None 2017": 311,
    "Mercedes-Benz EQE EQE53 AMG 4MATIC+ None 2024": 460,
    "BMW i5 eDrive 40 None 2024": 250,
    "Nissan Leaf EV None 2016": 80,
    "Kia EV9 Long Range 4WD Earth 2024": 283,
    "Kia EV9 Long Range 4WD Earth 2023": 283,
    "BMW i7 eDrive 50 M Sport Limited None 2024": 335,
    "BMW i4 M50 None 2023": 400,
    "BMW iX2 eDrive 20 M Sport None 2024": 150,
    "Tesla Model X Performance None 2019": 451,
    "Tesla Model 3 Long Range None 2022": 340,
    "Kia Soul EV None 2018": 81,
    "Renault-KoreaSamsung Twizy Life(2-Seater) None 2019": 13,
    "Tesla Model 3 Performance None 2021": 377,
    "Hyundai Ioniq6 Long Range Prestige 2023": 239,
    "Tesla Model 3 Long Range None 2025": 340,
    "Tesla Model S 75D None 2019": 245,
    "Tesla Model S 75D None 2018": 245,
    "Audi Q4 e-tron 40 Sportback None 2022": 150,
    "Kia EV6 Long Range GT Line 2023": 239,
    "Mercedes-Benz EQC EQC400 4MATIC None 2020": 300,
    "Polestar Polestar 4 Long Range Duel Moter None 2025": 400,
    "Polestar Polestar 4 Long Range Duel Moter None 2026": 400,
    'Tesla Model X 75D None 2018': 193,
    'Volkswagen ID.5 Pro None 2025': 200,
    "Jaguar I-PACE EV400 HSE None 2020": 294,
    "Tesla Model Y Standard Range None 2021": 220,
    "Tesla Model 3 Long Range None 2021": 340,
    "Mercedes-Benz EQA EQA250 AMG Line None 2023": 140,
    "Hyundai ST1 Cargo Freezer Container Smart 2025": 80,
    "Mercedes-Benz EQS EQS350 None 2022": 215,
    "BMW iX xDrive50 Sports Plus None 2023": 385,
    "Fiat 500 EV None 2017": 87,
    "Audi Q4 e-tron 40 Sportback None 2023": 150,
    "Porsche Taycan Base None 2025": 300,
    "Porsche Taycan Base None 2022": 300,
    "Mini Cooper SE Electric 3rd 2024": 135,
    "Mercedes-Benz EQS EQS580 4MATIC Launch Edition None 2023": 400,
    "Mercedes-Benz EQS EQS580 4MATIC Launch Edition None 2024": 400,
    "Peugeot 208 GT None 2021": 100,
    'Peugeot 208 GT None 2023': 100,
    "Porsche Taycan Base None 2024": 300,
    "Tesla Model 3 RWD None 2022": 208,
    "Peugeot 2008 EV GT None 2022": 100,
    "Peugeot 2008 EV GT None 2025": 115,
    "Volvo C40 Twin Ultimate None 2023": 300,
    "Kia EV3 Standard 2WD Air 2025": 150,
    "Hyundai Ioniq5 Standard E-Value+ 2025": 170,
    "ChevroletGMDaewoo Bolt EV EV LT DLX None 2019": 150,
    "Porsche Taycan 4 Cross Turismo None 2023": 320,
    "Tesla Model 3 Long Range None 2024": 340,
    "Porsche Taycan 4 Cross Turismo None 2025": 320,
    "Tesla Model X 100D None 2019": 311,
    "Genesis G80 e-AWD None 2023": 272,
    "Kia Niro Taxi None 2019": 100,
    'Kia Niro Taxi None 2024': 150,
    "Kia Niro Taxi None 2023": 150,
    'Xin yuan ET Van Pro 2-Seater 2023': 70,
    'BMW i3 LUX None 2018': 125,
    "Kia Niro Taxi None 2022": 150,
    "Mercedes-Benz EQA EQA250 AMG Package None 2024": 140,
    "Audi e-tron 50 Quattro None 2021": 230,
    "Hyundai Ioniq5 Long range Exclusive 2022": 239,
    "Others Others Others EV None 2018": 0,
    "Kia RAY EV None 2013": 50,
    "Renault-KoreaSamsung SM3 SE Plus None 2014": 70,
    "Hyundai Kona Modren None 2020": 150,
    "Porsche Macan 4S None 2025": 280,
    "Tesla Model S 75D None 2017": 245,
    'Kia EV6 Standard 4WD Earth 2023': 239,
    'KG_Mobility_Ssangyong Torres TV7 None 2024': 170,
    "Tesla Model 3 Standard Range Plue None 2019": 208,
    "Kia Niro Air (Taxi Trim) None 2023": 150,
    "Tesla Model X Long Range None 2020": 350,
    "Kia EV6 GT 4WD None 2024": 430,
    "Kia EV6 GT 4WD None 2022": 430,
    'Kia EV4 Long Range 2WD Earth 2026': 150,   
    "Hyundai Ioniq6 Long Range Prestige 2024": 239,
    "Kia RAY Van 2-Seater Light 2024": 50,
    "Nissan Leaf EV None 2015": 80,
    "Renault-KoreaSamsung SM3 RE None 2014": 70,
    "Hyundai Ioniq N None 2017": 45,  # PHEV
    "Kia EV6 Long Range Air 2024": 239,
    "Genesis GV60 Standard AWD None 2025": 234,
    "Hyundai Ioniq Q None 2017": 45,  # PHEV
    "Kia EV6 Long Range 4WD Air 2023": 239,
    "Kia EV6 Long Range 4WD Air 2025": 239,
    "Mini Countryman ALL4 SE Favoured None 2025": 70,  # PHEV
    "Hyundai Ioniq6 Long Range AWD Exclusive 2023": 239,
    "Citroen-DS DS3 E-Tense Grand Chic None 2022": 115,
    "Citroen-DS DS3 E-Tense Grand Chic None 2021": 115,
    "Tesla Cybertruck AWD None 2024": 440,
    "Mercedes-Benz EQS Maybach EQS680 4MATIC None 2024": 484,
    "Audi Q4 e-tron 40 None 2023": 150,
    "Audi Q4 e-tron 40 None 2022": 150,
    "Hyundai Ioniq5 Long range Prestige 2023": 239,
    "Jeep Avenger Altitude None 2024": 115,
    "Hyundai Ioniq5 Long Range AWD Commercial Long Range Package 2023": 239,
    "Peugeot 2008 EV GT Line None 2021": 100,
    "ChevroletGMDaewoo Bolt EV EV Premier None 2017": 150,
    "Kia EV6 Long Range 4WD GT Line 2024": 239,
    'Renault-KoreaSamsung SM3 SE None 2018': 70,
    "Kia EV6 Long Range Air 2023": 239,
    "Kia Niro Noblesse None 2019": 100,
    "Kia Niro Noblesse None 2018": 100,
    "Audi Q4 e-tron 40 Premium Sportback None 2023": 150,
    "BMW iX3 M Sports None 2022": 210,
    "Mercedes-Benz EQE EQE500 4MATIC None 2023": 300,
    'Hyundai Ioniq9 Cruise Type 2WD 6-Seater Exclusive 2025': 239,
    "Mercedes-Benz EQA EQA250 AMG Package Plus None 2021": 140,
    "Tesla Model S 100D None 2019": 311,
    "Polestar Polestar 2 Standard Singlemotor None 2023": 170,
    'Polestar Polestar 2 Standard Singlemotor None 2025': 180,
    "Porsche Taycan GTS None 2024": 380,
    "Hyundai Kona Long Range Inspiration None 2023": 160,
    "Hyundai Kona Long Range Inspiration 2025": 160,
    'Hyundai Kona Long Range Inspiration 2023': 160,
    'BMW i7 xDrive 60 M Sport Individual None 2023': 400,
    'Hyundai Ioniq9 Cruise Type AWD 6-Seater Prestige 2025': 320,
    "Smart Fortwo ED(electric drive) None 2016": 55,
    "Kia RAY Air None 2024": 50,
    "KG_Mobility_Ssangyong KORANDO E5 None 2022": 91,
    "Hyundai Kona Long Range Premium 2023": 160,
    "Mini Cooper Resolute Edition 3rd 2024": 135,
    "Volvo XC40 Twin Ultimate None 2023": 300,
    "Hyundai Ioniq5 Long Range Commercial 2025": 239,
    "BMW iX xDrive40 First Edition None 2022": 250,
    "Porsche Taycan 4S Cross Turismo None 2024": 420,
    "Porsche Taycan 4S Cross Turismo None 2025": 420,
    "ChevroletGMDaewoo Bolt EV EV LT DLX None 2018": 150,
    "Genesis GV60 Standard None 2023": 234,
    "Tesla Model Y Long Range None 2021": 340,
    "Hyundai Ioniq5 Long Range AWD Prestige 2023": 239,
    "Hyundai Ioniq5 Long Range Prestige 2025": 239,
    "Tesla Model Y Performance None 2021": 377,
    'Tesla Model Y Performance None 2024': 393,
    'Tesla Model X P100D None 2016': 500,
    "Audi Q4 e-tron 40 Premium None 2024": 150,
    "Tesla Model Y Long Range None 2022": 340,
    "Hyundai Ioniq5 Long Range AWD Commercial Long Range Package 2022": 239,
    "Renault-KoreaSamsung Twizy Life(2-Seater) None 2020": 13,
    "Renault-KoreaSamsung SM3 RE None 2015": 70,
    "BMW i7 xDrive 60 M sport None 2025": 335,
    "Peugeot 208 GT Line None 2022": 100,
    "Kia Niro Prestige None 2021": 150,
    "Tesla Model Y RWD None 2025": 208,
    "Hyundai Ioniq6 Long Range Exclusive 2022": 239,
    "Tesla Model Y Long Range None 2025": 340,
    "BMW i5 eDrive 40 M Sport None 2024": 250,
    "Kia EV6 Long Range 4WD Earth 2025": 239,
    "Mini Aceman SE Favoured None 2025": 135,
    "Mercedes-Benz EQS EQS53 AMG 4MATIC+ None 2024": 400,
    "Mercedes-Benz EQB EQB300 4MATIC AMG Line None 2025": 140,
    "Kia EV6 Standard Air 2022": 170,
    "Jaguar I-PACE EV400 SE None 2019": 294,
    "Jaguar I-PACE EV400 SE None 2020": 294,
    "BMW i5 eDrive 40 M Sport Pro None 2024": 250,
    "Hyundai Ioniq5 Long Range AWD Prestige 2022": 239,
    "Hyundai Ioniq Q None 2018": 45,  # PHEV
    "ChevroletGMDaewoo 볼트 EUV Premier None 2022": 150,
    "Hyundai Kona Long Range Inspiration 2024": 160,
    "Kia EV6 Long Range 4WD Air 2024": 239,
    "BMW i7 eDrive 50 M Sport None 2024": 335,
    "Kia EV6 Long Range 4WD Earth 2024": 239,
    "BMW i7 M70 xDrive None 2024": 400,
    "BMW i4 eDrive40 M Sports Pro None 2024": 250,
    "Mercedes-Benz EQA EQA250 Electric Art None 2024": 140,
    "Mercedes-Benz EQA EQA250 Electric Art None 2023": 140,
    "Porsche Taycan 4S Cross Turismo None 2023": 420,
    "Mercedes-Benz EQS EQS450 4MATIC None 2024": 400,
    "Mini Cooper Gen ZE Edition 3rd 2022": 135,
    "Kia EV6 Long Range Air 2022": 239,
    "Hyundai Ioniq5 Long range Commercial Long Range Package 2023": 239,
    "Hyundai Ioniq5 Long range Commercial Long Range Package 2022": 239,
    "Audi Q4 e-tron 45 Sportback None 2025": 180,
    "BMW iX xDriveM60 None 2024": 385,
    "Tesla Model 3 Performance None 2020": 377,
    "GMC Hummer EV e4WD None 2024": 1_012,  # 1 MW :)
    "Porsche Taycan Turbo Cross Turismo None 2023": 460,
    "ChevroletGMDaewoo Bolt EV EV LT None 2019": 150,
    "ChevroletGMDaewoo Bolt EV EV Premier None 2018": 150,
    "Renault-KoreaSamsung SM3 RE None 2017": 70,
    "Tesla Model X AWD None 2024": 500,
    'Tesla Model X AWD None 2025': 500,
    "Porsche Taycan GTS None 2022": 460,
    "BMW i4 eDrive40 M Sports None 2024": 250,
    "Volvo C40 Twin Ultimate None 2024": 300,
    "Kia Niro Air None 2023": 150,
    "BMW iX3 M Sports None 2024": 210,
    "BMW i3 SOL+ None 2019": 100,
    "Kia RAY EV None 2016": 50,
    "Porsche Taycan 4S Cross Turismo None 2022": 420,
    "Tesla Model Y Performance None 2022": 377,
    "Kia RAY Van 1-Seater AIr 2025": 50,
    "BMW i4 M50 Pro None 2022": 400,
    "Mercedes-Benz EQS EQS580 4MATIC None 2023": 400,
    "BMW iX xDrive40 Sport Plus None 2022": 250,
    "Genesis G80 e-AWD None 2024": 272,
    "BMW i4 M50 Pro None 2024": 400,
    "Hyundai Ioniq5 N None 2024": 310,
    "Mercedes-Benz EQA EQA250 None 2022": 140,
    "Mercedes-Benz EQA EQA250 AMG Package Plus None 2022": 140,
    "Audi e-tron GT GT quattro Premium None 2022": 440,
    "Audi e-tron GT GT quattro None 2022": 440,
    "Peugeot 2008 EV Allure None 2023": 100,
    "Tesla Model X Performance None 2020": 451,
    "Kia EV3 Long Range 2WD AIr 2025": 150,
    "Peugeot 208 Allure None 2022": 100,
    "Kia Soul Prestige None 2021": 150,
    "ChevroletGMDaewoo Bolt EV EV LT DLX None 2020": 150,
    "Volkswagen ID.4 Pro None 2023": 150,
    "Volkswagen ID.4 Pro None 2025": 150,
    "Hyundai Kona Standard Premium 2023": 115,
    "ChevroletGMDaewoo Bolt EV EV LT DLX None 2021": 150,
    "Mercedes-Benz EQB EQB300 4MATIC None 2022": 140,
    "Mercedes-Benz EQE EQE350+ None 2022": 300,
    "Tesla Model 3 Standard Range Plue None 2022": 208,
    "BMW iX xDrive50 Sports Plus None 2022": 385,
    "Renault-KoreaSamsung SM3 SE None 2016": 70,
    "Hyundai Ioniq6 Long Range AWD Prestige 2023": 239,
    "Hyundai Ioniq6 Long Range AWD Prestige 2024": 239,
    "Others Others Others EV None 2021": 0,
    "Audi Q8 e-tron 55 Quattro Sportback None 2024": 420,
    "Smart Fortwo EQ None 2019": 55,
    "Smart Fortwo EQ None 2018": 55,
    "Porsche Taycan Base None 2023": 105,
    "Kia Niro Light (Taxi Trim) None 2023": 150,
    "Kia EV6 Long Range Light 2022": 239,
    "Renault-KoreaSamsung Twizy Cargo(1-seater+Trunk) None 2020": 13,
    "Hyundai Ioniq5 Long range Prestige 2024": 239,
    "Tesla Model X Plaid None 2023": 761,
    "Kia Soul Noblesse None 2019": 150,
    "Mercedes-Benz EQS EQS450+ AMG Line None 2022": 400,
    "Mercedes-Benz EQA EQA250 AMG Line None 2024": 140,
    "BMW iX2 eDrive 20 M Sport None 2025": 150,
    "Renault-KoreaSamsung Zoe Intens None 2021": 38,
    "Kia EV6 Long Range 4WD GT Line 2022": 239,
    "Mercedes-Benz EQS EQS53 AMG 4MATIC+ None 2023": 400,
    "Genesis GV60 Standard AWD None 2022": 239,
    "BMW i3 LUX None 2016": 30,
    "Others Others Others EV None 2023": 0,
    "Kia EV6 Long Range 4WD GT Line 2025": 239,
    "Rolls-Royce Spectre Coupe None 2024": 430,
    "Tesla Model X AWD None 2023": 500,
    "BMW i4 eDrive40 Individual None 2024": 250,
    "Volkswagen ID.4 Pro None 2022": 150,
    "Kia Niro Prestige None 2020": 150,
    "BMW i7 xDrive 60 M sport None 2023": 335,
    "Kia EV6 Long Range 4WD Earth 2023": 239,
    "Hyundai Kona Modren None 2019": 150,
    "Porsche Taycan Turbo None 2022": 460,
    "Mercedes-Benz EQA EQA250 AMG Package None 2025": 140,
    "Tesla Model S Long Range None 2020": 340,
    "Genesis GV60 Performance AWD None 2022": 239,
    "Tesla Model S Plaid None 2023": 761,
    "Mercedes-Benz EQE EQE350 4MATIC None 2023": 300,
    "Audi Q4 e-tron 40 Premium None 2023": 150,
    "Hyundai Ioniq6 Standard Exclusive 2023": 111,
    "Mercedes-Benz EQS EQS450+ None 2024": 400,
    "Nissan Leaf EV S None 2019": 110,
    "Hyundai Ioniq5 Long Range AWD Prestige 2025": 239,
    "BMW i4 M50 Pro None 2023": 400,
    "ChevroletGMDaewoo Bolt EV EV Premier None 2020": 150,
    "Kia EV6 Long Range GT Line 2022": 239,
    "Peugeot 208 GT None 2022": 100,
    "BYD Atto 3 Plus None 2025": 150,
    "BMW i3 SOL+ None 2020": 130,
    "Tesla Model 3 RWD None 2025": 208,
    'Tesla Model 3 RWD None 2020': 208,
    "Mercedes-Benz EQB EQB300 4MATIC None 2023": 140,
    "Porsche Taycan Turbo S None 2024": 460,
    "Kia EV6 Long Range 2WD Earth 2025": 239,
    "Hyundai Ioniq6 Long Range E-Lite 2023": 239,
    "Tesla Model 3 Performance None 2024": 377,
    "BMW i3 SOL None 2015": 125,
    "BMW i3 SOL None 2014": 125,
    "Porsche Macan Turbo None 2025": 460,
    "KG_Mobility_Ssangyong Torres E7 None 2025": 100,
    "Audi e-tron 55 Quattro Sportback None 2021": 265,
    "Audi Q8 e-tron 55 Quattro None 2024": 420,
    "Audi e-tron GT GT quattro Premium None 2023": 440,
    "Porsche Taycan Turbo None 2021": 460,
    "Genesis GV60 Standard None 2025": 239,
    "Porsche Taycan Base None 2021": 105,
    "Tesla Model X Long Range None 2023": 340,
    "Hyundai Ioniq9 Cruise Type 2WD 6-Seater Prestige 2025": 100,
    "Hyundai Ioniq6 Long Range Prestige 2025": 239,
    "Porsche Taycan Turbo Cross Turismo None 2024": 460,
    "Audi e-tron 55 Quattro None 2022": 300,
    "Citroen-DS DS3 E-Tense Grand Chic None 2023": 115,
    "BMW i3 LUX None 2017": 125,
    "Audi e-tron 55 Quattro None 2020": 300,
    "BMW i4 M50 Pro Special Edition None 2024": 400,
    "Genesis GV60 Standard None 2022": 239,
    "ChevroletGMDaewoo Bolt EV EV Premier None 2019": 150,
    "Kia EV6 GT 4WD None 2023": 239,
    "Mercedes-Benz EQE EQE53 AMG 4MATIC+ None 2023": 300,
    "Polestar Polestar 2 Longrange Dualmotor None 2022": 300,
    "Hyundai Ioniq5 Long Range AWD Exclusive 2023": 239,
    "Mercedes-Benz EQE EQE350 4MATIC None 2024": 300,
    "Lexus RZ Luxury None 2023": 230,
    "BMW iX3 M Sports None 2023": 210,
    "Kia RAY EV None 2017": 50,
    "Tesla Model 3 Standard Range Plue None 2020": 208,
    "Kia Niro Earth None 2023": 150,
    "Tesla Model X Long Range None 2019": 340,
    "Mercedes-Benz EQE EQE300 None 2023": 180,
    "Kia EV6 Standard Earth 2024": 170,
    "Kia EV6 Standard Earth 2023": 170,
    "Hyundai Kona Standard Premium 2025": 115,
}