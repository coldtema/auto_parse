# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import A4
# from reportlab.lib.colors import Color
# from reportlab.lib.utils import ImageReader
# from reportlab.pdfbase import pdfmetrics
# from reportlab.pdfbase.ttfonts import TTFont
# import requests
# from io import BytesIO


# BACKGROUND_IMAGE = "parser/static/images/step1.png"
# BACKGROUND_IMAGE2 = "parser/static/images/step2.png"
# BACKGROUND_IMAGE3 = "parser/static/images/step3.png"

# def generate_pdf(data, buffer):
#     print(data)
#     c = canvas.Canvas(buffer, pagesize=A4)
#     pdfmetrics.registerFont(TTFont("TTNormsPro-Bold", "parser/static/fonts/TTNormsPro-Bold.ttf"))
#     pdfmetrics.registerFont(TTFont("DAMN", "parser/static/fonts/DAMN.ttf"))
#     pdfmetrics.registerFont(TTFont("NotoEmoji", "parser/static/fonts/NotoEmoji.ttf"))

#     # # === СТРАНИЦА 1: АНКЕТА ===
#     # c.setFillColor(Color(0, 0, 0, 1))
#     # c.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)

#     # c.setFillColor(Color(1, 0.84, 0, 1))  # золото
#     # c.setFont("DAMN", 12)
#     # c.drawString(50, 800, "ШАГ 1. ЗНАКОМСТВО")

#     # c.setFillColor(Color(1, 1, 1, 1))
#     # c.setFont("DAMN", 12)

#     # y = 760
#     # for field, value in data.items():
#     #     c.drawString(50, y, f"{field.upper()}: {value if value else '-'}")
#     #     y -= 22

#     # c.showPage()

#     # === СТРАНИЦА 2: ОТЧЁТ ===
#     width, height = A4
#     c.drawImage(BACKGROUND_IMAGE, 0, 0, width=width, height=height)
#     # draw_grid(c)
#     # c.setFillColor(Color(0, 0, 0, 1))
#     # c.rect(0, 0, A4[0], A4[1], stroke=0, fill=1)

#     # img = make_gradient_text("HELLO", "parser/static/fonts/DAMN.ttf", 80)
#     # img_path = "parser/static/images/tmp.png"
#     # img.save(img_path)

#     # c.drawImage(img_path, 100, 500, mask='auto')

#     c.setFillColorRGB(1, 0, 0)
#     c.setFont("TTNormsPro-Bold", 35)
#     c.drawString(20, 780, f"СТОИМОСТЬ АВТО")
#     c.setFont("TTNormsPro-Bold", 20)
#     c.setFillColorRGB(1, 1, 1)
#     c.drawString(20, 740, f"{data['full_name']}")

#     # блок стоимости (заглушки)
#     # c.setFillColor(Color(1, 1, 1, 1))
#     c.setFont("TTNormsPro-Bold", 25)


#     asia_services = count_asia_fee(data)
#     final_price = count_final_price(data, asia_services)
#     price_items = [
#         ("Стоимость автомобиля в Корее: ", f'{comma_price(data['ru_price'])} руб.'),
#         ("Доставка Корея — Владивосток: ", f'{comma_price(str(round(int(data['delivery_cost']) * float(data['rate']))))} руб.'),
#         ("Услуги Asia Alliance: ", f'{comma_price(asia_services)} руб.'),
#         ("Услуги дилера: ", f'{comma_price(data['dealer_services'])} руб.'),
#         ("Оплата по инвойсу: ", f'{comma_price(data['korea_invoice'])} руб.'),
#         ("Таможня: ", f'{comma_price(data['customs_duty'])} руб.'),
#         ("Утилизационный сбор: ", f'{comma_price(data['recycling_fee'])} руб.'),
#         ("Брокер / СВХ / Лаборатория: ", f'{comma_price(data['broker_cost'])} руб.'),
#         ("Общая стоимость: ", f'{comma_price(final_price)} руб.'),
#     ]

#     c.drawString(350, 653, f"{price_items[0][1]}")

#     c.drawString(340, 600, f"{price_items[1][1]}")

#     c.drawString(241, 543, f"{price_items[2][1]}")

#     c.drawString(185, 487, f"{price_items[3][1]}")

