# float'tan int'te

a = 5.2
b = int(a)
print(b) # 5

# int'ten float'a
a = 5
b = float(a)
print(b) # 5.0

# Örnek

sayi1 = input("1. Sayı : ") # String değer olarak alır.
sayi2 = input("2. Sayı : ") # String değer olarak alır.
toplam = sayi1 + sayi2      # sayi1 = 45 sayi2 = 2
print("Toplam : ",toplam)   # Toplam : 452

x = input("x : ")           # x : 5
y = input("y : ")           # y : 9
tplm = int(x) + int(y)      # inputtan alınan değerler int veri tipine dönüştürüldü.
print("Toplam : ",tplm)     # Toplam : 14