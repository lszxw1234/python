from PIL import Image, ImageDraw, ImageFont

def add_num(filepath):
    image = Image.open(filepath)
    w, h = image.size
    font = ImageFont.truetype('arial.ttf', size = 200)
    draw = ImageDraw.Draw(image)
    draw.text((4*w/5, h/5), '5', fill=(255, 10, 10), font=font)
    image.save('0.0.png', 'png')

add_num("IMG_20170221_0001.jpg")
# add_num("in.jpg")