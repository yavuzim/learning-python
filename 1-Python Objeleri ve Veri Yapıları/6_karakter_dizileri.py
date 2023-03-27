isim = "Yavuz"
yas = 24
ekranaYaz = "İsim : "+isim+" - Yaş : "+str(yas)
print(ekranaYaz) # İsim : Yavuz - Yaş : 24
print(ekranaYaz[0])    # İ
print(ekranaYaz[1])    # S
print(len(ekranaYaz))  # 23 - len metodu string metnin uzunluğunu alır. Boşluklarıda karakter olarak sayar.
uzunluk = len(ekranaYaz)
print(ekranaYaz[uzunluk - 1]) # 4
print(ekranaYaz[-1])       # en son karakteri verir. 4
print(ekranaYaz[2:9])      # 2.indeksten başla ve baştan 9 karakter al. im : Ya
print(ekranaYaz[3:])       # 3.indexten başla sonuna kadar al. m : Yavuz - Yaş : 24
print(ekranaYaz[:16])      # Baştan başla 16 karakter al.
print(ekranaYaz[2:23:2]) # 2.indeksten başla 23 karakter kadar git ve 2 karakterde bir al.