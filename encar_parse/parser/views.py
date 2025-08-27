from django.shortcuts import render
from django.http import HttpResponse
from parser.raw_parser import CarParser, TruckParser
from parser.async_parser import AsyncCarParser, AsyncTruckParser, DuplicateClearer
from .diag_parser import AsyncCarDiagParser
from .record_parser import AsyncCarRecordParser
from .forms import CarArtikulForm
from .models import Car, Truck, CarOption, TruckOption, OptionCategory



def car(request):
    # c_p = CarParser()
    # c_p.run()
    # del c_p
    c_p = AsyncCarParser()
    c_p.run()
    del c_p
    d_c = DuplicateClearer()
    d_c.go_through_unique_dummy_ids()
    del d_c
    c_p = AsyncCarDiagParser()
    c_p.run()
    del c_p
    c_p = AsyncCarRecordParser()
    c_p.run()
    del c_p
    return HttpResponse('oks')


def truck(request):
    t_p = TruckParser()
    t_p.run()
    del t_p
    return HttpResponse('oks')


def async_truck(request):
    t_p = AsyncTruckParser()
    t_p.run()
    del t_p
    return HttpResponse('oks')


def async_car(request):
    c_p = AsyncCarParser()
    c_p.run()
    del c_p
    d_c = DuplicateClearer()
    d_c.go_through_unique_dummy_ids()
    del d_c
    return HttpResponse('oks')


def diag_car(request):
    c_p = AsyncCarDiagParser()
    c_p.run()
    del c_p
    return HttpResponse('oks')


def record_car(request):
    c_p = AsyncCarRecordParser()
    c_p.run()
    del c_p
    return HttpResponse('oks')


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


def vechile(request):
    photo_url_params = '?impolicy=heightRate&rh=696&cw=1160&ch=696&cg=Center&wtmk=https://ci.encar.com/wt_mark/w_mark_04.png'
    artikul = request.GET.get('artikul')
    kind = request.GET.get('kind')
    if artikul.isdigit():
        if kind == 'truck':
            all_truck_options = OptionCategory.objects.filter(vechile='TRUCK').prefetch_related('truckoption_set')
            current_truck_options = list(map(lambda x: TruckOption.objects.get(encar_id=x).id, eval(truck.options)))
            photo_list = []
            sorted_codes = sorted(set(map(lambda x: int(x), eval(truck.photos_codes))))
            for i in sorted_codes:
                if i < 10: photo_list.append(f'{truck.photo_url}00{i}.jpg{photo_url_params}')
                else: photo_list.append(f'{truck.photo_url}0{i}.jpg{photo_url_params}') 
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
                                                                   'photo_list': photo_list,
                                                                   })
        if kind == 'car':
            try:
                car = Car.objects.get(encar_id=artikul)
            except:
                print('Ищет по dummy')
                car = Car.objects.get(dummy_id=artikul)
            all_car_options = OptionCategory.objects.filter(vechile='CAR').prefetch_related('caroption_set')
            current_car_options = list(map(lambda x: CarOption.objects.get(encar_id=x).id, eval(car.options)))
            photo_list = []
            sorted_codes = sorted(set(map(lambda x: int(x), eval(car.photos_codes))))
            for i in sorted_codes:
                if i < 10: photo_list.append(f'{car.photo_url}00{i}.jpg{photo_url_params}')
                else: photo_list.append(f'{car.photo_url}0{i}.jpg{photo_url_params}') 
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
                accidents = enumerate(record.accident_set.all(), 1)
            print(accidents)
            return render(request, 'parser/vechile.html', context={'all_options_list': all_car_options,
                                                                   'current_options_list': current_car_options,
                                                                   'full_name': f'{car.manufacturer} {car.model} {car.version}',
                                                                   'photo_list': photo_list,
                                                                   'encar_id': car.encar_id,
                                                                   'category': car.version_details,
                                                                   'kind': 'CAR',
                                                                   'transmission': car.transmission,
                                                                   'mileage': f'{car.mileage} км',
                                                                   'price': f'{car.price/100} млн Вон',
                                                                   'fuel_type': car.fuel_type,
                                                                   'model_year': car.model_year,
                                                                   'color': car.color,
                                                                   'engine_capacity': f'{car.engine_capacity} см²',
                                                                   'encar_url': car.url,
                                                                   'release_date': f'{str(car.release_date)[4:]}.{str(car.release_date)[:-2]}',
                                                                   'diagnosis': diagnosis,
                                                                   'record': record,
                                                                   'accidents': accidents
                                                                   })
        return render(request, 'parser/vechile.html')
    return render(request, 'parser/vechile.html')