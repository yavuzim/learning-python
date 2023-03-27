github = "https://www.github.com/yavuzim"
okul = "Fırat Üniversitesi Bilgisayar Mühendisliği"

# 1- 'okul' karakter dizisinde kaç karakter vardır?
print(len(okul))

# 2- 'github' içinde www karakterini al.
print(github[8:11])

# 3- 'github' içinde yavuzim karakterini al.
print(github[23:30])

# 4- 'okul' karakter dizisinde ilk 7 ve son 7 karakteri al.
ilkYedi = okul[0:7]
sonYedi = okul[-7:]
print("İlk 7 : "+ilkYedi)
print("Son 7 : "+sonYedi)

# 5- 'okul' ifadesindeki karakterleri tersten yazdır.
print(okul[::-1])

isim,soyisim,yas,meslek = "Kemal Yavuz","İMER",24,"Bilgisayar Mühendisi"
'''
   6- Yukarıda verilen değişkenler ile ekrana :
       'Benim Adım Kemal Yavuz, Yaşım 24 ve mesleğim Bilgisayar Mühendisi.'
  yazdır.
'''
print("Benim Adım {} {}, Yaşım {} ve mesleğim {}".format(isim,soyisim,str(yas),meslek))
print(f"Benim Adım {isim} {soyisim}, Yaşım {str(yas)} ve mesleğim {meslek}")

# 7- Hello world ifadesindeki w ifadesini W ile değiştir.
deger = "Hello world"
print(deger)
yeniDeger = deger[:5]+" W"+deger[7:]
print(yeniDeger)

# 8- abc ifadesini yan yana 3defa yazdır.

veri = "abc"
print(veri*3)