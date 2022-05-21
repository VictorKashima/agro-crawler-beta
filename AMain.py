from time import sleep

from NewArroz import arroznew
from NewCafe import cafenew
from NewSoja import sojanew

from PriceArroz import arrozprice
from PriceCafe import cafeprice
from PriceSoja import sojaprice

def linha():
    print('- '*30)


print('- - - - - - - - - - C O T A Ç Ã O - - - - - - - - - -')
arrozprice()
linha()
sleep(1)
cafeprice()
linha()
sleep(1)
sojaprice()
linha()

print('- - - - - - - - - - N O T Í C I A S - - - - - - - - - -')
arroznew()
linha()
sleep(1)
cafenew()
linha()
sleep(1)
sojanew()
linha()