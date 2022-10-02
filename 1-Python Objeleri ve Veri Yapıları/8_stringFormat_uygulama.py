github = "https://www.github.com/yavuzim"
okul = "Fırat Üniversitesi Bilgisayar Mühendisliği"

# 1- okul değişkeninde kaç karakter vardır ? 
print(len(okul)) 

# 2- github değişkeninde www karakterini al.
print(github[8:11])

# 3- github içinde com karakterini al.
print(github[19:22])

# 4- okul değişkeninde ilk 15 ve son 15 karakter al.
print("İlk 15 : "+okul[0:15]+"\n Son 15 : "+okul[-15:])

# 5- okul değişkeninin içindeki veriyi tersten yazdır.
print(okul[::-1])

isim,soyisim,yas,meslek = "Kemal Yavuz","İMER",24,"Bilgisayar Mühendisi"

#   6- Yukarıda verilen değişkenler ile ekrana :
# 'Benim Adım Kemal Yavuz, Yaşım 24 ve mesleğim Bilgisayar Mühendisi.'
# yazdır.
sonuc = f"Benim Adım {isim}, Yaşım {yas} ve mesleğim {meslek}"
print(sonuc)

# 7- Hello world ifadesindeki w ifadesini W ile değiştir.
deger = "Hello world"
print(deger)
deger = deger[:5] + " W"+deger[-4:]
print(deger)

# 8- abc ifadesini yan yana 3defa yazdır.
x = "abc"
print(x)
x = x*3
print(x)

