'''
Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi.
Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta.
Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä.
Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa.
Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

    Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan
    väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
    Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.

Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä.
Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna.
'''
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
        round_counter1 = 0
        while round_counter1 < self.tuntimäärä:
            round_counter1 += 1
            self.nopeuden_muutos = random.randint(-10, 15)
            self.nopeus = self.nopeus + self.nopeuden_muutos
            self.matka = self.matka + self.nopeus * self.tuntimäärä
            print(f"nopeuden muutos5: {self.nopeuden_muutos}")
            print(f"nopeus5: {self.nopeus}")
            #print(f"matka1 {self.matka}")
            if self.matka > 5000:
                print("ylitty")
                break
        '''
        else:
            print("kisa ohi")
        '''
        print(f"Voittaja on: {self.rekisteritunnus}")


a1 = Auto("ABC-1")
a2 = Auto("ABC-2")
a3 = Auto("ABC-3")
a4 = Auto("ABC-4")
a5 = Auto("ABC-5")
a6 = Auto("ABC-6")
a7 = Auto("ABC-7")
a8 = Auto("ABC-8")
a9 = Auto("ABC-9")
a10 = Auto("ABC-10")

round_counter2 = 0
while round_counter2 < 200:
    round_counter2 += 1
    a1.kulje(1)
    if a1.matka > 500:
        print("ylitty")
        break
    print(f"matka2: {a1.matka}")
    a2.kulje(1)
    if a2.matka > 500:
        print("ylitty")
        break
    print(f"matka2: {a2.matka}")
    a3.kulje(1)
    if a3.matka > 500:
        print("ylitty")
        break
    print(f"matka2: {a3.matka}")




    #Auto.kulje(10) = a1, a2, a3, a4, a5, a6, a7, a8, a9


'''
a1.tulosta_ominaisuudet()
a2.tulosta_ominaisuudet()
a8.tulosta_ominaisuudet()
a10.tulosta_ominaisuudet()
'''