#     c.drawString(235, 427, f"{price_items[4][1]}")

#     c.drawString(135, 303, f"{price_items[5][1]}")

#     c.drawString(270, 244, f"{price_items[6][1]}")

#     c.drawString(300, 186, f"{price_items[7][1]}")

#     c.drawString(220, 127, f"{price_items[8][1]}")

#     photo_url = data["photo"]

#     response = requests.get(photo_url)
#     img_data = BytesIO(response.content)

#     # координаты и размер фото (можно подстроить)
#     x = 0
#     y = 0
#     img_width = 150
#     img_height = 100

#     img_reader = ImageReader(img_data)

#     c.drawImage(img_reader, x, y, width=img_width, height=img_height, preserveAspectRatio=True, mask='auto')


#     photo_url = data["photo2"]

#     response = requests.get(photo_url)
#     img_data = BytesIO(response.content)

#     # координаты и размер фото (можно подстроить)
#     x = 150
#     y = 0
#     img_width = 150
#     img_height = 100

#     img_reader = ImageReader(img_data)

#     c.drawImage(img_reader, x, y, width=img_width, height=img_height, preserveAspectRatio=True, mask='auto')


#     photo_url = data["photo3"]

#     response = requests.get(photo_url)
#     img_data = BytesIO(response.content)

#     # координаты и размер фото (можно подстроить)
#     x = 300
#     y = 0
#     img_width = 150
#     img_height = 100

#     img_reader = ImageReader(img_data)

#     c.drawImage(img_reader, x, y, width=img_width, height=img_height, preserveAspectRatio=True, mask='auto')


#     photo_url = data["photo4"]

#     response = requests.get(photo_url)
#     img_data = BytesIO(response.content)

#     # координаты и размер фото (можно подстроить)
#     x = 450
#     y = 0
#     img_width = 150
#     img_height = 100

#     img_reader = ImageReader(img_data)

#     c.drawImage(img_reader, x, y, width=img_width, height=img_height, preserveAspectRatio=True, mask='auto')
    


#     # === СТРАНИЦА 2: КОПЛЕКТАЦИЯ ===
#     c.showPage()
#     width, height = A4
#     c.drawImage(BACKGROUND_IMAGE2, 0, 0, width=width, height=height)

#     # draw_grid(c)

#     c.setFillColorRGB(1, 1, 1)
#     c.setFont("NotoEmoji", 11)


#     #COMPLECTATION_DICT_PAGE1.keys()
#     for option in data['options']:
#         if option in COMPLECTATION_DICT_PAGE1.keys():
#             coords = COMPLECTATION_DICT_PAGE1[option]
#             c.drawString(coords[0], coords[1], "✔")
    


#     # === СТРАНИЦА 3: КОПЛЕКТАЦИЯ ===
#     c.showPage()
#     width, height = A4
#     c.drawImage(BACKGROUND_IMAGE3, 0, 0, width=width, height=height)

#     # draw_grid(c)

#     c.setFillColorRGB(1, 1, 1)
#     c.setFont("NotoEmoji", 11)


#     #COMPLECTATION_DICT_PAGE2.keys()
#     for option in data['options']:
#         if option in COMPLECTATION_DICT_PAGE2.keys():
#             coords = COMPLECTATION_DICT_PAGE2[option]
#             c.drawString(coords[0], coords[1], "✔")
    
#     c.save()



# def count_asia_fee(data):
#     return str(round(int(data['asia_services']) / 100 * int(data['ru_price'])))


# def count_final_price(data, asia_fee):
#     delivery_cost_rub = round(int(data['delivery_cost']) * float(data['rate']))
#     ru_price_in_korea = int(data['ru_price'])
#     dealer_services = int(data['dealer_services'])
#     customs_duty = int(data['customs_duty'])
#     recycling_fee = int(data['recycling_fee'])
#     broker_cost = int(data['broker_cost'])
#     final_price = ru_price_in_korea + delivery_cost_rub + int(asia_fee) + dealer_services + customs_duty + recycling_fee + broker_cost
    
#     return str(final_price)


