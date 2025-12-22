from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import Color
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import requests
from io import BytesIO


BACKGROUND_IMAGE = "parser/static/images/step1.png"  # твоя картинка

def generate_pdf(data, buffer):
    print(data)
    c = canvas.Canvas(buffer, pagesize=A4)
    pdfmetrics.registerFont(TTFont("TTNormsPro-Bold", "parser/static/fonts/TTNormsPro-Bold.ttf"))

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

    c.drawString(350, 673, f"{price_items[0][1]}")

    c.drawString(340, 620, f"{price_items[1][1]}")

    c.drawString(241, 563, f"{price_items[2][1]}")

    c.drawString(185, 507, f"{price_items[3][1]}")

    c.drawString(235, 447, f"{price_items[4][1]}")

    c.drawString(135, 393, f"{price_items[5][1]}")

    c.drawString(270, 334, f"{price_items[6][1]}")

    c.drawString(300, 276, f"{price_items[7][1]}")

    c.drawString(220, 217, f"{price_items[8][1]}")

    photo_url = data["photo"]

    response = requests.get(photo_url)
    img_data = BytesIO(response.content)

    # координаты и размер фото (можно подстроить)
    x = 0
    y = 0
    img_width = 300
    img_height = 200

    img_reader = ImageReader(img_data)

    c.drawImage(img_reader, x, y, width=img_width, height=img_height, preserveAspectRatio=True, mask='auto')


    photo_url = data["photo2"]

    response = requests.get(photo_url)
    img_data = BytesIO(response.content)

    # координаты и размер фото (можно подстроить)
    x = 300
    y = 0
    img_width = 300
    img_height = 200

    img_reader = ImageReader(img_data)

    c.drawImage(img_reader, x, y, width=img_width, height=img_height, preserveAspectRatio=True, mask='auto')
    

    c.showPage()
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