'''Készíts egy programot, amely a felhasználótól szavakat kér be, amíg az csupán ENTER-t nem üt! A szavakat tárolja el a program egy listában!
 Az adatbekérés befejezte után írja ki a program a lista elemeit, a legrövidebb és a leghosszabb szót!'''

szavak = []

print("Adj meg szavakat! Nyomj ENTER-t, ha be szeretnéd fejezni.")


while True:
    szo = input("Adj meg egy szót: ")
    if szo == "":  
        break
    szavak.append(szo)  

if szavak:
    legrövidebb = szavak[0]
    leghosszabb = szavak[0]
    
    for szo in szavak:
        if len(szo) < len(legrövidebb):
            legrövidebb = szo
        if len(szo) > len(leghosszabb):
            leghosszabb = szo

    print("A megadott szavak:", ", ".join(szavak))
    print("A legrövidebb szó:", legrövidebb)
    print("A leghosszabb szó:", leghosszabb)
else:
    print("Nem adtál meg egyetlen szót sem.")
