ogrenciler = {
    "120" : {
        "ad" : "Taner",
        "soyad" : "Çolak",
    },
     "121" : {
        "ad" : "Tarık Can",
        "soyad" : "Kaydu",
    },
     "121" : {
        "ad" : "Sefa",
        "soyad" : "Batar",
    },
}
print(ogrenciler)

# Ekleme 1.yol

numara = input("Numara : ")
ad = input("Ad : ")
soyad = input("Soyad : ")
ogrenciler[numara]={
    "ad" : ad,
    "soyad" : soyad
}
print(ogrenciler)

numara = input("Numara : ")
ad = input("Ad : ")
soyad = input("Soyad : ")
ogrenciler[numara]={
    "ad" : ad,
    "soyad" : soyad
}
print(ogrenciler)

##############################################################

# Ekleme 2.yol

numara = input("Numara : ")
ad = input("Ad : ")
soyad = input("Soyad : ")

ogrenciler.update({
    numara : {
        "ad" : ad,
        "soyad" : soyad
    }
})
print(ogrenciler)