import numbers


sayilar = [1,10,9,16,21,85]
harfler = ["a","x","f","t"]

print(min(sayilar)) # en küçük sayıyı yazdırır.
print(max(sayilar)) # en büyük sayıyı yazdırır.
print(min(harfler)) # ilk harfi yazdırır.
print(max(harfler)) # son harfi yazdırır.

print(harfler[2:3]) # ['f']

sayilar.append(81) # dizi sonuna 81 eklendi.
print(sayilar)

sayilar.insert(3,78) # 3. indekse 78 eklendi.
print(sayilar)

sayilar.insert(-1,56) # en son indeksten bir öncekine ekler.
print(sayilar) 

sayilar.pop() # en son elemanı siler
print(sayilar)

sayilar.pop(0) # 0. indisteki elemanı siler
print(sayilar)

sayilar.remove(9) # listedeki 9 sayısını siler
print(sayilar)

sayilar.sort() # küçükten büyüğe sıralar
print(sayilar)

harfler.sort() # alfabetik olarak sıralar (a-z)
print(harfler)

sayilar.reverse() # diziyi ters çevirir.
print(sayilar)

print(len(sayilar)) # dizi uzunluğunu gösterir.

print(sayilar.count(78)) # dizide kaç tane 78 var sorusunun cevabı.

sayilar.clear() # tüm elemanları siler.
print(sayilar)