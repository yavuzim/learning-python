# set oluşturma.

isimler = {"kemal","yeşim","mehmetcan","elif"}

# ekrana yaz.
print(isimler)

# set uzunluğu.
print(len(isimler))

# bir set farklı veri türleri içerebilir.

set1 = {"abc", 34.5, True, 40, "deger"}

# ögelere erişim. Döngü ile erişebiliriz.
for i in isimler:
    print(i)
    
# veri kontrolü.
print("kemal" in isimler) # kemal değeri varsa True yoksa False yazar.

# veri ekle.
isimler.add("yavuz")
print(isimler)

# isimler setine başka setten eleman ekleme.
dersler = {"Sayısal Analiz","Algoritma"}
isimler.update(dersler)
print(isimler)

# isimler setine liste elemanlarını ekleme.
liste = [8,9,14]
isimler.update(liste)
print(isimler)

# setten veri sil 1. (kaldırılacak veri yoksa hata verir.)
isimler.remove("Algoritma")
print(isimler)

# setten veri sil 2. (kaldırılacak veri yoksa hata vermez.)
isimler.discard("Sayısal Analiz")
print(isimler)

# rastgele bir öge kaldırma.
isimler.pop()
print(isimler)

# seti boşalt.
isimler.clear()
print(isimler)

# seti tamamen sil.
del isimler

