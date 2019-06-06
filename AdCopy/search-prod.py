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

arquivo = open('insert-pages.txt','r')

i = 0
a = 0
lines = []
url = ''

for linha in arquivo:
    linha = linha.rstrip()
    lines.append(linha)

for aux in lines:
    r = requests.get(lines[i])
    soup = BeautifulSoup(r.text, 'lxml')

    page = soup.find_all('div', {'class': 'images-viewer'})
    for item in page:
        get_item = item["item-url"]
        url = url + get_item + "\n"
        a += 1
    i += 1

arq = open("uniform-resource-locator.txt", "w")
arq.write(url)

print(a, "produtos encontrados.")
arq.close()
arquivo.close()
