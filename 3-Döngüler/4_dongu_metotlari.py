# range()

for item in range(10): # 0' dan 10'a kadar sayıları listeler. (0 dahil,10 dahil değil.)
    print(item)
    
print("----------------------------------")

for item in range(50,100,10): # 50'den başla 100'e kadar 10'ar arttır. (50 dahil, 100 dahil değil.)
    print(item)

print("----------------------------------")

print(list(range(5,100,20))) # [5, 25, 45, 65, 85]

print("###################################################################")

# enumerate()

deger = "Merhaba Dünya"

for item in enumerate(deger):
    print(item)

for indeks,harf in enumerate(deger):
    print(f"indeks : {indeks} - harf : {harf}")

print("###################################################################")

# zip()

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [100,200,300,400,500]

print(list(zip(list1,list2))) # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'), (5, 'e')]
print(list(zip(list1,list2,list3))) # [(1, 'a', 100), (2, 'b', 200), (3, 'c', 300), (4, 'd', 400), (5, 'e', 500)] 

for item in zip(list1,list2,list3):
    print(item)

for a,b,c in zip(list1,list2,list3):
    print(f"a : {a} - b : {b} - c : {c}")