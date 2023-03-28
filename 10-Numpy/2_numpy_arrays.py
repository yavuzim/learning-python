import numpy as np

# İçinde 1-10 arasında sayılar olan dizi. 10 dahil değil.
np_liste = np.arange(1,10)

# İçinde 1-100 arasında 2'şer 2'şer artan sayı dizisi.
np_liste = np.arange(1,10,2)

# İçinde 10 tane 0 olan dizi. Her bir değer float veri tipindedir.
np_liste = np.zeros(10)

# İçinde 10 tane 1 olan dizi. Her bir değer float veri tipindedir.
np_liste = np.ones(10)

# 0-100 arasındaki sayıları eşit aralıklarla 5 parçaya böl. Her bir değer float veri tipindedir
np_liste = np.linspace(0,100,5)

# 10-100 arasında rastgele 1 adet sayı üret. 100 dahil değil.
np_liste = np.random.randint(10,100)

# 10-100 arasında rastgele 3 adet sayı üret. 100 dahil değil.
np_liste = np.random.randint(10,100,3)
enBuyukSayi = np_liste.max() # üretilen en büyük sayıyı getirir.
enBuyukSayiIndex = np_liste.argmax() # üretilen en büyük sayıyının indexsini getirir.
enKucukSayi = np_liste.min() # üretilen en küçük sayıyı getirir.
enBuyukSayiIndex = np_liste.argmin() # üretilen en küçük sayıyının indexsini getirir.
ortalama = np_liste.mean()  # üretilen sayıların ortlamasını alır.
print("Üretilen En Büyük Sayı : ",enBuyukSayi)
print("Üretilen En Küçük Sayı : ",enKucukSayi)
print("Üretilen Sayıların Ortalaması : ",ortalama)

# 0-1 arasında 5 adet sayı üret. 1 dahil değil.
np_liste = np.random.rand(5)

# 0-1 arasında 5 adet sayı üret. Negatif değerlerde dahil. 1 dahil değil.
np_liste = np.random.randn(5)

# 5x10 matris oluşturma.
np_liste = np.arange(50).reshape(5,10)
satirDegerToplam = np_liste.sum(axis=1) # satırları toplar.
sutunDegerToplam = np_liste.sum(axis=0) # sutunları toplar.
print("Satır Toplam : ",satirDegerToplam)
print("Sütun Toplam : ",sutunDegerToplam)