# def comma_price(price):
#     price = str(price)
#     price = list(price)
#     counter = 0
#     new_price = []
#     while len(price) != 0:
#         new_price.insert(0, price.pop())
#         counter+=1
#         if counter % 3 == 0 and len(price) != 0:
#             new_price.insert(0, ',')
#     return ''.join(new_price)



# def draw_grid(c):
#     c.setFont("Helvetica", 6)
#     c.setFillColorRGB(1, 0, 0)

#     # вертикальные линии
#     for x in range(0, 600, 20):
#         c.drawString(x + 2, 2, str(x))
#         c.line(x, 0, x, 842)

#     # горизонтальные линии
#     for y in range(0, 900, 20):
#         c.drawString(2, y + 2, str(y))
#         c.line(0, y, 595, y)



# from PIL import Image, ImageDraw, ImageFont

# def make_gradient_text(text, font_path, font_size):
#     W, H = 800, 200
#     img = Image.new("RGBA", (W, H))
#     draw = ImageDraw.Draw(img)

#     # градиент
#     for y in range(H):
#         r = int(255 * (y / H))
#         g = 0
#         b = 255 - r
#         draw.line([(0, y), (W, y)], fill=(r, g, b, 255))

#     # текст с маской
#     mask = Image.new("L", (W, H), 0)
#     mdraw = ImageDraw.Draw(mask)
#     font = ImageFont.truetype(font_path, font_size)
#     mdraw.text((20, 50), text, font=font, fill=255)

#     img.putalpha(mask)
#     return img



# COMPLECTATION_DICT_PAGE1 = {
#     "006": (16, 683),
#     "008": (16, 653),
#     "017": (16, 621),
#     "029": (16, 591),
#     "031": (16, 561),
#     "062": (16, 530),
#     "075": (16, 499),
#     "082": (16, 468),
#     "084": (16, 432),
#     "007": (327, 683),
#     "010": (327, 650),
#     "024": (327, 613),
#     "030": (327, 562),
#     "074": (328, 525),
#     "059": (328, 495),
#     "080": (328, 463),
#     "083": (328, 427),
#     "001": (16.5, 314),
#     "019": (16.5, 274),
#     "026": (16.5, 227),
#     "032": (16.5, 190),
#     "055": (16.5, 151),
#     "058": (16.5, 112),
#     "086": (16.5, 78),
#     "088": (16.5, 30),
#     "002": (327, 314),
#     "020": (327, 265),
#     "027": (327, 222.5),
#     "033": (327, 184.5),
#     "056": (328, 139),
#     "085": (328, 93),
#     "087": (328, 61),
#     "083": (328, 26),
# }


# COMPLECTATION_DICT_PAGE2 = {
#     "003": (16, 690),
#     "005": (16, 660),
#     "023": (16, 628),
#     "057": (16, 598),
#     "071": (16, 568),
#     "096": (16, 537.5),
#     "092": (16, 502),
#     "094": (16, 457),
#     "068": (16, 413),
#     "004": (327, 691),
#     "015": (327, 657),
#     "054": (327, 620),
#     "079": (327, 583.5),
#     "072": (328, 546.5),
#     "081": (328, 516.5),
#     "095": (328, 484.5),
#     "093": (328, 448.5),
#     "097": (328, 408.5),
#     "014": (16.5, 314),
#     "022": (16.5, 274),
#     "021": (16.5, 227),
#     "051": (16.5, 190),
#     "063": (16.5, 151),
#     "090": (16.5, 112),
#     "035": (327, 314),
#     "034": (327, 265),
#     "078": (327, 228.5),
#     "077": (327, 193.5),
#     "089": (328, 149),
#     "091": (328, 111),
# }

# #список из названия, линии и цены
# field_slot_dict = {
#     'slot1': [(0, 0)],
#     'slot2': ()
# }


from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, Image, PageBreak
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
import requests
from reportlab.lib.enums import TA_RIGHT



def register_fonts():
    pdfmetrics.registerFont(
        TTFont("TTNormsPro-Medium", "parser/static/fonts/TTNormsPro-Medium.ttf")
    )
    pdfmetrics.registerFont(
        TTFont("TTNormsPro-Bold", "parser/static/fonts/TTNormsPro-Bold.ttf")
    )
    pdfmetrics.registerFont(
        TTFont("TTNormsPro-Italic", "parser/static/fonts/TTNormsPro-Italic.ttf")
    )
    pdfmetrics.registerFont(
        TTFont("DAMN", "parser/static/fonts/DAMN.ttf")
    )
    pdfmetrics.registerFont(
        TTFont("NotoEmoji", "parser/static/fonts/NotoEmoji.ttf")
    )

