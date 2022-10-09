import numpy as np

# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturun.

npArr = np.array([10,15,30,45,60])
print(f"npArr : {npArr}")

# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturun.

npArr = np.arange(5,15)
print(f"npArr : {npArr}")

# 3- (50-100) arasında 5'er 5'er artarak ilerleyen numpy dizisi oluşturun.

npArr = np.arange(50,100,5)
print(f"npArr : {npArr}")

# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturun.

sifirlar = np.zeros(10)
print(f"sifirlar : {sifirlar}")

# 5- 10 elemanlı birlerden oluşan bir dizi oluşturun.

birler = np.ones(10)
print(f"birler : {birler}")

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.***

esitAraliklar = np.linspace(0,100,5)
print(f"esitAraliklar : {esitAraliklar}")

# 7- (10-30) arasında rastgele 5 tane tamsayı üretin.

uretilenSayilar = np.random.randint(10,30,5)
print(f"uretilenSayilar : {uretilenSayilar}")

# 8- [1 ile -1] arasında 10 tane sayı üret.
uret = np.random.rand(10)
print(f"uret : {uret}")

# 9- (3x5) boyutlarında (10-50) arasında rastgele matris oluşturun.

matris = np.random.randint(10,50,15).reshape(3,5)
print(f"matris : {matris}")

# 10- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız.

satirToplam = matris.sum(axis=1)
sutunToplam = matris.sum(axis=0)
print(f"satirToplam : {satirToplam} - sutunToplam : {sutunToplam}")

# 11- Üretilen matrisin en büyük, en küçük ve ortlamasını hesaplayınız.

enBuyuk = matris.max()
enKucuk = matris.min()
ortalama = matris.mean()
print(f"enBuyuk : {enBuyuk} - enKucuk : {enKucuk} - ortalama : {ortalama} ")

# 12- ÜRetilen en büyük değerinin indeksi kaçtır?

index = matris.argmax()
print(f"index : {index}")

# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elamanını seçiniz.

dizi = np.arange(10,20)
print(f"dizi : {dizi}")
print(f"ilk üç eleman : {dizi[0:3]}")

# 14- Üretilen dizinin elemanlarını tersten yazdırın.

print(f"tersten : {dizi[::-1]}")

# 15- Üretilen matrisin ilk satırısnı seçiniz.

matris = np.arange(0,15).reshape(3,5)
print(f"matris : {matris}")
print(f"ilk satır : {matris[0]}")

# 16- Üretilen matrisin 2.satır 3.sütunundaki eleman hangisidir?

print(f"2.satır - 3.sütun : {matris[2][3]}")

# 17- Üretilen matrisin tüm satırlardaki ilk elemanlarını seçin.

print(f"tüm satırlardaki ilk elemanlar : {matris[:,0]}")

# 18- Üretilen matrisin her bir elemanın karesini alın.

print(f"kareleri : {matris[::]**2}")

# 19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır ? Aralık (-50,+50) arasında yapınız.

matris = np.random.randint(-50,50,15).reshape(3,5)
print(f"matris : {matris}")
cift =  matris[matris[::] % 2 == 0]
sonuc = cift[cift>0]
print(f"pozitif çift sayılar : {sonuc}")