#CAPTAR DATA EM TEMPO REAL
from requests import get
from bs4 import BeautifulSoup as bs
import html5lib

h = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36 OPR/86.0.4363.32'}

url = get('http://datadehoje.com', headers=h)
page = bs(url.content, 'html5lib')
d = page.find_all('p')[3]
da = d.text
dat = (da[-8:]).strip()
data = dat.replace('-', '/')[:5]