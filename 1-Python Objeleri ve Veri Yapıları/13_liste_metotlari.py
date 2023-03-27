sayilar = [1,3,7,88,45,31,47]
harfler = ["l","x","f","t"]

# dizi uzunluğu.
print(len(sayilar))

# en küçük sayıyı yaz.
print(min(sayilar))
# en büyük sayıyı yaz.
print(max(sayilar))
# ilk harfi yaz.
print(min(harfler))
# son harfi yaz.
print(max(harfler))

# 2.indisten başla 4 karater al.
print(harfler[2:4]) 

# sayilar dizisinin sonuna 72 ekle.
sayilar.append(72)
print(sayilar)

# sayılar dizisinin 3.indeksine 78 ekle.
sayilar.insert(3,78)
print(sayilar)

# en son indeksten bir öncekine 56 ekle.
sayilar.insert(-1,56)
print(sayilar)

# son elemanı sil.
sayilar.pop()
print(sayilar)

# 0.indisteki elemanı sil.
sayilar.pop(0)
print(sayilar)

# listedeki 45 sayısını sil.
sayilar.remove(45)
print(sayilar)

# sayilar listesini küçükten büyüğe sırala.
sayilar.sort()
print(sayilar)

# sayilar dizisini ters çevir.
sayilar.reverse()
print(sayilar)

# dizide kaç tane 56 var?
print(sayilar.count(56))

# tüm elemanları sil.
sayilar.clear()
print(sayilar)





















