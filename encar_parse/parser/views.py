from django.shortcuts import render
from .forms import CarArtikulForm
from .models import Car, Truck, CarOption, TruckOption, OptionCategory, CarPhoto, TruckPhoto, Config
import time
import traceback
from .forms import CarCalcForm
# from .pdf_generator import generate_pdf
import io
from django.http import FileResponse, JsonResponse
import requests

def time_count(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        f = func(*args, **kwargs)
        print(f'{time.time()-start} сек')
        return f
    return wrapper


def index(request):
    if request.method == 'POST':
        form = CarArtikulForm(request.POST)
        if form.is_valid():
            artikul = form.cleaned_data['artikul']
            kind = form.cleaned_data['kind']
            context = {
            'artikul': artikul,
            'kind': kind,
            }
        return render(request, 'parser/index.html', context)
    else:
        form = CarArtikulForm()
    return render(request, 'parser/index.html', {'form': form})

@time_count
def vechile(request):
    artikul = request.GET.get('artikul')
    kind = request.GET.get('kind')
    if artikul.isdigit(): 
        if kind == 'truck':
            try:
                truck = Truck.objects.get(encar_id=artikul)
            except:
                print('Ищет по dummy')
                truck = Truck.objects.get(dummy_id=artikul)
            all_truck_options = OptionCategory.objects.filter(vechile='TRUCK').prefetch_related('truckoption_set')
            current_truck_options = list(map(lambda x: TruckOption.objects.get(encar_id=x).id, eval(truck.options)))
            photo_list = TruckPhoto.objects.filter(truck_id=truck.pk).order_by('order_number').values('link')
            return render(request, 'parser/vechile.html', context={'all_options_list': all_truck_options,
                                                                   'current_options_list': current_truck_options,
                                                                   'full_name': f'{truck.manufacturer} {truck.model} {truck.version}',
                                                                   'encar_id': truck.encar_id,
                                                                   'category': truck.version_details,
                                                                   'kind': 'TRUCK',
                                                                   'transmission': truck.transmission,
                                                                   'mileage': f'{truck.mileage} км',
                                                                   'price': f'{truck.price/100} млн Вон',
                                                                   'fuel_type': truck.fuel_type,
                                                                   'color': truck.color,
                                                                   'engine_capacity': f'{truck.engine_capacity} см²',
                                                                   'release_date': f'{str(truck.release_date)[4:]}.{str(truck.release_date)[:-2]}',
                                                                   'encar_url': truck.url,
                                                                   'photo_list': photo_list,                                                         })
        if kind == 'car':
            try:
                try:
                    car = Car.objects.get(encar_id=artikul)
                except:
                    print('Ищет по dummy')
                    car = Car.objects.get(dummy_id=artikul)
                all_car_options = OptionCategory.objects.filter(vechile='CAR').prefetch_related('caroption_set')
                current_car_options = list(map(lambda x: CarOption.objects.get(encar_id=x).id, eval(car.options)))
                photo_list = CarPhoto.objects.filter(car_id=car.pk).order_by('order_number').values('link')
                try:
                    diagnosis = car.diagnosis
                except:
                    diagnosis = None

                try:
                    record = car.car_record
                except:
                    record = None
                accidents = None
                if record:
                    accidents = enumerate(record.caraccident_set.all(), 1)
                return render(request, 'parser/vechile.html', context={'all_options_list': all_car_options,
                                                                    'current_options_list': current_car_options,
                                                                    'full_name': f'{car.manufacturer} {car.model} {car.version}',
                                                                    'photo_list': photo_list,
                                                                    'encar_id': car.encar_id,
                                                                    'category': car.version_details,
                                                                    'kind': 'CAR',
                                                                    'transmission': car.transmission,
                                                                    'mileage': f'{car.mileage} км',
                                                                    'ru_price': f'{car.ru_price} ₽',
                                                                    'customs_duty': f'{car.customs_duty} ₽',
                                                                    'recycling_fee': f'{car.recycling_fee} ₽',
                                                                    'fuel_type': car.fuel_type,
                                                                    'model_year': car.model_year,
                                                                    'color': car.color,
                                                                    'engine_capacity': f'{car.engine_capacity} см²',
                                                                    'encar_url': car.url,
                                                                    'release_date': f'{str(car.release_date)[4:]}.{str(car.release_date)[:-2]}',
                                                                    'diagnosis': diagnosis,
                                                                    'record': record,
                                                                    'accidents': accidents,
                                                                    #'final_price': f'{car.recycling_fee + car.customs_duty + car.ru_price + 95000 + 20000 + 97000} ₽',
                                                                    })
            except:
                traceback.print_exc()
        return render(request, 'parser/vechile.html')
    return render(request, 'parser/vechile.html')




def calc_view(request):
    if request.method == "POST":
        form = CarCalcForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            data['encar_url'] = data['encar_url'].split('?')[0]
            print(data['encar_url'])
            car = Car.objects.filter(url=data['encar_url']).last()
            if car:
                data['ru_price'] = str(round(float(data["rate"]) * float(data["korean_price"])))
                data['customs_duty'] = car.customs_duty
                data['recycling_fee'] = car.recycling_fee
                data['full_name'] = f'{car.manufacturer.value_name} {car.model}'
                data["dealer_services"] = str(round(float(data["rate"]) * float(data["dealer_services"])))
                data["korea_invoice"] = str(round(float(data["rate"]) * float(data["korea_invoice"])))
                
                photos = car.carphoto_set.all()[:2]  # берём максимум 2 фото

                data['photo'] = photos[0].link
                data['photo2'] = photos[1].link
                
            pdf_buffer = io.BytesIO()
            generate_pdf(data, pdf_buffer)
            pdf_buffer.seek(0)

            return FileResponse(pdf_buffer, as_attachment=True, filename="AsiaAlliance_Report.pdf")

    else:
        form = CarCalcForm()

    return render(request, "parser/calculator.html", {"form": form})


def api_view(request):
    if request.method == 'GET':
        url = request.GET.get("url")
        url = url.split('?')[0]
        print(url)
        name = []

        car = Car.objects.filter(url=url).last()

        if car.manufacturer.value_name:
            name.append(car.manufacturer.value_name)

        if car.model:
            name.append(car.model)

        if car.version:
            name.append(car.version)

        if car.model_year:
            name.append(f'({car.model_year})')

        name = ' '.join(name)

        currency_dict = dict()

        response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

        currency_dict['krw/rub'] = response['Valute']['KRW']['Value']/response['Valute']['KRW']['Nominal']
        currency_dict['usd/rub'] = response['Valute']['USD']['Value']/response['Valute']['USD']['Nominal']


        if currency_dict['usd/rub'] != float(request.GET.get("usd_rate")):
            currency_dict['usd/rub'] = float(request.GET.get("usd_rate"))

        currency_dict['krw/usd'] = currency_dict['krw/rub'] / currency_dict['usd/rub']


        return JsonResponse({
        "found": True,
        "korean_price": round(car.price * 10000 * currency_dict['krw/usd']),
        "ru_price": car.ru_price,
        "car_name": name
    })