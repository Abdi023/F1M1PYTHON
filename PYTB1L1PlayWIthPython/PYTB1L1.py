2 + 2
3 * 10
100 - 10
25 / 5
10 / 3
10 // 3

# Verander <JOUW NAAM HIER> in je eigen naam
print('Mijn naam is <Abdi Abdikarim>')
naam = '<Abdi Abdikarim>'
print(naam)
print(naam.upper())
print(naam[0:2])
print(naam[::-1])

# Verander dit in je eigen leeftijd
leeftijd = 20
print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
leeftijd = leeftijd + 1
leeftijd
leeftijd-=1
leeftijd

if leeftijd < 20:
    hoelang_tot20jaar = 20 - leeftijd
    print('Over ' + str(hoelang_tot20jaar) + ' jaar wordt je 20')
elif leeftijd > 20:
    hoelang_al18jaar = leeftijd - 20
    print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 20 werd ;-)')
else:
    print('Je bent precies ' + str(leeftijd) + ' jaar')
    # Let op: hier 2x een enter doen!

# Willekeurige getallen genereren
from random import randint
randint(0,1000)
willekeurig_getal = randint(0,1000)
willekeurig_getal
print('Willekeurig getal tussen 0 en 1000: ' + str(willekeurig_getal))

# Datum en tijd
from datetime import datetime
datum = datetime.now()
print(datum)
datum.strftime('%A %d %B %Y')

# Nu in een andere taal
import locale
locale.setlocale(locale.LC_TIME, 'nl_NL')
datum.strftime('%A %d %B %Y')
locale.setlocale(locale.LC_TIME, 'it_IT')
datum.strftime('%A %d %B %Y')