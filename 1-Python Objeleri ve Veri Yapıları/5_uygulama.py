'''
    Dairenin Alanını ve Çevresini Hesaplama
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

'''
    Karenin Alanını ve Çevresini Hesaplama
    Kare Alan : a*a
    Kare Çevre : a*4

'''

a = input("Kenar : ")
kareAlan = int(a)**2 # veya kareAlan = int(a)*int(a)
kareCevre = int(a)*4
print("Alan : ",kareAlan)
print("Çevre : ",kareCevre)