from requests import get
from bs4 import BeautifulSoup as bs
import html5lib
from DataCerta import data

def arroznew():

    h = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.23'}

    url = get('https://www.agrolink.com.br/noticias/cultura/arroz/lista', headers=h)
    page = bs(url.content, 'html5lib')

    ldata = []
    ltitle = []
    lstitle = []
    llink = []
    lst = 0
    pref = 'https://www.agrolink.com.br'

    for i in range(6, 29, 2):
        d = page.find_all('small')[i]
        a = d.text[:5]
        d = a[:2]
        m = a[3:5]
        da = int(d)
        datanew = (f'{da}/{m}')
        ldata.append(datanew)
        if data == datanew:
            lst = lst + 1
                
    for t in range(12):
        ti = page.find_all('h3', attrs={'class':'mb-2'})[t]
        tit = ti.text
        ltitle.append(tit)

    for l in range(12):
        li = page.find_all('h3', attrs={'class':'mb-2'})[l]
        for lin in li:
            if 'href' in lin.attrs:
                link = (str(lin.attrs['href']))
                llink.append(f'{pref}{link}')

    for s in range(12):
        st = page.find_all('p', attrs={'class':'mb-0'})[s]
        sti = st.text
        stit = sti.replace('\n','')
        lstitle.append(stit)

    if data == ldata[0]:        
        for n in range(lst):
            print(ltitle[n])
            print(lstitle[n])
            print(llink[n])
            print(f'Data:',ldata[n])
    else:
        print(f'Até o presente momento não foi possível encontrar nenhuma notícia sobre Arroz.\nPortanto a última notícia encontrada foi:')
        print(ltitle[0])
        print(lstitle[0])
        print(f'Link: {llink[0]}')
        print(f'Data: {ldata[0]}')