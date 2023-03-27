a = int(input("a : "))
b = int(input("b : "))

if a>b:
    mesaj = "a sayısı b sayısından büyük."
elif a<b:
    mesaj = "b sayısı a sayısından büyük."
else:
    mesaj = "a ve b sayıları eşittir."
print(mesaj)