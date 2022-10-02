github = "https://www.github.com/yavuzim"
mesaj = "Python ile Derin Öğrenme"

# 1- ' Hello World ' karakter dizisinin baş ve sonundaki boşluk karakterini sil.
helloWorld = " Hello World "
print(helloWorld.strip())   # sağ ve sol
print(helloWorld.lstrip())  # sol
print(helloWorld.rstrip())  # sağ

# 2- www.github.com/yavuzim içindeki yavuzim bilgisi hariç her karakteri sil.
x = github[-7:].lstrip("/:com")
print(x)

# 3- mesaj değişkenin içindeki karakterlerin hepsini küçük ve büyük harf yap.
kucukHarf = mesaj.lower()
buyukHarf = mesaj.upper()
print(kucukHarf)
print(buyukHarf)

# 4- github içinde kaç tane a karakteri vardır ?
ara = github.count("a")
print(ara)

# 5- gihub www ile başlayıp com ile bitiyor mu?
print(str(mesaj.startswith("www"))+" - "+str(mesaj.endswith("com")))