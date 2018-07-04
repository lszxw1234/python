import random
import string

from PIL import Image,ImageDraw,ImageFont,ImageFilter



def make_verification_code():

    valid_str = string.ascii_letters + string.digits
    str = random.choice(valid_str)
    return str

def rndColor():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

def rndbgColor():
    return (random.randint(64, 255), random.randint(64, 255), random.randint(64, 255))

def add_to_pic():
    width = 60 * 4
    height = 60
    image = Image.new('RGB', (width, height), (255, 255, 255))
    font = ImageFont.truetype('arial.ttf', 36)
    draw = ImageDraw.Draw(image)
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=rndbgColor())
    for i in range(4):
        draw.text((i * 60 + 10, 10), make_verification_code(), font=font, fill=rndColor())
    image = image.filter(ImageFilter.BLUR)
    image.save('code.jpg', 'jpeg')

add_to_pic()
