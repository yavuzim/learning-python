import numpy as np

# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturun.
sayilar = np.array([10,15,30,45,60])

# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturun.
sayilar = np.arange(5,16)

# 3- (50-100) arasında 5'er 5'er artarak ilerleyen numpy dizisi oluşturun.
sayilar = np.arange(5,101,5)

# 4- 10 elemanlı sıfırlardan oluşan bir dizi oluşturun.
sifirlar = np.zeros(10)

# 5- 10 elemanlı birlerden oluşan bir dizi oluşturun.
birler = np.ones(10)

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin.***
sayilar = np.linspace(0,100,5)

# 7- (10-30) arasında rastgele 5 tane tamsayı üretin.
sayilar = np.random.randint(10,31,5)

# 8- [-1 ile 1] arasında 10 tane sayı üret.
sayilar = np.random.randn(10)

# 9- (3x5) boyutlarında (10-50) arasında rastgele matris oluşturun.
matris = np.array(np.random.randint(10,51,15)).reshape(3,5)

# 10- Üretilen matrisin satır ve sütun sayıları toplamlarını hesaplayınız.
matris = np.array(np.random.randint(10,51,10)).reshape(2,5)
satirToplam = matris.sum(axis=1)
sutunToplam = matris.sum(axis=0)

# 11- Üretilen matrisin en büyük, en küçük ve ortlamasını hesaplayınız.
matris = np.array(np.random.randint(1,10,10)).reshape(2,5)
enBuyuk = matris.max()
enKucuk = matris.min()
ortalama = matris.mean()

# 12- Üretilen en büyük değerinin indeksi kaçtır?
matris = np.random.randint(4,18,8).reshape(2,4)
ebIndis = matris.argmax()

# 13- (10-20) arasındaki sayıları içeren dizinin ilk 3 elamanını seçiniz.
dizi = np.arange(10,21)
ilkUc = dizi[:3]

# 14- Üretilen dizinin elemanlarını tersten yazdırın.
dizi = np.array([8,9,12,45])
tersYaz = dizi[::-1]

# 15- Üretilen matrisin ilk satırısnı seçiniz.
matris = np.array([[1,2,3],[4,5,6],[7,8,9]])
ilkSatir = matris[0,:]

# 16- Üretilen matrisin 2.satır 3.sütunundaki eleman hangisidir?
matris = np.array([[1,2,3],[4,5,6],[7,8,9]])
veri = matris[1,2]

# 17- Üretilen matrisin tüm satırlardaki ilk elemanlarını seçin.
matris = np.array([[1,2,3],[4,5,6],[7,8,9]])
veriler = matris[:,0]

# 18- Üretilen matrisin her bir elemanın karesini alın.
matris = np.array([[1,2,3],[4,5,6],[7,8,9]])
matris2 = matris**2

# 19- Üretilen matris elemanlarının hangisi pozitif çift sayıdır ? Aralık (-50,+50) arasında yapınız.
matris = np.random.randint(-50,51,10).reshape(2,5)
ciftler = matris[matris%2==0]
sonuc = cift[cift>0]