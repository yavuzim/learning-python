# random modülünü import et.
import random as rnd

# random metotlarını getirme.
sonuc = dir(rnd)
print(sonuc)

# random metotlarının kullanımlarını getir.
sonuc = help(rnd)
print(sonuc)

# 0 ile 1 arasında rastgele sayı üret.
uret = rnd.random()
print(uret)

# 1 ile 10 arasında ondalıklı sayı üret.
ondalikliSayi = rnd.uniform(1,10)
print(ondalikliSayi)

# 1 ile 10 arasında tam sayı üret.
tamSayi1 = int(rnd.uniform(1,10))
print(tamSayi1)
tamSayi2 = rnd.randint(1,10)
print(tamSayi2)

# liste içinde rastgele veri çekme.
isimler = ["Alp","Yavuz","Taner","Tarık","Sefa"]
secilenIsim = rnd.choice(isimler)
print(secilenIsim)

# listedeki elemanların yerlerini rastgele değiştir.
liste = list(range(10))
print(liste)
rnd.shuffle(liste)
print(liste)

# listeden rastgele 3 tane eleman getir.
liste = range(10)
sonuc = rnd.sample(liste,3)
print(sonuc)