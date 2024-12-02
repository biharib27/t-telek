'''A program számolja össze, hogy hány darab 'A' vagy 'a' betűvel kezdődő szó van az adott listában (amely a 'Próbáld ki!' gombra kattintva elérhető)!
 A képernyőre írja is ki a feltételnek megfelelő szavakat!'''

szavak = ['alma' , 'barack' , 'Korte' , 'banan' , 'dinnye' , 'adomany']
helyes_szavak = []

for szo in szavak:
    if szo.startswith('a' or 'A'):
        helyes_szavak.append(szo)
print(helyes_szavak)

