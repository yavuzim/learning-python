# tuple oluşturma.

meyveler = ("elma","çilek","kivi","muz","portakal","ananas","erik","armut")
print(meyveler)

sayilar = (1,8,31,23,47,21)
print(sayilar)

isimler = ("kemal",)
print(isimler)

sonuclar = (True,False,True,True)
print(sonuclar)


# tuple uzunluğu.
uzunluk = len(meyveler)
print(uzunluk)

# 1.indisteki elemanı getir.
print(meyveler[1])

# son elemanı getir.
print(meyveler[-1])

# sondan 2.elemanı getir.
print(meyveler[-2])  # ya da print(meyveler[len(meyveler)-2])


# 2.indisten başla baştan 7 eleman getir.
print(meyveler[2:7])

# baştan 5 eleman getir.
print(meyveler[:5])

# sondan 3 eleman getir.
print(meyveler[len(meyveler)-3:])

# -4.indisten başlayıp (sondan 4.) -1.indise kadar al (-1 son indis - dahil etme)
print(meyveler[-4:-1])

# elma verisini üzüm olarak değiştir.
meyveler = list(meyveler)
meyveler[0] = "üzüm"
print(meyveler)

# elma verisini ekle.
meyveler = list(meyveler)
meyveler.append("elma")
print(meyveler)

# kivi verisini sil.
meyveler = list(meyveler)
meyveler.remove("kivi")
print(meyveler)

# iki tupleyi birleştirme
meyveler+=sayilar
print(meyveler)

# tupleyi komple sil.
del meyveler