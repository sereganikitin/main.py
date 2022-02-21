import xml.etree.ElementTree as ET
import requests
from PIL import Image

tree = ET.parse('simvol-67.xml')
root = tree.getroot()

f = open('parsed.txt', 'w')

for ch in root:
    for child in ch:
        im_tag = str(child.tag)

        if 'image' in im_tag:
            url = child.text
            resp = requests.get(url, stream=True).raw
            try:
                im = Image.open(resp)
                width = im.size[0]
                height = im.size[1]
                if width <= 1000 or height <= 1000:
                    print(url, "Размер изображения маловат!: ", width, ' x ', height)
                    a=(url, "Размер изображения маловат!: ", width, ' x ', height)
                    f.write(str(a))

                else:
                    print(url, "Размер изображения в норме: ", width, ' x ', height)
                    b=(url, "Размер изображения в норме: ", width, ' x ', height)
                    f.write(str(b))

            except IOError:
                print(url, 'Изображение не найдено')
                c=(url, 'Изображение не найдено')
                f.write(str(c))

f.close()