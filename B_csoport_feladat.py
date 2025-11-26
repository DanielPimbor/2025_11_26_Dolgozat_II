"""B csoport
Olvasunk be billentyűzetről egész számokat, és tároljuk őket egy listában! A bevitel végét a 0 jelezze. 
Majd oldjuk meg a következő feladatokat!Minden feladat előtt a program írja ki a feladat sorszámát!

1. Volt-e -10 és -15 közé eső szám a beírtak között?
2. Írjuk ki az utolsó 2-vel és 5-tel osztható szám indexét!
3. Hány darab 20-nál nagyobb számot írtak be?
4. Melyik és hányadik volt a legkisebb beírt pozitív egész szám?
5. Mennyi a negatív számok számok átlaga?"""

# proba_lista = [-11,-12,-13,-14,-15,10,20,30,40,33,44,77,-2,-3]

egesz_szamok_listaja = [] #szamok listaja
minusz10_minusz15 = [] #1. feladathoz
a2_5_oszthato = [] #2. feladathoz
nagyobb_20nal = [] #3.feladathoz
pozitiv_egesz_szamok = [] #4.feladathoz
negativ_szamok = [] #5.feladathoz

while True:
    try:
        egesz_szamok = int(input('Adj meg egy egész számot. (Ha 0-át adsz meg, az lezárja a bevitelt, de beleteszi a listába!!!) '))

    except ValueError:
        print('Nem egész számot adtál meg.')

    egesz_szamok_listaja.append(egesz_szamok)
    if egesz_szamok == 0:
        break

    else:
        continue


print('Itt van a listád:')
print(egesz_szamok_listaja)

print('--------------------------------------------------- \n')

print('1. feladat')

for szam in egesz_szamok_listaja:
    if szam < -10 and szam > -15:
        minusz10_minusz15.append(szam)
    
if len(minusz10_minusz15) > 0:
    print('Voltak -10 és -15 közé eső számok.')

else:
    print('Nem voltak -10 és -15 közé eső számok.')

print('--------------------------------------------------- \n')


print('2. feladat')

for szam in egesz_szamok_listaja:
    if szam % 2 == 0 and szam % 5 == 0:
        a2_5_oszthato.append(szam)

utso_szam = a2_5_oszthato[-1]
utso_szam_indexe=egesz_szamok_listaja.index(utso_szam)

if len(a2_5_oszthato) > 0:
    print(f'Ez volt az utolsó 2-vel és 5-tel osztható szám indexe: {utso_szam_indexe}')

else:
    print('Nem volt ilyen szám.')

print('--------------------------------------------------- \n')


print('3.feladat')

for szam in egesz_szamok_listaja:
    if szam > 20:
        nagyobb_20nal.append(szam)

if len(nagyobb_20nal) > 0:
    print(f'Ennyi 20 nál nagyobb szám volt: {len(nagyobb_20nal)}')

else:
    print('Nem volt 20-nál nagyobb.')

print('--------------------------------------------------- \n')


print('4.feladat')

for szam in egesz_szamok_listaja:
    if szam >= 0:
        pozitiv_egesz_szamok.append(szam)

if len(pozitiv_egesz_szamok):
    print(f'Ez volt a legkisebb pozitív egész szám: {min(pozitiv_egesz_szamok)}')

else:
    print('Nem volt pozitív egész szám.')

print('--------------------------------------------------- \n')


print('5. feladat')

for szam in egesz_szamok_listaja:
    if szam < 0:
        negativ_szamok.append(szam)


if len(negativ_szamok) > 0:
    negativ_szamok_atlaga = sum(negativ_szamok) / len(negativ_szamok)
    print(f'Ennyi volt a negatív számok átlaga: {negativ_szamok_atlaga}')

else:
    print('Nem volt negatív szám.')

print('--------------------------------------------------- \n')

