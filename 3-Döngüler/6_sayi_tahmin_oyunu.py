import random

print("** ZORLUKLAR **")
print(" 1- 5 HAK (KOLAY) \n 2- 3 HAK (ORTA) \n 3- 1 HAK (ZOR)")

zorlukSec = input("Zorluk Derecesi : ")
zorlukSec = int(zorlukSec)

hak = 0

if zorlukSec == 1 : hak = 5
elif zorlukSec == 2: hak = 3
else : hak = 1

print(f"Hak Sayınız : {hak}")

uretilenSayi = random.randint(0, 101)

print(f"uretilenSayi : {uretilenSayi}")

yanlis = 0
i = 0
while(yanlis<hak):
    i+=1
    tahmin = input("Tahmin : ")
    tahmin = int(tahmin)
    if tahmin<uretilenSayi and yanlis<hak:
        print("Yukarı")
        yanlis+=1
        print(f"Kalan Hakkınız : {hak - yanlis}")
    elif tahmin>uretilenSayi:
        print("Aşağı")
        yanlis+=1
        print(f"Kalan Hakkınız : {hak - yanlis}")
    else :
        print(f"Tebrikler {i}. tahminde bildiniz!")
        break

if yanlis == hak : print("HAKKINIZ BİTTİ - KAYBETTİNİZ")
