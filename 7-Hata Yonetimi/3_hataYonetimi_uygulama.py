# 1- Liste elemanlar içindeki sayısal değerleri bulunuz.
liste = ["1","2","5a","10b","abc"]
try:
    for i in liste:
        print(int(i))
except ValueError as e:
    print(e)

# 2- Kullanıcı 'q' değerini girmedikçe alınan her inputun sayı olduğundan 
# emin olunuz aksi hata mesajı yazın.

deger = ""
sayilar = []
while True:
    try:
        deger = input("Değer : ")
        if deger == "q" :
            break
        deger = int(deger)
        sayilar.append(deger)
    except ValueError:
        print("Hatalı Değer")
print(sayilar)
print("Bitti")

# 3- Girilen parola içinde türkçe karakter hatası veriniz.
def sifreKontrol(sifre):
    import re
    if  re.search("[ı,İ,ü,Ü,Ç,ç,Ş,ş,ğ,Ğ,ö,Ö]",sifre):
        raise Exception("Şifre Türkçe Karakter İçermemelidir.")
parola = input("Şifre : ")
try:
    sifreKontrol(parola)
except Exception as ex:
    print(ex)
else: print("Şifreniz Oluşturuldu.")

# 4- Faktoriyel fonksiyonu oluşturup fonksiyona gelen değer için hata mesajı
# verin.

def faktoriyel(sayi):
    import re
    carpim = 1
    if sayi<0:
        raise Exception("Değer negatif olamaz!")
    elif sayi==0:
        carpim = 1
    else:
        for i in range(1,sayi+1):
            carpim*=i

    return carpim
sonuca = 1
try:
    sayi = int(input("Sayı : "))
    sonuc = faktoriyel(sayi)
except Exception as err:
    print(err)
except ValueError as err:
    print(err)
else: print(f"{sayi}! = {sonuc}")