import pandas as pd
import numpy as np

personeller  = {
        "Çalışan": ["Kemal Yavuz İMER","Koray GÜLER","Ahmet MÜJDE", "Alican DARI"],
        "Departman": ["İnsan Kaynakları","Bilgi İşlem","Muhasebe","İnsan Kaynakları"],
        "Yaş": [24,24,24,22],
        "Semt":["Kadıköy","Tuzla","Pendik","Kadıköy"],
        "Maaş": [5000,5500,3800,5000]
    }

df = pd.DataFrame(personeller)


# Toplam Maaş.
toplamMaas = df["Maaş"].sum()


# Verileri gruplama.
sonuc = df.groupby("Departman").groups
sonuc = df.groupby(["Departman","Semt"]).groups


for isim,grup in df.groupby("Semt"):
    print(isim)
    print(grup)
    print("-------------------------------------")
    
print("#######################################################")

for isim,grup in df.groupby("Departman"):
    print(isim)
    print(grup)
    print("-------------------------------------")

print("#######################################################")  

# Sadece Kadıköy bilgisine sahip olanları getirme.
sonuc = df.groupby("Semt").get_group("Kadıköy")
sonuc = df.groupby("Departman").get_group("Muhasebe")

# Departmana göre yaş ve maaş toplamlarını verir.
sonuc = df.groupby("Departman").sum()
# Departmana göre yaş ve maaş ortalamarını verir.
sonuc = df.groupby("Departman").mean()
# Departmana göre maaş ortalamarını verir.
sonuc = df.groupby("Departman")["Maaş"].mean()
# Semte göre yaş ortalamalarını verir.
sonuc = df.groupby("Semt")["Yaş"].mean()
# Semtlere göre çalışanları getirir.
sonuc = df.groupby("Semt")["Çalışan"].sum()
# Semtlere göre çalışan sayısını getirir.
sonuc = df.groupby("Semt")["Çalışan"].count()
# Departmana göre en büyük maaşı getirme.
sonuc = df.groupby("Departman")["Maaş"].max()
# Muhasebe bölümündeki maksimum maaşı verisini getirme.
sonuc = df.groupby("Departman")["Maaş"].max()["Muhasebe"]
# Departmana göre ortalama hesabı yapma.
sonuc = df.groupby("Departman").agg(np.mean)
# Departmana göre Maaş da toplam,min,max ve ortalama hesabı yapar.
sonuc = df.groupby("Departman")["Maaş"].agg([np.sum,np.max,np.min,np.mean])
# Muhasebeye göre Maaş da toplam,min,max ve ortalama hesabı yapar.
sonuc = df.groupby("Departman")["Maaş"].agg([np.sum,np.max,np.min,np.mean]).loc["Muhasebe"]