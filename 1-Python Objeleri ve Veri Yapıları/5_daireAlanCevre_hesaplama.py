'''
    Daire Alan  : πr²
    Daire Çevre : 2πr

    * Yarı çapı verilen bir dairenin alanını ve çevresini
     hesaplayınız. (π : 3.14)

'''

pi = 3.14
r = input("Yarı Çap : ")
r = int(r)

alan = pi*(r**2)
cevre = 2*pi*r

print("Alan : ",alan)
print("Çevre : ",cevre)

