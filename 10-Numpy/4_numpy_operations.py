import numpy as np

sayilar1 = np.random.randint(10,100,6)
sayilar2 = np.random.randint(10,100,6)

print(f"sayilar1 : {sayilar1} \n sayilar2 : {sayilar2}")

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

logaritma = np.log(sayilar1)
print(f"logaritma : {logaritma}")


#############################################################################################

s1 = np.array([1,4,9,16,25,36])
s2 = np.array([1,8,27,64,12,196])
matris1 = s1.reshape(2,3)
matris2 = s2.reshape(2,3)
print(f"matris1 : {matris1}")
print(f"matris2 : {matris2}")

# matrisleri dikey birleştir.
dikeyBirles = np.vstack((matris1,matris2))
print(f"Sonuç : {dikeyBirles}")

# matrisleri yatay birleştir.
yatayBirles = np.hstack((matris1,matris2))
print(f"Sonuç : {yatayBirles}")

kontrolEt = s1 >= 10      # s1 listesinde 10 dan büyük olanları kontrolEt listesinde True, küçük olanları False ekler.
print(f"kontrolEt : {kontrolEt}")
print(f"sayilar1[kontrolEt] : {s1[kontrolEt]}") # True olanları liste şeklinde yazar.