try:
    x = int(input("x : "))
    y = int(input("y : "))
    print(f"x/y = {x/y}")
except ZeroDivisionError:
    print(f"y>0 olmalı!")
except ValueError:
    print("Hatalı Değer Girdiniz!")
else:
    print("Program Sorunsuz Bitti.")


