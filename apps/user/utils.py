import random, string
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.core.files.base import ContentFile


def generate_default_avatar(name, size=(200, 200), font_size=100):
    # Tasodifiy rang yaratish
    colors = [(255, 87, 34), (63, 81, 181), (76, 175, 80), (255, 193, 7)]
    background_color = random.choice(colors)
    text_color = (255, 255, 255)

    # Harfni olish
    initial = name[0].upper() if name else "A"

    # Rasm yaratish
    image = Image.new('RGB', size, background_color)
    draw = ImageDraw.Draw(image)

    # Yangi shriftni yuklash (siz o'z shrift faylingizni ko'rsatishingiz mumkin)
    try:
        font = ImageFont.truetype("arial.ttf", font_size)  # Tizimingizdagi shriftni ko'rsatish
    except IOError:
        font = ImageFont.load_default()

    # Matn o'lchamini olish
    text_bbox = draw.textbbox((0, 0), initial, font=font)  # Matnning cheklovlari
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    # Matnni markazlash
    text_position = ((size[0] - text_width) / 2, (size[1] - text_height) / 2)

    # Rasmga harfni chizish
    draw.text(text_position, initial, font=font, fill=text_color)

    # Rasmni saqlash
    buffer = BytesIO()
    image.save(buffer, format="PNG")
    return ContentFile(buffer.getvalue(), "default_avatar.png")



def generate_sms_code(length=6):
    sms_code = ''.join(random.choices(string.digits, k = length))
    return sms_code