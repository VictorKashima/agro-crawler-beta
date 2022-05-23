#CRAWLER DE NOTÍCIAS DO CAFÉ

from requests import get
from bs4 import BeautifulSoup as bs
import html5lib
from DataCerta import data

def cafenew():
    global ltxt, lst
    he = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.32'}

    urlu = get('https://www.agrolink.com.br/noticias/cultura/cafe/lista', headers=he)
    pagep = bs(urlu.content, 'html5lib')

    ltxt = []
    ldata = []
    ltitle = []
    lstitle = []
    llink = []
    lst = 0
    pref = 'https://www.agrolink.com.br'

    for i in range(6, 29, 2):
        d = pagep.find_all('small')[i]
        a = d.text[:5]
        d = a[:2]
        m = a[3:5]
        da = int(d)
        datanew = (f'{da}/{m}')
        ldata.append(datanew)
        if data == datanew:
            lst = lst + 1
                
    for t in range(12):
        ti = pagep.find_all('h3', attrs={'class':'mb-2'})[t]
        tit = ti.text
        ltitle.append(tit)

    for l in range(12):
        li = pagep.find_all('h3', attrs={'class':'mb-2'})[l]
        for lin in li:
            if 'href' in lin.attrs:
                link = (str(lin.attrs['href']))
                llink.append(f'{pref}{link}')

    for s in range(12):
        st = pagep.find_all('p', attrs={'class':'mb-0'})[s]
        sti = st.text
        stit = sti.replace('\n','')
        lstitle.append(stit)

    
    if data == ldata[0]:        
        for n in range(lst):
            ltxt.append(f"↧Notícias de hoje sobre café:↧\n{ltitle[n]}\n{lstitle[n]}\n{llink[n]}\nData: {ldata[n]}")

    else:
        lst = 1
        ltxt.append(f"↧Última notícia de café:↧\n{ltitle[0]}\n{lstitle[0]}\n{llink[0]}\nData: {ldata[0]}""")

    return ltxt