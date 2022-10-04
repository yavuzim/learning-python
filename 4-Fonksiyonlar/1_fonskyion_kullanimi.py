def cizgi():
    print("##################################")

def hello():
    print("Hello")

hello()

cizgi()

def yazdir(mesaj):
    print(mesaj)

yazdir("Merhaba Python")

cizgi()

def topla(sayi1,sayi2):
    return sayi1+sayi2

toplam = topla(8,9)
print(toplam)

cizgi()

def degistir(n):
    n[0] = "Ankara"

sehirler = ["Elazığ","Hatay"]
print(sehirler)
degistir(sehirler)
print(sehirler)

cizgi()

def add(*parametreler): # * tüm parametreleri alır
    print(f"Tipi : {type(parametreler)}")
    return sum(parametreler)

print(add(10,20))

cizgi()

def kullanici(**argumanlar):
    print(f"Tipi : {type(argumanlar)}")
    for key,value in argumanlar.items():
        print(f"{key} : {value} ")

kullanici(name="Kemal Yavuz",yas=24,sehir="Hatay")