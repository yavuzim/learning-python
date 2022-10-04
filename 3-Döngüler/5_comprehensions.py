for x in range(10):
    print(x)

sayilar = [x for x in range(10)]
print(sayilar) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("---------------------------------")

sayilar = []
for i in range(10):
    sayilar.append(i)
print(sayilar)

print("---------------------------------")

for x in range(10):
    print(x**2)

sayilar = [x**2 for x in range(10)]
print(sayilar)

print("---------------------------------")

sayilar = [x**2 for x in range(10) if x%3 == 0]
print(sayilar) # [0, 9, 36, 81]