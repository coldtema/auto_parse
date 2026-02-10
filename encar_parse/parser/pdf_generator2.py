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
    spaceBefore=0,
    spaceAfter=0,
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


def generate_pdf2(data):

    car_name = data['full_name']
    rates = data['rates']
    upfront_rows = data['upfront_rows']
    delivery_options = data['delivery_options']
    middle_rows = data['middle_rows']
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
    elements.append(price_table("ОПЛАТА СРАЗУ", upfront_rows))
    elements.append(Spacer(1, 20))

    elements.append(price_table("ОПЛАТА В БИШКЕК", middle_rows+delivery_options))
    elements.append(Spacer(1, 20))

    elements.append(price_table("ВЫЕЗД В МОСКВУ", customs_rows+total))
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