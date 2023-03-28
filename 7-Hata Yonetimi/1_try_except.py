try: # x veya y hatalı girilirse except blokları çalışır.
    x = int(input("x : "))
    y = int(input("y : "))
except ValueError: # syntax hatasında çalışır.
    print("Karakter girmeyiniz!")
except ZeroDivisionError: # 0'a bölme hatasında çalışır.
    print("0'a bölünemez!")
else: # except bloklarına girmediğinde çalışır.
    print("(x/y) = ",x/y)
    print("İşlem Başarılı")
finally: # her try'ın sonunda çalışır.
    print("İşlem Sonlandı!")