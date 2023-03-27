'''
        Otopark Ücret Tarifesi
        Bir otoparkın ücret tarifesi aşağıdaki gibidir:

          *  1 saate kadar: 5 TL
          *  1-5 saat arası: Saat başı 4 TL
          *  5 saatten fazla: Saat başı 3 TL
'''

ucret = 0
kalinanSaat = input("Kalınan Saat : ")
kalinanSaat = float(kalinanSaat)

if kalinanSaat<1:
    ucret = kalinanSaat*5
elif kalinanSaat>=1 and kalinanSaat<5:
    ucret = kalinanSaat*4
else:
    ucret = kalinanSaat*3

print("Otopark Ücreti : ",ucret)