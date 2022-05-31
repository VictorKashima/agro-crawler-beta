#EXECUTAR/TESTAR TODOS OS CRAWLERS!

from time import sleep

import NewArroz as NA
import NewCafe as NC
import NewSoja as NS

import PriceArroz as PA
import PriceCafe as PC
import PriceSoja as PS

def linha():
    print('- '*30)


print('- - - - - - - - - - C O T A Ç Ã O - - - - - - - - - -')
print(PA.arrozprice())
linha()
sleep(1)
print(PC.cafeprice())
linha()
sleep(1)
print(PS.sojaprice())
linha()

print('- - - - - - - - - - N O T Í C I A S - - - - - - - - - -')
for i in range(len(NA.arroznew())):
    print(NA.arroznew()[i])
linha()
for j in range(len(NC.cafenew())):
    print(NC.cafenew()[j])
linha()
for k in range(len(NS.sojanew())):
    print(NS.sojanew()[k])
linha()