from deep_translator import GoogleTranslator
from faker import Faker
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import time

start = time.time()

fake = Faker("fr_FR")

def createdico(nmbr):
    translated={}
    while len(translated) < nmbr:
        word = fake.word()
        entoes = GoogleTranslator(source='fr', target='es').translate(word) 
        entofr = word
        translated[entofr]=entoes
    return translated


def fakedico(nmbr):
    fakedico={}
    while len(fakedico) < nmbr:
        fakedico[fake.word()] = fake.word()
    return fakedico

for imagestogen in range(50):
    translated=fakedico(50)
    width = 1654 
    height = 2339

    #img  = Image.new( mode = "RGB", size = (width, height), color=(255,255,255) )

    x = 165.4
    y = -116.95
    counter= -1

    base_width= 1654
    img = Image.open('background.jpg')
    wpercent = (base_width / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    input_image = img.resize((base_width, hsize), Image.Resampling.LANCZOS)
    input_image2 = img.resize((base_width, hsize), Image.Resampling.LANCZOS)

    for key, value in translated.items():
        counter+=1
        draw = ImageDraw.Draw(input_image)
        text_position = (x, y)
        text = key
        text_color = (0, 0, 0)
        x+=330.8
        if counter % 5 == 0:
            y+=233.9
        if counter % 5 == 0:
            x=165.4

        font = ImageFont.truetype("arial.ttf", 40)
        _, _, w, h = draw.textbbox((0,0), text, font=font)
        n=0
        while w > 316:
            n+=1
            _, _, w, h = draw.textbbox((0,0), text, font=font)
            font = ImageFont.truetype("arial.ttf", 40-n)
        draw.text(((x*2-w)/2,(y*2-h)/2), text, fill=text_color, font=font)
        #draw.text(text_position, text, fill=text_color)

    x=1654-165.4
    y = -116.95
    counter = -1
    for key, value in translated.items():
        counter+=1
        draw = ImageDraw.Draw(input_image2)
        text_position = (x, y)
        text = value
        text_color = (0, 0, 0)
        x-=330.8
        if counter % 5 == 0:
            y+=233.9
        if counter % 5 == 0:
            x=1654-165.4

        font = ImageFont.truetype("arial.ttf", 40)
        _, _, w, h = draw.textbbox((0,0), text, font=font)
        n=0
        while w > 316:
            n+=1
            _, _, w, h = draw.textbbox((0,0), text, font=font)
            font = ImageFont.truetype("arial.ttf", 40-n)
        draw.text(((x*2-w)/2,(y*2-h)/2), text, fill=text_color, font=font)
        #draw.text(text_position, text, fill=text_color)

    images = [input_image2]
    input_image.save(str(imagestogen) + "frTOesFLASHCARDS.pdf", save_all=True, append_images=images)

end = time.time()
print(end - start)
print("done")