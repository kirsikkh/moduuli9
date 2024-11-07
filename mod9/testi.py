import random
#round_counter = 0

class Auto:
    pass

auto = Auto()

class Auto:
    def __init__(self, rekisteritunnus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = random.randint(100, 200)
        self.nopeus = 60
        self.matka = 0
    def tulosta_ominaisuudet(self):
        print(f"Tämänhetkinen nopeus: {self.nopeus}km")
        print(f"Huippunopeus: {self.huippunopeus}km")
        print(f"Matka: {self.matka}km")
        print(f"Nopeuden muutos: {self.nopeuden_muutos}")
        print(f"Tuntimäärä1: {self.tuntimäärä}")
    def kiihdytä(self, nopeuden_muutos):
        self.nopeus = self.nopeus + self.nopeuden_muutos
        print(f"nopeus1 {self.nopeus}")
        #rajoitetaan kiihdytyksen tulos huippunopeuteen
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        #auto pysähtyy, jos nopeus alle 0
        if self.nopeus < 0:
            self.nopeus = 0
    def kulje(self, tuntimäärä):
        self.tuntimäärä = tuntimäärä
        round_counter = 0
        while round_counter < self.tuntimäärä:
            round_counter += 1
            self.nopeuden_muutos = random.randint(-10, 15)
            self.nopeus = self.nopeus + self.nopeuden_muutos
            self.matka = self.matka + self.nopeus * self.tuntimäärä
            print(f"matka1 {self.matka}")
            if self.matka > 5000:
                print("ylitty")
                break
        else:
            print("kisa ohi")
        print(f"Voittaja on: {self.rekisteritunnus}")

'''
komento = input("Anna komento: ")
                while komento != "lopeta":
                    if komento == "MAYDAY":
                        break
                    print("Suoritan toiminnon: " + komento)
                    komento = input("Anna komento: ")
                else:
                    print("Näkemiin.")
                print("Toiminnot lopetettu.")
'''

a1 = Auto("ABC-1")

a1.kulje(100)
#print(self.nopeuden_muutos)

a1.tulosta_ominaisuudet()
a1.kiihdytä(a1.nopeuden_muutos)
