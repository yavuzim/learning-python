dizi = [5,8,9]
print(dizi) # [5, 8, 9]
dizi = ["bir",19,True,12.8]
print(dizi) # ['bir', 19, True, 12.8]

liste1 = ["bir","iki","üç","dört"]
liste2 = ["beş","altı","yedi"]

listeBirlestir = liste1+liste2 # liste1 ve liste2'yi birleştirir listeBirlestir'e atar.
print(listeBirlestir) # ['bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi']

print(len(listeBirlestir)) # liste eleman sayısını verir.

print(listeBirlestir[0]) # listenin 0. elamanına erişir.

kullanici1 = ["Kemal",24]
kullanici2 = ["Yavuz",255]
kullanicilar =[kullanici1,kullanici2]
print(kullanicilar) # [['Kemal', 24], ['Yavuz', 255]]
print(kullanicilar[1]) # ['Yavuz', 255]
print(kullanicilar[1][0]) # Yavuz