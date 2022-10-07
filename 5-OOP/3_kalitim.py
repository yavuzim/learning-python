class TemelSinif():
    def __init__(self,isim,soyisim):
        self.isim = isim
        self.soyisim = soyisim
        print("TemelSinif Çalıştı.")
        print(f"{self.isim} {self.soyisim}")

class Ogrenci(TemelSinif):
    def __init__(self,isim,soyisim):
        TemelSinif.__init__(self,isim,soyisim)
        print("Ogrenci Çalıştı")
class Ogretmen(TemelSinif):
    def  __init__(self, isim, soyisim):
        TemelSinif.__init__(self,isim, soyisim)
        print("Ogretmen Çalıştı")

o1 = Ogretmen("Yunus","Özyavuz")
o2 = Ogretmen("Bilgin","Özçalkan")
ogr1 = Ogrenci("Mozole","Mirach")