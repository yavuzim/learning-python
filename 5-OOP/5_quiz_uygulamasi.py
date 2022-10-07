class Sinav:
    def __init__(self, soruSayisi, dogruSayisi, puan):
        self.soruSayisi = soruSayisi
        self.dogruSayisi = dogruSayisi
        self.puan = puan

    def soruEkle(self):
        liste = {}
        soruSirasi = self.soruSayisi+1-self.soruSayisi
        while soruSirasi <= self.soruSayisi:
            soru = input(f"{soruSirasi}. Soru : ")
            a = input("A : ")
            b = input("B : ")
            c = input("C : ")
            d = input("D : ")
            cevap = input("Cevap : ")
            liste.update({
                soruSirasi: {
                    "Soru": soru,
                    "A": a,
                    "B": b,
                    "C": c,
                    "D": d,
                    "cevap": cevap
                }
            })
            soruSirasi += 1
        return liste

    def sinavaBasla(self, liste, soruSira):
        if soruSira > len(liste):
            return f"Doğru Sayınız : {self.dogruSayisi} - Yanlış Sayınız : {len(liste) - self.dogruSayisi} - Puanınız : {self.puan}"
        else:
            self.__sorulariCagir(soruSira)
            __cevap = self.__soruCevapla()
            if liste[soruSira]['cevap'] == __cevap:
                self.dogruSayisi += 1
                self.puan = self.puan + 20
            return self.sinavaBasla(liste, soruSira+1)

    def __soruCevapla(self):
        __cevap = input("Cevabınız : ")
        return __cevap

    def __sorulariCagir(self, soruSirasi):
        print(f"Soru : {liste[soruSirasi]['Soru']}")
        print(f"A : {liste[soruSirasi]['A']}")
        print(f"B : {liste[soruSirasi]['B']}")
        print(f"C : {liste[soruSirasi]['C']}")
        print(f"D : {liste[soruSirasi]['D']}")


soruSayisi = 0
while soruSayisi <= 0 or soruSayisi > 10:
    soruSayisi = input("Soru Sayısı : ")
    soruSayisi = int(soruSayisi)
sinav = Sinav(soruSayisi,0,0)
liste = sinav.soruEkle()
print("#####################################################################")
soruSira = 1
sonuc = sinav.sinavaBasla(liste, soruSira)
print(sonuc)
