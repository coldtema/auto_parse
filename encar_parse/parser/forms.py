from django import forms
from .models import Config
import requests

class CarArtikulForm(forms.Form):
    artikul = forms.CharField(
        label='Артикул',
        max_length=100,
        widget=forms.TextInput(attrs={'placeholder': 'Например: 38877922', 'class': 'input'}))
    
    KIND_CHOICES = (
        ('car', 'Легковой (car)'),
        ('truck', 'Грузовой (truck)'))


    kind = forms.ChoiceField(
        label='Тип ТС',
        choices=KIND_CHOICES,
        widget=forms.RadioSelect)
    

class CarCalcForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        cfg = Config.objects.first()
        if cfg:
            self.fields["delivery_cost"].initial = cfg.delivery_cost
            self.fields["extra_expenses"].initial = cfg.extra_expenses
            self.fields["asia_services"].initial = cfg.asia_services
            self.fields["dealer_services"].initial = cfg.dealer_services
            self.fields["korea_invoice"].initial = cfg.korea_invoice
            self.fields["broker_cost"].initial = cfg.broker_cost

        self.fields["rate"].initial = self.get_rate()
            

    encar_url = forms.CharField(label="Ссылка на Encar")

    korean_price = forms.CharField(label="Стоимость автомобиля на сегодняшний день (в $)", required=False)

    delivery_cost = forms.CharField(label="Стоимость доставки (в $)", required=False)
    extra_expenses = forms.CharField(label="Доп. расходы (в руб.)", required=False)
    rate = forms.CharField(label="Курс $", required=False)

    asia_services = forms.CharField(label="Услуги Asia Alliance (в %)", required=False)
    dealer_services = forms.CharField(label="Услуги дилера (в $)", required=False)
    korea_invoice = forms.CharField(label="Оплата по инвойсу в Корею (в $)", required=False)

    broker_cost = forms.CharField(label="Брокер / СВХ / Лаборатория (в руб.)", required=False)
    
    horse_power = forms.CharField(label="Лошадиные силы", required=False)
    customs_fee = forms.CharField(label="Таможенные платежи", required=False)
    recycling_fee = forms.CharField(label="Утилизационный сбор", required=False)


    def get_rate(self):
        try:
            response = requests.get('https://moscaex.online/api2/usdt_rate').json()
            return response['buy']
        except:
            response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
            return response['Valute']['USD']['Value']/response['Valute']['USD']['Nominal']
        

class CarCalcForm2(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        cfg = Config.objects.first()
        if cfg:
            self.fields["delivery_cost_korea_bishkek"].initial = cfg.delivery_cost_korea_bishkek
            self.fields["broker_cost_bishkek"].initial = cfg.broker_cost_bishkek
            self.fields["delivery_cost_bishkek_moscow"].initial = cfg.delivery_cost_bishkek_moscow
            self.fields["asia_services"].initial = cfg.asia_services
            self.fields["lab_moscow"].initial = cfg.lab_moscow

        self.fields["rate"].initial = self.get_rate()
            

    encar_url = forms.CharField(label="Ссылка на Encar")

    korean_price = forms.CharField(label="Стоимость автомобиля на сегодняшний день (в $)", required=False)
    delivery_cost_korea_bishkek = forms.CharField(label="Стоимость доставки из Кореи в Бишкек (в $)", required=False)
    asia_services = forms.CharField(label="Услуги Asia Alliance (в %)", required=False)
    dealer_services = forms.CharField(label="Услуги дилера (в $)", required=False, initial=0)
    korea_invoice = forms.CharField(label="Оплата по инвойсу в Корею (в $)", required=False, initial=0)

    customs_fee_bishkek = forms.CharField(label="Таможенные платежи в Бишкеке (в $)", required=False, initial=0)
    broker_cost_bishkek = forms.CharField(label="Стоимость услуг брокера в Бишкеке (в $)", required=False)
    delivery_cost_bishkek_moscow = forms.CharField(label="Стоимость доставки из Бишкека в Москву (в $)", required=False)
    bishkek_invoice = forms.CharField(label="Оплата по инвойсу в Бишкеке (в $)", required=False, initial=0)

    lab_moscow = forms.CharField(label="Лаборатория в Москве (в руб.)", required=False)
    recycling_fee = forms.CharField(label="Утилизационный сбор", required=False, initial=0)


    rate = forms.CharField(label="Курс $", required=False)
    horse_power = forms.CharField(label="Лошадиные силы", required=False)


    def get_rate(self):
        try:
            response = requests.get('https://moscaex.online/api2/usdt_rate').json()
            return response['buy']
        except:
            response = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
            return response['Valute']['USD']['Value']/response['Valute']['USD']['Nominal']