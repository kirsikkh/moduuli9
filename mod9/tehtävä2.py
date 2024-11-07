'''
Jatka ohjelmaa kirjoittamalla Auto-luokkaan kiihdytä-metodi,
joka saa parametrinaan nopeuden muutoksen (km/h).
Jos nopeuden muutos on negatiivinen, auto hidastaa.
Metodin on muutettava auto-olion nopeus-ominaisuuden arvoa.
Auton nopeus ei saa kasvaa huippunopeutta suuremmaksi eikä alentua nollaa pienemmäksi.
Jatka pääohjelmaa siten, että auton nopeutta nostetaan ensin +30 km/h,
sitten +70 km/h ja lopuksi +50 km/h. Tulosta tämän jälkeen auton nopeus.
Tee sitten hätäjarrutus määräämällä nopeuden muutos -200 km/h ja tulosta uusi nopeus.
Kuljettua matkaa ei tarvitse vielä päivittää.
'''

class Auto:
    pass

auto = Auto()

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 0
    def tulosta_ominaisuudet(self):
        print(f"Rekisteritunnus: {self.rekisteritunnus}")
        print(f"Huippunopeus: {self.huippunopeus}")
        print(f"Tämänhetkinen nopeus: {self.nopeus}")
    def kiihdytä(self, nopeuden_muutos):
        self.nopeus = self.nopeus + 1 + nopeuden_muutos
        #rajoitetaan kiihdytyksen tulos huippunopeuteen
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        #auto pysähtyy, jos nopeus alle 0
        if self.nopeus < 0:
            self.nopeus = 0



a1 = Auto("ABC-123", 142)

a1.kiihdytä(30)
a1.kiihdytä(70)
a1.kiihdytä(50)
a1.tulosta_ominaisuudet()
a1.kiihdytä(-200)
a1.tulosta_ominaisuudet()
