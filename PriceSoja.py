from requests import get
from bs4 import BeautifulSoup as bs
from DataCerta import data
import html5lib

def sojaprice():

    h = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.23'}

    url = get('https://www.cepea.esalq.usp.br/br/indicador/soja.aspx', headers=h)
    page = bs(url.content, 'html5lib')

    tudo = []

    for p in range(5):
        p = page.find_all('td')[p]
        pr = p.text
        pri = pr.replace(' ','')
        tudo.append(pri)

    pdata = tudo[0]
    pr = pdata[:2]
    prd = int(pr)
    prm = pdata[3:5]
    pdm = (f'{prd}/{prm}')

    preais = tudo[1]
    pvard = tudo[2]
    pvarm = tudo[3]
    pdol = tudo[4]

    if data == pdm:
        print(f'A cotação da saca de soja fechou hoje em:')
        print(f'Reais: R${preais}')
        print(f'Dólar: ${pdol}')
        print(f'Variação no dia: {pvard}')
        print(f'Variação no mês: {pvarm}')
    else:
        print('Ainda não foi atualizado as informações sobre a saca de soja')
        print('Últimas informações:')
        print(f'Data: {pdata}')
        print(f'Reais: R${preais}')
        print(f'Dólar: ${pdol}')
        print(f'Variação no dia: {pvard}')
        print(f'Variação no mês: {pvarm}')