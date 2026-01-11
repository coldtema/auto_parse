from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import Color
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import requests
from io import BytesIO


BACKGROUND_IMAGE = "parser/static/images/step1.png"
BACKGROUND_IMAGE2 = "parser/static/images/step2.png"
BACKGROUND_IMAGE3 = "parser/static/images/step3.png"

def generate_pdf(data, buffer):
    print(data)
    c = canvas.Canvas(buffer, pagesize=A4)
    pdfmetrics.registerFont(TTFont("TTNormsPro-Bold", "parser/static/fonts/TTNormsPro-Bold.ttf"))
    pdfmetrics.registerFont(TTFont("DAMN", "parser/static/fonts/DAMN.ttf"))
    pdfmetrics.registerFont(TTFont("NotoEmoji", "parser/static/fonts/NotoEmoji.ttf"))

    # # === СТРАНИЦА 1: АНКЕТА ===
    # c.setFillColor(Color(0, 0, 0, 1))
    # c.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)

    # c.setFillColor(Color(1, 0.84, 0, 1))  # золото
    # c.setFont("DAMN", 12)
    # c.drawString(50, 800, "ШАГ 1. ЗНАКОМСТВО")

    # c.setFillColor(Color(1, 1, 1, 1))
    # c.setFont("DAMN", 12)

    # y = 760
    # for field, value in data.items():
    #     c.drawString(50, y, f"{field.upper()}: {value if value else '-'}")
    #     y -= 22

    # c.showPage()

    # === СТРАНИЦА 2: ОТЧЁТ ===
    width, height = A4
    c.drawImage(BACKGROUND_IMAGE, 0, 0, width=width, height=height)
    # draw_grid(c)
    # c.setFillColor(Color(0, 0, 0, 1))
    # c.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)

    # img = make_gradient_text("HELLO", "parser/static/fonts/DAMN.ttf", 80)
    # img_path = "parser/static/images/tmp.png"
    # img.save(img_path)

    # c.drawImage(img_path, 100, 500, mask='auto')

    c.setFillColorRGB(1, 0, 0)
    c.setFont("TTNormsPro-Bold", 35)
    c.drawString(20, 780, f"СТОИМОСТЬ АВТО")
    c.setFont("TTNormsPro-Bold", 20)
    c.setFillColorRGB(1, 1, 1)
    c.drawString(20, 740, f"{data['full_name']}")

    # блок стоимости (заглушки)
    # c.setFillColor(Color(1, 1, 1, 1))
    c.setFont("TTNormsPro-Bold", 25)


    asia_services = count_asia_fee(data)
    final_price = count_final_price(data, asia_services)
    price_items = [
        ("Стоимость автомобиля в Корее: ", f'{comma_price(data['ru_price'])} руб.'),
        ("Доставка Корея — Владивосток: ", f'{comma_price(str(round(int(data['delivery_cost']) * float(data['rate']))))} руб.'),
        ("Услуги Asia Alliance: ", f'{comma_price(asia_services)} руб.'),
        ("Услуги дилера: ", f'{comma_price(data['dealer_services'])} руб.'),
        ("Оплата по инвойсу: ", f'{comma_price(data['korea_invoice'])} руб.'),
        ("Таможня: ", f'{comma_price(data['customs_duty'])} руб.'),
        ("Утилизационный сбор: ", f'{comma_price(data['recycling_fee'])} руб.'),
        ("Брокер / СВХ / Лаборатория: ", f'{comma_price(data['broker_cost'])} руб.'),
        ("Общая стоимость: ", f'{comma_price(final_price)} руб.'),
    ]

    c.drawString(350, 653, f"{price_items[0][1]}")

    c.drawString(340, 600, f"{price_items[1][1]}")

    c.drawString(241, 543, f"{price_items[2][1]}")

    c.drawString(185, 487, f"{price_items[3][1]}")

    c.drawString(235, 427, f"{price_items[4][1]}")

    c.drawString(135, 303, f"{price_items[5][1]}")

    c.drawString(270, 244, f"{price_items[6][1]}")

    c.drawString(300, 186, f"{price_items[7][1]}")

    c.drawString(220, 127, f"{price_items[8][1]}")

    photo_url = data["photo"]

    response = requests.get(photo_url)
    img_data = BytesIO(response.content)

    # координаты и размер фото (можно подстроить)
    x = 0
    y = 0
    img_width = 150
    img_height = 100

    img_reader = ImageReader(img_data)

    c.drawImage(img_reader, x, y, width=img_width, height=img_height, preserveAspectRatio=True, mask='auto')


    photo_url = data["photo2"]

    response = requests.get(photo_url)
    img_data = BytesIO(response.content)

    # координаты и размер фото (можно подстроить)
    x = 150
    y = 0
    img_width = 150
    img_height = 100

    img_reader = ImageReader(img_data)

    c.drawImage(img_reader, x, y, width=img_width, height=img_height, preserveAspectRatio=True, mask='auto')


    photo_url = data["photo3"]

    response = requests.get(photo_url)
    img_data = BytesIO(response.content)

    # координаты и размер фото (можно подстроить)
    x = 300
    y = 0
    img_width = 150
    img_height = 100

    img_reader = ImageReader(img_data)

    c.drawImage(img_reader, x, y, width=img_width, height=img_height, preserveAspectRatio=True, mask='auto')


    photo_url = data["photo4"]

    response = requests.get(photo_url)
    img_data = BytesIO(response.content)

    # координаты и размер фото (можно подстроить)
    x = 450
    y = 0
    img_width = 150
    img_height = 100

    img_reader = ImageReader(img_data)

    c.drawImage(img_reader, x, y, width=img_width, height=img_height, preserveAspectRatio=True, mask='auto')
    


    # === СТРАНИЦА 2: КОПЛЕКТАЦИЯ ===
    c.showPage()
    width, height = A4
    c.drawImage(BACKGROUND_IMAGE2, 0, 0, width=width, height=height)

    # draw_grid(c)

    c.setFillColorRGB(1, 1, 1)
    c.setFont("NotoEmoji", 11)


    #COMPLECTATION_DICT_PAGE1.keys()
    for option in data['options']:
        if option in COMPLECTATION_DICT_PAGE1.keys():
            coords = COMPLECTATION_DICT_PAGE1[option]
            c.drawString(coords[0], coords[1], "✔")
    


    # === СТРАНИЦА 3: КОПЛЕКТАЦИЯ ===
    c.showPage()
    width, height = A4
    c.drawImage(BACKGROUND_IMAGE3, 0, 0, width=width, height=height)

    # draw_grid(c)

    c.setFillColorRGB(1, 1, 1)
    c.setFont("NotoEmoji", 11)


    #COMPLECTATION_DICT_PAGE2.keys()
    for option in data['options']:
        if option in COMPLECTATION_DICT_PAGE2.keys():
            coords = COMPLECTATION_DICT_PAGE2[option]
            c.drawString(coords[0], coords[1], "✔")
    
    c.save()



