# key - value şeklinde çalışır.
# 31 => Hatay 23 => Elazığ

# Liste
sehirler = ["Hatay","Elazığ"]
plakalar = [31,23]

print(plakalar[sehirler.index("Hatay")]) # 31

#####################################################################

# Dictionary
plakalar = {"Hatay" : 31, "Elazığ" : 23}
print(plakalar) # {'Hatay': 31, 'Elazığ': 23}

print(plakalar["Hatay"]) # 31

plakalar["Ankara"] = 6
print(plakalar["Ankara"]) # 6

# ---------------------------------------------------------

kullanicilar = {
    "Kemal Yavuz İMER" : {
        "yas" : 24,
        "rol" : ["admin","user"],
        "email" : "kyavuzimer@gmail.com",
        "adres" : "Elazığ"
    },
    "Taner Çolak" : {
        "yas" : 23,
        "rol" : ["user"],
        "email" : "taner@gmail.com",
        "adres" : "Hatay"
    }
}

print(kullanicilar["Kemal Yavuz İMER"]["email"])
print(kullanicilar["Taner Çolak"]["rol"])


