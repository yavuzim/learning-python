sayi = input("Sayı : ")
sayi = int(sayi)

cikti = ""

if sayi<2: cikti = f"{sayi} sayısı asal değildir."
else:
    for deger in range(2,sayi,1):
        if sayi%deger == 0:
            cikti = f"{sayi} sayısı asal değildir."
            break
        else : cikti = f"{sayi} sayısı asal sayıdır."

print(cikti)
            