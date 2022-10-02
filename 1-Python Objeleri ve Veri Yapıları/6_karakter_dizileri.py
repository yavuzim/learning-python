isim = "Yavuz"
yas = 24
yazdir = 'İsim : '+isim+' '+'Yaş : '+str(yas)
print(yazdir)       # İsim : Yavuz Yaş : 24
print(yazdir[0])    # İ 
print(yazdir[1])    # S
print(len(yazdir))  # 21 - len metodu string metnin uzunluğunu alır.
uzunluk = len(yazdir)
print(yazdir[uzunluk - 1]) # 4
print(yazdir[-1])       # en son karakteri verir. 4
print(yazdir[2:8])  # 2.indeksten başla ve baştan 8'e kadar al. im : Y
print(yazdir[3:])   # 3.indexten başla sonuna kadar git. m : Yavuz Yaş : 24
print(yazdir[2:21:2]) # 2.indeksten başla (2 dahil değil) 21 karakter kadar 2 karakterde bir al.