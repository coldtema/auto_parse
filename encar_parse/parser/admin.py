from django.contrib import admin
from .models import TruckOption, OptionCategory, CarOption, CarManufacturer, Config


@admin.register(TruckOption)
class TruckOptionAdmin(admin.ModelAdmin):
    list_display = ['encar_id', 'name', 'category']


@admin.register(CarOption)
class CarOptionAdmin(admin.ModelAdmin):
    list_display = ['encar_id', 'name', 'category']


@admin.register(OptionCategory)
class OptionCategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(CarManufacturer)
class CarManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'value_key', 'value_name', 'car_count', 'is_foreign']


@admin.register(Config)
class ConfigAdmin(admin.ModelAdmin):
    list_display = ['delivery_cost', 'extra_expenses', 'rate', 'asia_services', 'dealer_services', 'korea_invoice', 'broker_cost']