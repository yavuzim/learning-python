def sifreKontrol(sifre):
    import re
    if len(sifre) < 8:
        raise Exception("Parola En Az 8 Karakter Olmalıdır.")
    elif not re.search("[a-z]",sifre):
        raise Exception("Parola Küçük Harf İçermelidir.")
    elif not re.search("[A-Z]",sifre):
        raise Exception("Parola Büyük Harf İçermelidir.")
    elif not re.search("[0-9]",sifre):
        raise Exception("Parola Rakam Harf İçermelidir.")
    elif not re.search("[_@$]",sifre):
        raise Exception("Parola Alpha Numeric Karakter İçermelidir.")
    elif re.search("\s",sifre):
        raise Exception("Parola Boşluk Karakteri İçermemelidir.")

sifre = "12345678aA_$"

try:
    sifreKontrol(sifre)
except Exception as ex:
    print(ex)
else : print("Geçerli Praola.")

    