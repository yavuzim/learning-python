import numpy as np

sayilar1 = np.random.randint(10, 100, 6)
sayilar2 = np.random.randint(10, 100, 6)

print(f"sayilar1 : {sayilar1} - sayilar2 : {sayilar2}")

toplam = sayilar1 + sayilar2
print(f"toplam : {toplam}")

fark = sayilar1 - sayilar2
print(f"fark : {fark}")

carpim = sayilar1 * sayilar2
print(f"carpim : {carpim}")

bolum = sayilar1 / sayilar2
print(f"bolum : {bolum}")

sinus = np.sin(sayilar1)
print(f"sinus : {sinus}")

cosinus = np.cos(sayilar1)
print(f"cosinus : {cosinus}")

karekok = np.sqrt(sayilar1)
print(f"karekok : {karekok}")

logaritmaSonuc = np.log(sayilar1)
print(f"logaritmaSonuc : {logaritmaSonuc}")

print("############################################################")

matris1 = sayilar1.reshape(2, 3)
matris2 = sayilar2.reshape(2, 3)

print(f"matris1 : {matris1}")
print(f"matris2 : {matris2}")

dikeyBirlestir = np.vstack((matris1, matris2))
print(f"dikeyBirlestir : {dikeyBirlestir}")
print(f"dikeyBirlestir[2] : {dikeyBirlestir[2]}")

yatayBirlesitir = np.hstack((matris1, matris2))
print(f"yatayBirlesitir : {yatayBirlesitir}")
print(f"yatayBirlesitir[1] : {yatayBirlesitir[1]}")

kontrolEt = sayilar1 >= 50      # sayılar1 listesinde 50 den büyük olanları kontrolEt listesinde True, küçük olanları False ekler.
print(f"kontrolEt : {kontrolEt}")
print(f"sayilar1[kontrolEt] : {sayilar1[kontrolEt]}") # True olanları liste şeklinde yazar.