def count_asia_fee(data):
    return str(round(int(data['asia_services']) / 100 * int(data['ru_price'])))


def count_final_price(data, asia_fee):
    delivery_cost_rub = round(int(data['delivery_cost']) * float(data['rate']))
    ru_price_in_korea = int(data['ru_price'])
    dealer_services = int(data['dealer_services'])
    customs_duty = int(data['customs_duty'])
    recycling_fee = int(data['recycling_fee'])
    broker_cost = int(data['broker_cost'])
    final_price = ru_price_in_korea + delivery_cost_rub + int(asia_fee) + dealer_services + customs_duty + recycling_fee + broker_cost
    
    return str(final_price)


def comma_price(price):
    price = str(price)
    price = list(price)
    counter = 0
    new_price = []
    while len(price) != 0:
        new_price.insert(0, price.pop())
        counter+=1
        if counter % 3 == 0 and len(price) != 0:
            new_price.insert(0, ',')
    return ''.join(new_price)



def draw_grid(c):
    c.setFont("Helvetica", 6)
    c.setFillColorRGB(1, 0, 0)

    # вертикальные линии
    for x in range(0, 600, 20):
        c.drawString(x + 2, 2, str(x))
        c.line(x, 0, x, 842)

    # горизонтальные линии
    for y in range(0, 900, 20):
        c.drawString(2, y + 2, str(y))
        c.line(0, y, 595, y)



from PIL import Image, ImageDraw, ImageFont

def make_gradient_text(text, font_path, font_size):
    W, H = 800, 200
    img = Image.new("RGBA", (W, H))
    draw = ImageDraw.Draw(img)

    # градиент
    for y in range(H):
        r = int(255 * (y / H))
        g = 0
        b = 255 - r
        draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

    # текст с маской
    mask = Image.new("L", (W, H), 0)
    mdraw = ImageDraw.Draw(mask)
    font = ImageFont.truetype(font_path, font_size)
    mdraw.text((20, 50), text, font=font, fill=255)

    img.putalpha(mask)
    return img



COMPLECTATION_DICT_PAGE1 = {
    "006": (16, 683),
    "008": (16, 653),
    "017": (16, 621),
    "029": (16, 591),
    "031": (16, 561),
    "062": (16, 530),
    "075": (16, 499),
    "082": (16, 468),
    "084": (16, 432),
    "007": (327, 683),
    "010": (327, 650),
    "024": (327, 613),
    "030": (327, 562),
    "074": (328, 525),
    "059": (328, 495),
    "080": (328, 463),
    "083": (328, 427),
    "001": (16.5, 314),
    "019": (16.5, 274),
    "026": (16.5, 227),
    "032": (16.5, 190),
    "055": (16.5, 151),
    "058": (16.5, 112),
    "086": (16.5, 78),
    "088": (16.5, 30),
    "002": (327, 314),
    "020": (327, 265),
    "027": (327, 222.5),
    "033": (327, 184.5),
    "056": (328, 139),
    "085": (328, 93),
    "087": (328, 61),
    "083": (328, 26),
}


COMPLECTATION_DICT_PAGE2 = {
    "003": (16, 690),
    "005": (16, 660),
    "023": (16, 628),
    "057": (16, 598),
    "071": (16, 568),
    "096": (16, 537.5),
    "092": (16, 502),
    "094": (16, 457),
    "068": (16, 413),
    "004": (327, 691),
    "015": (327, 657),
    "054": (327, 620),
    "079": (327, 583.5),
    "072": (328, 546.5),
    "081": (328, 516.5),
    "095": (328, 484.5),
    "093": (328, 448.5),
    "097": (328, 408.5),
    "014": (16.5, 314),
    "022": (16.5, 274),
    "021": (16.5, 227),
    "051": (16.5, 190),
    "063": (16.5, 151),
    "090": (16.5, 112),
    "035": (327, 314),
    "034": (327, 265),
    "078": (327, 228.5),
    "077": (327, 193.5),
    "089": (328, 149),
    "091": (328, 111),
}