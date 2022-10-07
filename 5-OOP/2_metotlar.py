# class

class Person:
    bolum = "Bilgi Girilmedi"

    def __init__(self,isim,yil,bolum):
        self.isim = isim
        self.yil = yil
        self.bolum = bolum  
        print("init metodu çalıştı.")   

    # metotlar
    def yazdir(self):
        print(f"Merhaba {self.isim}")
    def yasHesapla(self):
        return 2022 - self.yil

# object (instance)
p1 = Person("Kemal Yavuz",1998,"Bilgisayar Mühendisliği")
p2 = Person("Taner",1999,"Sınıf Öğretmenliği")

print(f" isim : {p1.isim} - yıl : {p1.yil} - bölüm : {p1.bolum}")
print(f" isim : {p2.isim} - yıl : {p2.yil} - bölüm : {p2.bolum}")
p1.yazdir()
print(f" Ad : {p1.isim} - Yaş : {p1.yasHesapla()}")
p2.yazdir()
print(f" Ad : {p2.isim} - Yaş : {p2.yasHesapla()}")

print("#############################################################################")

# Uygulama : Daire alan ve çevre hesaplama
class Circle:
    pi = 3.14
    def __init__(self,yaricap=1):
        self.yaricap = yaricap
    def cevreHesapla(self):
        return 2*self.pi*self.yaricap
    def alanHesapla(self):
        return self.pi*(self.yaricap**2)

c1 = Circle()
print(f"c1 -> Alan : {c1.alanHesapla()} - Çevre : {c1.cevreHesapla()}")

c2 = Circle(2)
print(f"c2 -> Alan : {c2.alanHesapla()} - Çevre : {c2.cevreHesapla()}")

c3 = Circle(3)
print(f"c3 -> Alan : {c3.alanHesapla()} - Çevre : {c3.cevreHesapla()}")


