'''
Laajenna ohjelmaa siten, että mukana on kulje-metodi,
joka saa parametrinaan tuntimäärän.
Metodi kasvattaa kuljettua matkaa sen verran kuin auto on tasaisella vauhdilla
annetussa tuntimäärässä edennyt.
Esimerkki: auto-olion tämänhetkinen kuljettu matka on 2000 km. Nopeus on 60 km/h.
Metodikutsu auto.kulje(1.5) kasvattaa kuljetun matkan lukemaan 2090 km.
'''

class Auto:
    pass

auto = Auto()

class Auto:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = 60
        self.matka = 2000
    def tulosta_ominaisuudet(self):
        print(f"Tämänhetkinen nopeus: {self.nopeus}km")
        print(f"Matka: {self.matka}km")
    def kiihdytä(self, nopeuden_muutos):
        self.nopeus = self.nopeus + 1 + nopeuden_muutos
        #rajoitetaan kiihdytyksen tulos huippunopeuteen
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        #auto pysähtyy, jos nopeus alle 0
        if self.nopeus < 0:
            self.nopeus = 0
    def kulje(self, tuntimäärä):
        self.tuntimäärä = tuntimäärä
        self.matka = self.matka + self.nopeus * self.tuntimäärä


a1 = Auto("ABC-123", 142)

a1.kulje(1.5)
a1.tulosta_ominaisuudet()