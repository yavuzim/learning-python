mesaj = "python Öğreniyorum. "

print(mesaj)
# Python Öğreniyorum.

print(mesaj.upper()) # Karakterleri büyük harfe çevirir.
# Python Öğreniyorum.

print(mesaj.lower()) # Karakterleri küçük harfe çevirir.
# python öğreniyorum.

print(mesaj.capitalize()) # Değerin sadece ilk harfini büyük yapar.
# Python öğreniyorum.

print(mesaj.strip()) # Değerin başındaki ve sonundaki boşlukları siler.

print(mesaj.split()) # Değer içindeki boşluklara göre ayırıp her birini bir dizinin elemanı şeklinde yazar.
# ['python', 'Öğreniyorum.']


print(mesaj.split(".")) # Noktaya göre ayırır.
# [' python Öğreniyorum', ' ']

x = "-".join(mesaj) # Aralarına - ekler.
print(x)
# Y-a-p-a-y- -Z-e-k-a
 
indis = mesaj.find("python") # python kelimesini arar ve değer varsa ilk karakterinin indisini yazar.
print(indis)
# 1

print(mesaj.startswith("p")) # p ile başlıyorsa true değilse false
# true
print(mesaj.endswith("m")) # m ile bitiyorsa true değilse false
# false

print(mesaj.replace("python","Yapay Zeka")) # python yerine Yapay Zeka yazdırır.
# Yapay Zeka Öğreniyorum.

print(mesaj.center(100)) # Verilen string değerini yani mesaj verisini sağ ve solundan 100 karakter ekler.Stringi ortalar.
