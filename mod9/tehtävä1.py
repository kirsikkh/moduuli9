'''
Kirjoita Auto-luokka, jonka ominaisuuksina ovat rekisteritunnus, huippunopeus,
tämänhetkinen nopeus ja kuljettu matka. Kirjoita luokkaan alustaja,
joka asettaa ominaisuuksista kaksi ensin mainittua parametreina saatuihin arvoihin.
Uuden auton nopeus ja kuljetut matka on asetettava automaattisesti nollaksi.
Kirjoita pääohjelma, jossa luot uuden auton (rekisteritunnus ABC-123, huippunopeus 142 km/h).
Tulosta pääohjelmassa sen jälkeen luodun auton kaikki ominaisuudet.
'''

class Auto:
    pass

auto = Auto()

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.matka = matka
    def tulosta_ominaisuudet(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus}")
        print(f"Tämänhetkinen nopeus: {self.nopeus}")
        print(f"Matka: {self.matka}")

a1 = Auto("ABC-123", "142 km/h", "82 km/h", "5 km")
a1.tulosta_ominaisuudet()

'''
print(f'Auton registeritunnus on {auto.rekisteritunnus}, huippunopeus on {auto.huippunopeus}, nopeus tällä hetkellä on {auto.nopeus} ja kuljettu matka on {auto.matka}.')

    def printtaa(self):
        print (f'{self.rekisteritunnus}, {self.huippunopeus}, {self.nopeus}, {self.matka}')
'''
#f'Koira nimi on {self.nimi} ja syntymävuosi on {self.syntymävuosi}'

'''
class Auto:
    def __init__(self, rek_nro, huippunopeus):
        self.rek_nro = rek_nro
        self.nopeus = 0
        self.huippunopeus = huippunopeus
    def tulosta_ominaisuudet(self):
        print(f"{self.rek_nro}, huippunopeus: {self.huippunopeus}")
        print(f"Tämänhetkinen nopeus: {self.nopeus}")
    def kiihdytä(self, nopeuden_muutos):
        self.nopeus = self.nopeus + 1 + nopeuden_muutos
        #rajoitetaan kiihdytyksen tulos huippunopeuteen
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        #auto pysähtyy, jos nopeus alle 0
        if self.nopeus < 0:
            self.nopeus = 0
            
'''