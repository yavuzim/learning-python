dersAdi = "Algortima Analizi"

print("Ders Adı : {}".format(dersAdi)) # .format(dersAdi)'a gelen değer {} içine yazılır.
# Ders Adı Algortima Analizi

dersAkts = 6
print("Ders Adı : {} - AKTS : {}".format(dersAdi,str(dersAkts)))
# Ders Adı : Algortima Analizi - AKTS : 6

print("Ders Adı : {d} - AKTS : {a}".format(d = dersAdi,a = str(dersAkts))) # Parantezlere değişken vererekte yapabiliriz.
# Ders Adı : Algortima Analizi - AKTS : 6

print(f"Ders Adı : {dersAdi} - AKTS : {dersAkts}") # Başına f yazdığımızda {} içinde değişken isimlerini belirtiriz.


sonuc = 200/700
print("Sonuc : {}".format(sonuc))
# Sonuc : 0.2857142857142857
print("Sonuc : {s:1.4}".format(s = sonuc)) # Baştan 1 basamak boşluk ve virgülden sonra 4 basamak al.
# Sonuc : 0.2857