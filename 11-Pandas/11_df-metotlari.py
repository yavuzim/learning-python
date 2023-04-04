import pandas as pd
import numpy as np

veri = {
            "Sutun1": [2,4,6,8,10,8,2],
            "Sutun2": [20,40,60,80,100,80,40],
            "Sutun3": ["abc","bca","ade","cba","dea","bca","cba"]
}

df = pd.DataFrame(veri)

# Tekrarlanmayan elemanları getir.
sonuc = df["Sutun1"].unique()
sonuc = df["Sutun2"].unique()
sonuc = df["Sutun3"].unique()

# Eleman sayısını gösterme. Tekrarlanan elemanlar bir kez sayılır.
sonuc = df["Sutun1"].nunique()
sonuc = df["Sutun2"].nunique()
sonuc = df["Sutun3"].nunique()

# Elemanların kaç kez tekrarlandığını gösterir.
sonuc = df["Sutun1"].value_counts()
sonuc = df["Sutun2"].value_counts()
sonuc = df["Sutun3"].value_counts()

# Sutundaki verileri 2 ile çarpma.
sonuc = df["Sutun1"] * 2
sonuc = df["Sutun2"] * 2
sonuc = df["Sutun3"] * 2

# Metoda parametre olarak gönderme.
def kareal(x):
    return x**2
sonuc = df["Sutun1"].apply(kareal)

# Lambdaya parametre olarak gönderme.
ikiyebol = lambda x : x/2
sonuc = df["Sutun1"].apply(ikiyebol)

# Sutundaki string karakterlerin uzunluğunu alma.
sonuc = df["Sutun3"].apply(len)

# Sutun sayılarına bakma.
sonuc = len(df.columns)

# index bilgilerini getirme.
sonuc = df.index

# Satır sayısını getirme.
sonuc = len(df.index)

# df bilgilerini getirme.
sonuc = df.info

# Sıralama yapma.
sonuc = df.sort_values("Sutun2") # küçükten büyüğe a->z
sonuc = df.sort_values("Sutun2",ascending=False) # büyükten küçüğe z->a

veri = {
    "Ay": ["Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan","Mayıs","Haziran","Nisan"],
    "Kategori": ["Elektronik","Elektronik","Elektronik","Kitap","Kitap","Kitap","Giyim","Giyim","Giyim"],
    "Gelir": [20,30,15,14,32,42,12,36,52]
}

df = pd.DataFrame(veri)

# Tekrarlayan alanları düzenleme.
df = df.pivot_table(index="Ay",columns = "Kategori",values="Gelir")

print(df)

