BACKGROUND_IMAGE = "parser/static/images/asia_blank_page.png"

BACKGROUND_IMAGE2 = "parser/static/images/step2.png"

BACKGROUND_IMAGE3 = "parser/static/images/step3.png"

TITLE_STYLE = ParagraphStyle(
    "TitleStyle",
    fontName="TTNormsPro-Bold",
    fontSize=28,
    textColor=colors.red,
    spaceAfter=6,
)

SUBTITLE_STYLE = ParagraphStyle(
    "SubtitleStyle",
    fontName="TTNormsPro-Bold",
    fontSize=18,
    textColor=colors.white,
    spaceAfter=12,
)

SUBTITLE_TABLE_STYLE = ParagraphStyle(
    "SubtitleStyle",
    fontName="TTNormsPro-Italic",
    fontSize=18,
    textColor=colors.black,
    spaceAfter=12,
)

RATE_STYLE = ParagraphStyle(
    "RateStyle",
    fontName="TTNormsPro-Italic",
    alignment=TA_RIGHT,
    textColor=colors.white,
    spaceBefore=10,
    spaceAfter=10,
)

TEXT_STYLE = ParagraphStyle(
    "TextStyle",
    fontName="TTNormsPro-Medium",
    fontSize=20,
    textColor=colors.white,
)


def draw_background(canvas, doc):
    width, height = A4
    canvas.drawImage(
        BACKGROUND_IMAGE,
        0,
        0,
        width=width,
        height=height,
        mask='auto'
    )

def draw_footer_photos(canvas, doc, photo_urls):
    page_width, page_height = A4
    img_width = 45*mm
    img_height = 30*mm
    spacing = 5*mm  # расстояние между картинками
    start_x = (page_width - (img_width*4 + spacing*3)) / 2  # центрируем ряд
    y = 5*mm  # отступ от низа страницы

    for i, url in enumerate(photo_urls):
        try:
            response = requests.get(url)
            img_data = BytesIO(response.content)
            img_reader = ImageReader(img_data)
            x = start_x + i*(img_width + spacing)
            canvas.drawImage(img_reader, x, y, width=img_width, height=img_height,
                                preserveAspectRatio=True, mask='auto')
        except Exception as e:
            print(f"Ошибка при загрузке фото {url}: {e}")


