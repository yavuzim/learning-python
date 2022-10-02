 # 1- 'Bmw,Mercedes,Opel,Mazda' elemanlarına sahip liste oluştur.

arabalar = ["Bmw","Mercedes","Opel","Mazda"]
print(arabalar)

 # 2- Liste kaç elemanlıdır?

print(len(arabalar))

 # 3- Listenin ilk ve son elemanı nedir.

ilkEleman = arabalar[0]
uzunluk = len(arabalar) - 1
sonEleman = arabalar[uzunluk]
print(ilkEleman+" - "+sonEleman)

 # 4- Mazda değerini Toyota değeri ile değiştir.

arabalar[uzunluk] = "Toyota"
print(arabalar)

 # 5- Mercedes listenin bir elemanı mıdır?

ara = arabalar.index("Mercedes")
print(ara)

 # 6- Listenin -2 indeksindeki değer nedir?

print(arabalar[-2])

 # 7- Listenin ilk 3 elemanını alın.

print(arabalar[0:3])

 # 8-Listenin son 2 elemanı yerine 'Toyota' ve 'Renault' değerini ekleyin.

arabalar[uzunluk] = "Toyota"
arabalar[uzunluk-1] = "Renault"
print(arabalar)

 # 9-Listenin üzerine 'Audi' ve 'Nissan'  değerlerini ekleyin.

arabalar.append("Audi")
arabalar.append("Nissan")
print(arabalar)

 # 10- Listenin son elemanını silin.

uzunluk = len(arabalar) - 1
arabalar.remove(arabalar[uzunluk])
print(arabalar)

 # 11- Listenin elemanlarını tersten yaz.

print(arabalar[::-1])

 # 12- Aşağıdaki verileri bir liste içinde sakla.

