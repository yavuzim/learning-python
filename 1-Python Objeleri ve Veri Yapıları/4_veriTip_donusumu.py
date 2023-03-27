# float -> int dönüşümü

a = 5.2
b = int(a)
print("a : ",a)
print("b : ",b)

# int -> float dönüşümü

x = 5
y = float(x)
print("x : ",x)
print("y : ",y)

# Örnek 1

sayi1 = input("1.Sayı : ")  # sayi1 = 8 | Klavyeden alınan değerler her zaman stringtir.
sayi2 = input("2.Sayı : ")  # sayi2 = 9 | Klavyeden alınan değerler her zaman stringtir.
toplam = sayi1 + sayi2      # toplam = 8+9 | Değerleri int'e çevrilmediğinden + operatörü birleştirme yapar.
print("toplam : ",toplam)   # toplam = 89

# Örnek 2

s1 = input("1.Sayı : ")    # s1 = 8 | Klavyeden alınan değerler her zaman stringtir.
s2 = input("2.Sayı : ")    # s2 = 9 | Klavyeden alınan değerler her zaman stringtir.
tplm = int(s1) + int(s2)   # tplm = 8+9 | Değerleri int'e çevrilir + operatörü ile toplama yapar.
print("toplam : ",tplm)    # tplm = 17

# Örnek 3

deger1 = input("1.Sayı : ")    # deger1 = 8 | Klavyeden alınan değerler her zaman stringtir.
deger2 = input("2.Sayı : ")    # deger2 = 9 | Klavyeden alınan değerler her zaman stringtir.
sonuc = int(deger1) + float(deger2)   # sonuc = 8+9 | değer1 int, değer2 floata çevrilir ve toplama yapılır. Sonuç floattır.
print("toplam : ",sonuc)        # sonuc = 17.0

# Örnek 4

kelime = "yazılım"
cevir = int(kelime) # Hata verir. Alfabetik değerler sayısal değere çevrilmez.
print(cevir) 