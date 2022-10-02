meyveler = {"Portakal","Elma","Muz"}
print(meyveler)
# print(meyveler[1]) indekslenemez!

# Elemanlarına döngü ile ulaşırız
for x  in meyveler :
    print(x)

# Eklenen elemanlar rastgele yerlere eklenir.
meyveler.add("Çilek") # Yeni eleman ekler.
print(meyveler)

meyveler.update(["Ananas","Üzüm"]) # Yeni eleman ekler.
print(meyveler)

meyveler.add("Elma") # Eklenen eleman varsa ekleme yapmaz.
print(meyveler)
 
meyveler.update(["Ananas","Üzüm"]) # Eklenen eleman varsa ekleme yapmaz.
print(meyveler)

meyveler.remove("Elma") # Elmayı siler
print(meyveler)

meyveler.pop() # Herhangi bir elemanı siler.
print(meyveler)

dizi = [1,2,1,9,6,5,6,1]
print(dizi)
print(set(dizi)) # Tekrarlanan elemanaları liste içerisinden gider. {1, 2, 5, 6, 9}


