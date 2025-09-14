from celery import shared_task, chain
from parser.parsers import async_clearer, async_parser, diag_parser, raw_parser, record_parser
from parser import ru_price_calc
import traceback


@shared_task
def get_raw_car_info():
    '''Собираем инфу из полного каталога машин (батч по пробегам)'''
    p = raw_parser.CarParser()
    try:
        p.run()
    except Exception as e:
        tb = traceback.format_exc() 
        print(f"Ошибка: {e}\n{tb}")
    del p
    return True


@shared_task
def get_raw_truck_info():
    '''Собираем инфу из полного каталога траков (батч по пробегам)'''
    p = raw_parser.TruckParser()
    try:
        p.run()
    except Exception as e:
        tb = traceback.format_exc() 
        print(f"Ошибка: {e}\n{tb}")
    del p
    return True


@shared_task
def get_full_car_info():
    '''Собираем полую инфу отдельно из каждого url машины'''
    p = async_parser.AsyncCarParser()
    try:
        p.run()
    except Exception as e:
        tb = traceback.format_exc() 
        print(f"Ошибка: {e}\n{tb}")
    del p
    return True


@shared_task
def get_full_truck_info():
    '''Собираем полую инфу отдельно из каждого url трака'''
    p = async_parser.AsyncTruckParser()
    try:
        p.run()
    except Exception as e:
        tb = traceback.format_exc() 
        print(f"Ошибка: {e}\n{tb}")
    del p
    return True


@shared_task
def delete_fake_cars():
    '''Удаляем машины не для продажи в рф + дубли'''
    p = async_parser.CarDuplicateClearer()
    try:
        p.go_through_unique_dummy_ids()
    except Exception as e:
        tb = traceback.format_exc() 
        print(f"Ошибка: {e}\n{tb}")
    del p
    return True


@shared_task
def delete_fake_trucks():
    '''Удаляем траки не для продажи в рф + дубли'''
    p = async_parser.TruckDuplicateClearer()
    try:
        p.go_through_unique_dummy_ids()
    except Exception as e:
        tb = traceback.format_exc() 
        print(f"Ошибка: {e}\n{tb}")
    del p
    return True


@shared_task
def get_car_diagnosis():
    '''Собираем инфу о состоянии кузова всех машин'''
    p = diag_parser.AsyncCarDiagParser()
    try:
        p.run()
    except Exception as e:
        tb = traceback.format_exc() 
        print(f"Ошибка: {e}\n{tb}")
    del p
    return True


@shared_task
def get_truck_diagnosis():
    '''Собираем инфу о состоянии кузова всех траков'''
    p = diag_parser.AsyncTruckDiagParser()
    try:
        p.run()
    except Exception as e:
        tb = traceback.format_exc() 
        print(f"Ошибка: {e}\n{tb}")
    del p
    return True


@shared_task
def get_car_record():
    '''Собираем инфу о страховых случаях каждой машины'''
    p = record_parser.AsyncCarRecordParser()
    try:
        p.run()
    except Exception as e:
        tb = traceback.format_exc() 
        print(f"Ошибка: {e}\n{tb}")
    del p
    return True


@shared_task
def count_duties_and_ru_price():
    '''Расчет таможенных сборов и ру-цены для каждой машины'''
    p = ru_price_calc.RuPriceCalc()
    try:
        p.run()
    except Exception as e:
        tb = traceback.format_exc() 
        print(f"Ошибка: {e}\n{tb}")
    del p
    return True


@shared_task
def delete_not_avaliable_cars():
    '''Удаление неактуальных объявлений машин'''
    p = async_clearer.AsyncCarClearer()
    try:
        p.run()
    except Exception as e:
        tb = traceback.format_exc() 
        print(f"Ошибка: {e}\n{tb}")
    del p
    return True


@shared_task
def delete_not_avaliable_trucks():
    '''Удаление неактуальных объявлений траков'''
    p = async_clearer.AsyncTruckClearer()
    try:
        p.run()
    except Exception as e:
        tb = traceback.format_exc() 
        print(f"Ошибка: {e}\n{tb}")
    del p
    return True


@shared_task
def main_task():
    '''Полностью добавляет новые машины со всей подробной инфой в бд (раз в 3 часа)'''
    chain(
        delete_not_avaliable_cars.si(),
        count_duties_and_ru_price.si(),
        get_raw_car_info.si(),
        get_full_car_info.si(),
        delete_fake_cars.si(),
        get_car_diagnosis.si(),
        get_car_record.si(),
        count_duties_and_ru_price.si(),
        delete_not_avaliable_trucks.si(),
        get_raw_truck_info.si(),
        get_full_truck_info.si(),
        delete_fake_trucks.si(),
        get_truck_diagnosis.si(),
    )()
    return True


@shared_task
def easy_task():
    '''Удаляет неактуальные объявления + пересчитывает таможенные сборы и ру цену (раз в час)у легковых машин'''
    chain(
        delete_not_avaliable_cars.si(),
        delete_not_avaliable_trucks.si(),
        count_duties_and_ru_price.si(),
    )()
    return True


@shared_task
def main_task_truck():
    '''Полностью добавляет новые траки со всей подробной инфой в бд (раз в 3 часа)'''
    chain(
        get_raw_truck_info.si(),
        get_full_truck_info.si(),
        delete_fake_trucks.si(),
        get_truck_diagnosis.si(),
    )()
    return True


@shared_task
def easy_task_truck():
    '''Удаляет неактуальные объявления (раз в час) у траков'''
    chain(
        delete_not_avaliable_trucks.si(),
    )()
    return True