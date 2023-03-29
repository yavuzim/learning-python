import numpy as np

sayilar = np.array([78,45,1998,785,200,100,96,35,17,56,103,96,99])

# Tüm verileri getir.
veri = sayilar[::] # ya da print(sayilar)

# 5. indekste olan veriyi getir.
veri = sayilar[5]

# Son indeksteki veriyi getir.
veri = sayilar[-1] # ya da veri = sayilar[len(sayilar)-1]

# İlk 4 elemanı getir.
veri = sayilar[0:4] # ya da veri = sayilar[:4]

# 3.indeksten sonraki elemanları getir.
veri = sayilar[3:]

# Listeyi tersten yaz.
veri = sayilar[::-1]

#############################################################################################

# 3x3 matris
matris = np.array([[1,4,9],[16,25,36],[49,64,81]])

# Tüm verileri getir.
veri = matris[::] 
veri = matris[:]
veri = matris[:3,:3]
print(matris)

# Birinci satırdaki verileri getir.
veri = matris[0]

# İkinci satırdaki verileri getir.
veri = matris[1] 
veri = matris[1,:]

# Üçüncü satırdaki verileri getir.
veri = matris[2]
veri = matris[-1,:]

# İlk satırdaki son veriyi getir.
veri = matris[0,2]

# İkinci satırdaki ilk veriyi getir.
veri = matris[1,0]

# Tüm satırların son verilerini getir.
veri = matris[:,2]

# Tüm satırların ilk verilerini getir.
veri = matris[:,0]

# Tüm satırlardan ilk 2 veriyi getir.
veri = matris[:,0:2]

# İlk 2 satırın ilk 2 elamanını getir.
veri = matris[:2,:2]


#############################################################################################

dizi1 = np.arange(0,10)

dizi2 = dizi1 # aynı referans

print(f"dizi1 : {dizi1} \n dizi2 : {dizi2}")

# dizi1 ve dizi2 aynı referansı tuttuklarından dolayı dizi2'nin 2.indisi 20 olursa dizi1'inde 2. indisi 20 olur.
dizi2[2] = 20 
print(f"dizi1 : {dizi1} \n dizi2 : {dizi2}")
#**************************************************
arr1 = np.arange(0,10)
arr2 = arr1.copy() # farklı referans
print(f"arr1 : {arr1} \n arr2 : {arr2}")

# arr1 ve arr2 farklı referansı tuttuklarından dolayı dizi2'nin 2.indisi 20 olursa dizi1'inde 2. indisinde bir değişiklik olmaz.
arr2[2] = 20
print(f"arr1 : {arr1} \n arr2 : {arr2}")