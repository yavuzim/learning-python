sayilar = [1,3,5,7,9,12,19,21]

# 1- Sayılar listesindeki hangi sayılar 3'ün katıdır?

for item in sayilar:
    if item%3==0:
        print(item)

# 2- Sayılar listesindeki sayıların toplamı kaçtır?
toplam = 0
for item in sayilar:
    toplam+=item
print(toplam)

# 3- Sayılar listesindeki sayıların karesini alınız.

for item in sayilar:
    print(item**2)

#####################################################################################

sehirler = ["Kocaeli","İstanbul","Ankara","İzmir","Rize","Hatay","Elazığ","Kırkraleli","Hakkari"]

# 4- Şehirlerden hangileri en fazla 5 karakterlidir?

for item in sehirler:
    if len(item)<=5:
        print(item)

#####################################################################################

urunler = [
    {"name" : "Samsung S6", "price" : "5000"},
    {"name" : "Samsung S7", "price" : "8000"},
    {"name" : "Samsung S8", "price" : "9000"},
    {"name" : "Samsung S9", "price" : "10000"},
    {"name" : "Samsung S10", "price" : "15000"}
]

# 5- Ürünlerin fiyatları toplamı nedir?
toplam = 0
for item in urunler:
    toplam+=int(item["price"])
print(toplam)

# 6- Ürünlerden fiyatı en fazla 9000 olan ürünleri gösteriniz.
for item in urunler:
    if int(item["price"])<=9000:
        i = item
        print(i)
        