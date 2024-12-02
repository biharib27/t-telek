'''Készítsen programot, ami az alábbi listában tárolt értékekkel dolgozik.

A program írja ki, hogy
a) Hány dátum volt az 2000 előtt!
b) Listázza ki a szeptember hónapra eső dátumokat!
c) Melyik volt a legutolsó év a dátumok között? (Csak az évet írja ki!)'''

date_list = [ '1983-06-15', '1991-12-07', '1987-03-24', '2001-08-19', '2015-04-03', '1980-11-21', '1999-02-28', '2008-09-12', '1995-01-05', '2020-07-09', '1986-10-30', '1993-05-14', '2011-06-26', '1989-12-18', '2005-03-11', '2018-09-01', '1997-07-20', '2012-11-03', '2023-01-22', '1990-04-09' ]

elott_2000 = 0
evszamok = []  
szeptemberi_datumok = []  
legutolso_ev = None

for datum in datumok:
    ev = int(datum[:4])  
    honap = datum[5:7] 
    evszamok.append(ev)
    
    if ev < 2000:
        elott_2000 += 1

    if honap == "09":
        szeptemberi_datumok.append(datum)

    if legutolso_ev is None or ev > legutolso_ev:
        legutolso_ev = ev
szeptemberi_lista = ", ".join(szeptemberi_datumok)

print(f"2000 előtt összesen {elott_2000} dátum volt.")
print(f"Szeptemberi dátumok: {szeptemberi_lista}")
print(f"A legutolsó év: {legutolso_ev}")

