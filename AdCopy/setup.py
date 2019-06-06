# ====================================================================
# AdCopy.py v1.0.0
# https://github.com/joaofelipegom/Python/tree/master/AdCopy
# ====================================================================
# Documentation
# You may obtain a copy of the Documentation at
# https://github.com/joaofelipegom/Python/blob/master/AdCopy/README.md
# ====================================================================

import requests
from bs4 import BeautifulSoup
from xlsxwriter import Workbook

arquivo = open('uniform-resource-locator.txt','r')
f_excel = Workbook('planilha-anuncios.xlsx')
sheet = f_excel.add_worksheet()
row = 1

sheet.write(0,0, 'URL')
sheet.write(0,1, 'Título')
sheet.write(0,2, 'Preço')
sheet.write(0,3, 'Categoria')
sheet.write(0,4, 'Descrição')
sheet.write(0,5, 'Imagem 1')
sheet.write(0,6, 'Imagem 2')
sheet.write(0,7, 'Imagem 3')
sheet.write(0,8, 'Imagem 4')
sheet.write(0,9, 'Imagem 5')
sheet.write(0,10, 'Imagem 6')
sheet.write(0,11, 'Imagem 7')
sheet.write(0,12, 'Imagem 8')
sheet.write(0,13, 'Imagem 9')
sheet.write(0,14, 'Imagem 10')
sheet.write(0,15, 'Imagem 11')
sheet.write(0,16, 'Imagem 12')
sheet.write(0,17, 'Modalidade')

def splitimg(image):
    i = 0
    global list
    list = ['','','','','','','','','','','','']

    for x in image:
        imagem1 = image[i]
        imagem1 = imagem1[7:]
        imagem1 = imagem1.split('",')
        image1 = str(imagem1[0])

        list[i] = image1
        i = i + 1

def AdCopy(x):
    r = requests.get(x)
    soup = BeautifulSoup(r.text, 'lxml')

    titulo = soup.title
    titulo = str(titulo)
    titulo = titulo.split(" - R$", 1)
    price = titulo[1]
    title = titulo[0]
    title = title[7:]
    sheet.write(row,1, title)

    price = price[1:]
    price = price[:-24]
    sheet.write(row,2, price)

    categ = soup.find('input', {'name': 'categoryId'}).get('value')
    sheet.write(row,3, categ)

    descr = soup.find_all('div', class_='item-description__text')
    descr = str(descr)
    descr = descr.replace("<br/>", "\n")
    descr = descr[41:]
    descr = descr[:-12]
    sheet.write(row,4, descr)

    image = soup.find('div', {'class': 'gallery-content item-gallery__wrapper'}).get('data-full-images')
    image = str(image)
    image = image[2:]
    image = image[:-1]
    image = image.split('},{')

    splitimg(image)

    sheet.write(row,5, list[0])
    sheet.write(row,6, list[1])
    sheet.write(row,7, list[2])
    sheet.write(row,8, list[3])
    sheet.write(row,9, list[4])
    sheet.write(row,10, list[5])
    sheet.write(row,11, list[6])
    sheet.write(row,12, list[7])
    sheet.write(row,13, list[8])
    sheet.write(row,14, list[9])
    sheet.write(row,15, list[10])
    sheet.write(row,16, list[11])

    modes = soup.find('span', {'class': 'free-shipping'}).get('data-state')
    if modes == 'invisible':
        modes = 'Classico'
    else:
        modes = 'Premium'
    sheet.write(row,17, modes)

i = 0
lines = []

for linha in arquivo:
    linha = linha.rstrip()
    lines.append(linha)

for aux in lines:
    sheet.write(row,0, lines[i])
    AdCopy(lines[i])
    i += 1
    row += 1

print(row-1, "Produtos copiados com sucesso!")
arquivo.close()
f_excel.close()
