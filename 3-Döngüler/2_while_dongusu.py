sayilar = [1,3,5,7,9,12,19,21]

# 1- sayilar listesini while ile ekrana yaz.

i = 0
while i<len(sayilar):
    print(sayilar[i])
    i+=1 

# 2- Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki
#    aradaki tüm tek sayıları ekrana yaz.

baslangic = input("Başlangıç : ")
bitis = input("Bitiş : ")
baslangic = int(baslangic)
bitis = int(bitis)

while baslangic<=bitis:
    if baslangic % 2 == 1:
        print(baslangic)
    baslangic+=1


# 3- 1-100 arasındaki sayıları azalan şekilde yaz.

x = 100
while x>0:
    print(x)
    x-=1

# 4- Kullanıcıdan alacağınız sınırsız ürün bilgisini urunler listesi içiden sakla
#    ** ürün sayısını kullanıcıya sor.
#    ** dictionary listesi yapısında olsun.
#    ** ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listele.

urunAdet = input("Ürün Sayısı : ")
urunAdet = int(urunAdet)
urunler = []
sayac = 1
while sayac<=urunAdet:
    urunAd = input("Ürün Adı : ")
    urunFiyat = input("Ürün fiyatı : ")
    urunler.append({
        "name" : urunAd,
        "price" : urunFiyat
    })
    sayac+=1

i = 0
while i<len(urunler):
    print(urunler[i])
    i+=1

