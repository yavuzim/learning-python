# dictionary oluştrma

kimlik = {
    "isim": "Kemal Yavuz",
    "soyisim": "İMER",
    "yas": 24,
    "dersler": ["Algoritma ve Programlama","Sayısal Tasarım","Sayısal Analiz"]
    }

# Ekrana yazdır.
print(kimlik)

# İsim bilgisini ekrana yaz.
print(kimlik["isim"]) 
print(kimlik.get("dersler"))

# dictionary uzunluğu.
print(len(kimlik))

# keys adlarını yaz.
print(kimlik.keys())

# değerleri yaz.
print(kimlik.values())

# listedeki verileri tuple olarak yaz.
print(kimlik.items())

# yeni veri ekle.
kimlik["okul"]="Fırat Üniversitesi"
print(kimlik)

# yaş değerini güncelle.
kimlik.update({"yas":25}) #♠ ya da kimlik["yas"] = 25
print(kimlik)

# son ögeyi kaldır.
kimlik.popitem()
print(kimlik)

# yas ögesini kaldır.
del kimlik["yas"]
print(kimlik)

# dictionaryi içeriğini tamamen sil.
kimlik.clear()
print(kimlik)

# dictionaryi sil
del kimlik














