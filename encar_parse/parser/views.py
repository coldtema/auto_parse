from django.shortcuts import render
from django.http import HttpResponse
from parser.raw_parser import CarParser, TruckParser
from parser.async_parser import AsyncCarParser, AsyncTruckParser
from .forms import CarArtikulForm
from .models import Car, Truck, CarOption, TruckOption, OptionCategory



def car(request):
    c_p = CarParser()
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
    artikul = request.GET.get('artikul')
    kind = request.GET.get('kind')
    if artikul.isdigit():
        if kind == 'truck':
            truck = Truck.objects.get(encar_id=artikul)
            all_truck_options = OptionCategory.objects.filter(vechile='TRUCK').prefetch_related('truckoption_set')
            current_truck_options = list(map(lambda x: TruckOption.objects.get(encar_id=x).id, eval(truck.options)))
            return render(request, 'parser/vechile.html', context={'all_options_list': all_truck_options,
                                                                   'current_options_list': current_truck_options,
                                                                   'full_name': f'{truck.manufacturer} {truck.model} {truck.version}',
                                                                   'number_of_photos': truck.number_of_photos,
                                                                   'photo_url': truck.photo_url,
                                                                   'encar_id': truck.encar_id,
                                                                   'category': truck.version_details,
                                                                   'kind': 'TRUCK'
                                                                   })
        if kind == 'car':
            car = Car.objects.get(encar_id=artikul)
            all_car_options = OptionCategory.objects.filter(vechile='CAR').prefetch_related('caroption_set')
            current_car_options = list(map(lambda x: CarOption.objects.get(encar_id=x).id, eval(car.options)))
            return render(request, 'parser/vechile.html', context={'all_options_list': all_car_options,
                                                                   'current_options_list': current_car_options,
                                                                   'full_name': f'{car.manufacturer} {car.model} {car.version}',
                                                                   'number_of_photos': car.number_of_photos,
                                                                   'photo_url': car.photo_url,
                                                                   'encar_id': car.encar_id,
                                                                   'category': car.version_details,
                                                                   'kind': 'CAR',
                                                                   })
        return render(request, 'parser/vechile.html')
    return render(request, 'parser/vechile.html')