def generate_pdf(data):

    car_name = data['full_name']
    rates = data['rates']
    upfront_rows = data['upfront_rows']
    delivery_options = data['delivery_options']
    customs_rows = data['customs_rows']
    total = data['total']

    buffer = BytesIO()

    register_fonts()

    def format_money(value, suffix):
        return f"{value:,.0f}".replace(",", " ") + f" {suffix}"

    def price_table(title, rows):
        data = [[
            Paragraph(title, SUBTITLE_TABLE_STYLE),
            Paragraph("₽", SUBTITLE_TABLE_STYLE),
            Paragraph("$", SUBTITLE_TABLE_STYLE),
        ]]

        for row in rows:
            data.append([
                Paragraph(row["label"], TEXT_STYLE),
                Paragraph(format_money(row["rub"], "₽"), SUBTITLE_STYLE),
                Paragraph(format_money(row["usd"], "$"), SUBTITLE_STYLE),
            ])

        table = Table(data, colWidths=[100*mm, 50*mm, 50*mm])
        table.setStyle(TableStyle([
            ("ALIGN", (0, 0), (-1, 0), "CENTER"),
            ("VALIGN", (0, 0), (-1, 0), "MIDDLE"),
            ("BACKGROUND", (0, 0), (-5, 0), colors.whitesmoke),
            ("TOPPADDING", (0, 0), (-1, 0), 8),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 13),

            ("TOPPADDING", (0, 1), (-1, -1), 13),
            ("BOTTOMPADDING", (0, 1), (-1, -1), 13),
            ("LEFTPADDING", (0, 0), (-1, -1), 4),
            ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ]))
        return table
    

    def rate_block(title, usd_rate):
        text = f"{title}: 1 {usd_rate}"
        return Paragraph(text, RATE_STYLE)


    doc = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        rightMargin=5*mm,
        leftMargin=5*mm,
        topMargin=5*mm,
        bottomMargin=0*mm,
    )

    elements = []

    elements.append(Paragraph("СТОИМОСТЬ АВТО", TITLE_STYLE))
    elements.append(Spacer(1, 20))
    elements.append(Paragraph(car_name, SUBTITLE_STYLE))
    elements.append(Spacer(1, 8))
    elements.append(Paragraph(data['mileage'], SUBTITLE_STYLE))
    elements.append(Spacer(1, 10))

    elements.append(rate_block("КУРС", f"$ = {rates['USD_RUB']} ₽"))

    elements.append(Spacer(1, 12))
    elements.append(price_table("ОПЛАТА СРАЗУ", upfront_rows+delivery_options))
    elements.append(Spacer(1, 30))

    elements.append(price_table("ОПЛАТА ПРИ ТАМОЖНЕ", customs_rows+total))
    elements.append(Spacer(1, 20))

    photo_urls = [data["photo1"], data["photo2"], data["photo3"], data["photo4"]]

    # подготовка Image объектов
    images = []
    img_width = 52*mm  # ширина каждой картинки
    img_height = 30*mm  # высота каждой картинки

    for url in photo_urls:
        response = requests.get(url)
        img_data = BytesIO(response.content)
        img = Image(img_data, width=img_width, height=img_height)
        images.append(img)

    # можно сделать row через Table, чтобы ровно выстроились
    # table = Table([images], colWidths=[img_width]*4)
    # table.setStyle(TableStyle([
    #     ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    #     ("ALIGN", (0,0), (-1,-1), "CENTER"),
    # ]))

    # # добавляем в конец элементов
    # elements.append(Spacer(1, 25))
    # elements.append(table)

    doc.photo1 = data["photo1"]
    doc.photo2 = data["photo2"]
    doc.photo3 = data["photo3"]
    doc.photo4 = data["photo4"]
    doc.options = data["options"]

    elements.append(PageBreak())
    elements.append(Spacer(1, 1))

    elements.append(PageBreak())
    elements.append(Spacer(1, 1))


    doc.build(
        elements,
        onFirstPage=draw_pages,
        onLaterPages=draw_pages,
    )
    buffer.seek(0)
    return buffer


def draw_pages(canvas, doc):
    if doc.page == 1:
        draw_page_1(canvas, doc)

    elif doc.page == 2:
        draw_complectation(
            canvas,
            doc,
            BACKGROUND_IMAGE2,
            COMPLECTATION_DICT_PAGE1
        )

    elif doc.page == 3:
        draw_complectation(
            canvas,
            doc,
            BACKGROUND_IMAGE3,
            COMPLECTATION_DICT_PAGE2
        )




def draw_page_1(canvas, doc):
    width, height = A4
    canvas.drawImage(
        BACKGROUND_IMAGE,
        0,
        0,
        width=width,
        height=height,
        mask='auto'
    )

    photo_urls = [ doc.photo1, doc.photo2, doc.photo3, doc.photo4, ]

    canvas.saveState()

    PAGE_WIDTH, PAGE_HEIGHT = A4

    img_width = PAGE_WIDTH / 4
    img_height = 30 * mm

    y = 0  # прям от низа листа

    for i, img in enumerate(photo_urls):
        x = i * img_width
        canvas.drawImage(
            img,
            x,
            y,
            width=img_width,
            height=img_height,
            preserveAspectRatio=False,  # ВАЖНО
            mask="auto"
        )

    canvas.restoreState()




def draw_complectation(canvas, doc, background_image, comp_dict):
    canvas.saveState()

    width, height = A4

    # фон
    canvas.drawImage(
        background_image,
        0,
        0,
        width=width,
        height=height,
        preserveAspectRatio=False,
        mask="auto"
    )

    # галочки
    canvas.setFillColorRGB(1, 1, 1)
    canvas.setFont("NotoEmoji", 11)

    for option in doc.options:
        if option in comp_dict:
            x, y = comp_dict[option]
            canvas.drawString(x, y, "✔")

    canvas.restoreState()




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