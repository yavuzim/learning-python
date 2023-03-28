# 1- Liste elemanlar içindeki sayısal ve string değerleri ayırınız.

liste = ["1","2","5a","10b","abc","4"]

sayiListe = []
stringListe = []
sayac = 0
while sayac<len(liste):
    try:
        sayiListe.append(int(liste[sayac]))
    except ValueError:
        stringListe.append(liste[sayac])
    finally:
        sayac+=1
        
print(sayiListe)
print(stringListe)

# 2- Kullanıcı 'q' değerini girmedikçe alınan her inputun sayı olduğundan emin olunuz aksi hata mesajı yazın.

deger = ""
while deger!="q":
    deger = input("Değer : ")
    try:
        deger = int(deger)
    except ValueError:
        if deger!="q":
            print("Girdiğiniz Değer Hatalı")
    else:        
        print("Girilen Değer : ",deger)

# 3- Girilen parola içinde türkçe karakter hatası veriniz.

def sifre_kontrol(sifre):
    import re
    if re.search("[ı,İ,ü,Ü,Ç,ç,Ş,ş,ğ,Ğ,ö,Ö]",sifre):
        raise Exception("Şifre Türkçe Katakter İçermemelidir!")
    return sifre

sifre = input("Şifre : ")
try:
    yeniSifre = sifre_kontrol(sifre)
except Exception as ex:
    print(ex)
else:
    print("Şifre Oluşturuldu")
    print("Şifre : ",yeniSifre)
    
# 4- Faktoriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajı verin.

def faktoriyel(sayi):
    import re
    carpim = 1
    if sayi<0:
        raise Exception("sayi>-1 olmalıdır!")
    else:
        for i in range(1,sayi+1):
            carpim = carpim*i
    return carpim

sayi = int(input("Sayı : "))
try:
    sonuc = faktoriyel(sayi)
except Exception as ex:
    print(ex)
else:
    print(str(sayi)+"! = "+str(sonuc))

























