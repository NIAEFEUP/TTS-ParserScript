from lxml import html
import requests

fac = 'feup'
type = 'MI'
year= '2016'
url = 'https://sigarra.up.pt/' + fac + '/pt/cur_geral.cur_tipo_curso_view?pv_tipo_sigla='+type+'&pv_ano_lectivo=' + year
page = requests.get(url)
tree = html.fromstring(page.content)
print url
crs = tree.cssselect('#MI_a li')

courses = []
for li in crs:
    courses.append(li.find('a').get('href').split("=")[4])
    print(li.find('a').get('href') + ': --> ' + li.text_content())
    continue
print(courses)