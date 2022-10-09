import numpy as np

sonuc = np.arange(1,10)                     # [1 2 3 4 5 6 7 8 9]

sonuc = np.arange(10,100,3)                 # [10 13 16 19 ... 97]

sonuc = np.zeros(10)                        # [0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

sonuc = np.ones(10)                         # [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]

sonuc = np.linspace(0,100,5)                # [  0.  25.  50.  75. 100.]

sonuc = np.linspace(0,5,5)                  # [0.   1.25 2.5  3.75 5.  ]

sonuc = np.random.randint(0,10)             # Rastgele sayı üretir. 0 <= sonuc < 10

sonuc = np.random.randint(20)               # Rastgele sayı üretir. 0 <= sonuc < 20

sonuc = np.random.randint(1,10,3)           # [7 4 4] <- Rastgele üretildi. 

sonuc = np.random.rand(2)                   # [0.87102353 0.26386273] 0 ve 1 arası rastgele 2 sayı

np_array = np.arange(50)                    # [0 1 2 3 4 5 ... 47 48 49]

np_multi = np_array.reshape(5,10)           # 5x10 matris

print(np_multi.sum(axis=1))                 # np_multi matrisinin her satırının toplamı. [ 45 145 245 345 445]
rnd_sayilar = np.random.randint(1,100,10) 
enBuyuk = rnd_sayilar.max()                 # Üretilen en büyük sayı.
enKucuk = rnd_sayilar.min()                 # Üretilen en küçük sayı.
ortalama = rnd_sayilar.mean()               # Üretilen sayıların ortalamaları.
buyukSayiIndex = rnd_sayilar.argmax()       # Üretilen en büyük sayının indeksi.
kucukSayiIndex = rnd_sayilar.argmin()       # Üretilen en küçük sayının indeksi.


