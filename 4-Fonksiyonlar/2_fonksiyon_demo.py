# 1- Gönderilen bir kelimeyi belirten kez ekranda yazan fonksiyon.

def yaz(mesaj,tekrarSayisi):
    for item in range(tekrarSayisi):
        print(mesaj)

mesaj = input("Mesaj : ")
tekrarSayisi = input("Tekrar Sayısı : ")
tekrarSayisi = int(tekrarSayisi)
yaz(mesaj,tekrarSayisi)

########################################################################

# 2- Kendisine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyon.

def listeOlustur(*parametreler):
    liste = []
    for parametre in parametreler:
        liste.append(parametre)
    return liste
print(listeOlustur(10,20,30,48,"Kemal"))

########################################################################

# 3- Gönderilen iki sayı arasındaki tüm asal sayıları.

def asalMi(sayi1,sayi2):
    kontrol = True
    for i in range(sayi1,sayi2,1): # 4 5 6 7 8 9      2 3 5 7 
        for j in range(2,i,1):
            if i % j == 0:
                kontrol = True
                break
            else:
                kontrol = False
        if kontrol == False:
            print(i)      

sayi1 = 0
sayi2 = 0
while sayi1>=sayi2:
    sayi1 = input("1.sayı : ")
    sayi2 = input("2.Sayı :")
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
asalMi(sayi1,sayi2)

########################################################################

# 4- Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyon.

def tamBolenler(sayi):
    liste = []
    i = 1 
    while i<sayi:
        if sayi % i == 0:
            liste.append(i)
        i+=1
    return liste

sayi = input("Sayı : ")
sayi = int(sayi)
print(tamBolenler(sayi))
