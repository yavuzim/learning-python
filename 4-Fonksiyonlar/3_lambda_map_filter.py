# map()

sayilar = [4,9,12,18,13,15]

def usAl(sayi) : return sayi**2

sonuc = list(map(usAl,sayilar)) # sayılar listesindeki her bir elemanı döndürerek usAl fonksiyonunun işlevini gerçekleştirir.
print(sonuc)

######################################################################

sonuc = list(map(lambda birleTopla : birleTopla+1,sayilar)) # lambda ifadesini kullanarak map'in içinde isimsiz fonksiyon yazabiliriz.
print(sonuc)

######################################################################

kubAl = lambda kub : kub**3 # lambda'yı değişkene atarak yapma.
sonuc = list(map(kubAl,sayilar))
print(sonuc)

######################################################################
######################################################################

# filter()

def ciftSayi(sayi): return sayi%2==0

sonuc = list(map(ciftSayi,sayilar)) # True veya False döner.  [True, False, True, True, False, False]
print(sonuc)
sonuc = list(filter(ciftSayi,sayilar)) # Çiftleri döner.  [4, 12, 18]
print(sonuc)
