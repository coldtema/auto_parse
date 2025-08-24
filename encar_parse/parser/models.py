from django.db import models


class FuelType(models.TextChoices):
    GASOLINE = "G", "Бензин"
    DIESEL = "D", "Дизель"
    LPG = "L", "Газ"
    GASOLINE_ELECTRIC = "GE", "Бензин + Электро"
    DIESEL_ELECTRIC = "DE", "Дизель + Электро"
    LPG_ELECTRIC = "LE", "Газ + Электро"
    LPG_GASOLINE = "LG", "Газ + Бензин"
    ELECTRIC = "E", "Электро"
    HYDROGEN = "HY", "Водород"


class Car(models.Model):
    encar_id = models.BigIntegerField(verbose_name='Внутреннее id encar', unique=True)
    url = models.URLField()
    category = models.CharField(max_length=1)
    trust_service = models.CharField(max_length=50)
    inspection = models.BooleanField(default=False)
    record = models.BooleanField(default=False)
    resume = models.BooleanField(default=False)
    photo_url = models.CharField(max_length=256)
    number_of_photos = models.IntegerField()
    manufacturer = models.CharField(max_length=128, null=True, blank=True)
    model = models.CharField(max_length=128, null=True, blank=True)
    version = models.CharField(max_length=128, null=True, blank=True)
    version_details = models.CharField(max_length=128, null=True, blank=True)
    color = models.CharField(max_length=128, null=True, blank=True)
    engine_capacity = models.IntegerField(null=True, blank=True)
    transmission = models.CharField(max_length=128)
    fuel_type = models.CharField(max_length=2, choices=FuelType.choices, default=FuelType.GASOLINE)
    release_date = models.IntegerField()
    model_year = models.IntegerField()
    mileage = models.IntegerField()
    price = models.BigIntegerField()
    sell_type = models.CharField(max_length=128)
    updated = models.DateTimeField()
    city = models.CharField(max_length=128)
    showroom_name = models.CharField(max_length=256)
    dealer_name = models.CharField(max_length=256)


class Truck(models.Model):
    encar_id = models.BigIntegerField(verbose_name='Внутреннее id encar', unique=True)
    url = models.URLField()
    category = models.CharField(max_length=1)
    trust_service = models.CharField(max_length=50)
    inspection = models.BooleanField(default=False)
    record = models.BooleanField(default=False)
    resume = models.BooleanField(default=False)
    photo_url = models.CharField(max_length=256)
    number_of_photos = models.IntegerField()
    manufacturer = models.CharField(max_length=128, null=True, blank=True)
    model = models.CharField(max_length=128, null=True, blank=True)
    version = models.CharField(max_length=128, null=True, blank=True)
    version_details = models.CharField(max_length=128, null=True, blank=True)
    color = models.CharField(max_length=128, null=True, blank=True)
    engine_capacity = models.IntegerField(null=True, blank=True)
    horse_power = models.IntegerField(null=True, blank=True)
    capacity = models.CharField(max_length=32)
    transmission = models.CharField(max_length=128)
    fuel_type = models.CharField(max_length=2, choices=FuelType.choices, default=FuelType.GASOLINE)
    release_date = models.IntegerField()
    model_year = models.IntegerField()
    mileage = models.IntegerField()
    price = models.BigIntegerField()
    usage = models.CharField(max_length=128)
    updated = models.DateTimeField()
    city = models.CharField(max_length=128)

class Vechile(models.TextChoices):
    CAR = 'CAR', 'CAR'
    TRUCK = 'TRUCK', 'TRUCK'

class OptionCategory(models.Model):
    name = models.CharField(max_length=64)
    vechile = models.CharField(max_length=5, choices=Vechile.choices, default=Vechile.TRUCK)

    def __str__(self):
        return self.name

class TruckOption(models.Model):
    encar_id = models.CharField(max_length=3)
    name = models.CharField(max_length=128)
    category = models.ForeignKey(OptionCategory, on_delete=models.CASCADE)


class CarOption(models.Model):
    encar_id = models.CharField(max_length=3)
    name = models.CharField(max_length=128)
    category = models.ForeignKey(OptionCategory, on_delete=models.CASCADE)



