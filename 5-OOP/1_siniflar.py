# class

class Person:
    pass
    # nitelikler (attributes)
    bolum = "Bilgi Girilmedi"

    # yapıcı metot (cpnstructor)
    def __init__(self,isim,yil,bolum):
        self.isim = isim
        self.yil = yil
        self.bolum = bolum  
        print("init metodu çalıştı.")   

    # metotlar

# object (instance)
p1 = Person("Kemal Yavuz",1998,"Bilgisayar Mühendisliği")
p2 = Person("Taner",1999,"Sınıf Öğretmenliği")

print(f" isim : {p1.isim} - yıl : {p1.yil} - bölüm : {p1.bolum}")
print(f" isim : {p2.isim} - yıl : {p2.yil} - bölüm : {p2.bolum}")