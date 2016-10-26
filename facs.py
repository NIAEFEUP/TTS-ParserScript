from lxml import html
import requests

page = requests.get('https://sigarra.up.pt/up/pt/web_base.gera_pagina?p_pagina=escolas')
tree = html.fromstring(page.content)

facs = tree.cssselect('#nav-third ul li')

faculdades = []
for li in facs:
    faculdades.append(li.find('a').get('href').split("/")[1])
    print(li.find('a').get('href') + ': --> ' + li.text_content())
    continue
print(faculdades)


