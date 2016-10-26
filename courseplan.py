from lxml import html
import requests

fac = 'feup'
id = '742'
year= '2016'
url = 'https://sigarra.up.pt/'+ fac +'/pt/cur_geral.cur_planos_estudos_list?pv_curso_id='+ id +'&pv_ano_lectivo=' + year
page = requests.get(url)
tree = html.fromstring(page.content)
print url
pln = tree.cssselect('.dados .d .k a')
for link in pln:
    print(link.get('href'))
    coursePlan = 'https://sigarra.up.pt/' + fac + '/pt/' + link.get('href')
    continue

print(coursePlan)

