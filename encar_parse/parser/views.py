from django.shortcuts import render
from django.http import HttpResponse
from parser.raw_parser import CarParser, TruckParser
from parser.async_parser import AsyncCarParser, AsyncTruckParser



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
