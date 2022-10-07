class Film():
    def __init__(self,baslik,yonetmen,sure):
        self.baslik = baslik
        self.yonetmen = yonetmen
        self.sure = sure
        print("Film objesi oluşturuldu")
    def __str__(self):
        return f"{self.baslik} filminin yönetmeni : {self.yonetmen}"
    def __len__(self):
        return self.sure
    def __del__(self):
        print(f"{self.baslik} filmi silindi")

f1 = Film("Dağ 1","Alper Çağlar",90)
print(str(f1)) # __str__ 'yi çalıştırır.
print(f"{len(f1)} filminin süresi : {len(f1)} dakika") # __len__ metodunu çalıştırır.
del(f1) # __del__ metodunu çalıştırır.

f2 = Film("Drishtam","Nishikant Kamat",163)
print(str(f2)) # __str__ 'yi çalıştırır.
print(f"{len(f2)} filminin süresi : {len(f2)} dakika") # __len__ metodunu çalıştırır.