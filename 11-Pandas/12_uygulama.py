import pandas as pd

df = pd.read_csv("nba.csv")
print(df)
print(df.columns)
print("#####################################################################")
# İlk 10 kaydı getiriniz.
sonuc = df.head(10)

# Toplam kayıt sayısını getir.
sonuc = len(df.index)

# Tüm oyuncuların toplam maaş ortalaması.
sonuc = df["Salary"].mean()

# En yüksek maaşı alan oyuncu.
sonuc = df["Salary"].max()

# En yüksek maaşı alan oyuncu.
sonuc = df[df["Salary"]==df["Salary"].max()][["Name","Team","Salary"]]

# Yaşı 20-25 arasında olan oyuncuların isim ve oynadıkları takım isimleri.
sonuc = df[(df["Age"]>=20) & (df["Age"]<=25)][["Name","Age","Team"]]

# Yaşı en büyük olan oyuncu/oyuncular.
sonuc = df[df["Age"]==df["Age"].max()][["Name","Team","Age"]]

# Yaşı en küçük olan oyuncu/oyuncular.
sonuc = df[df["Age"]==df["Age"].min()][["Name","Team","Age"]]

# "John Holland" isimli oyuncunun oynadığı takım.
sonuc = df[df["Name"]=="John Holland"][["Name","Team"]]
sonuc = df[df["Name"]=="John Holland"]["Team"].iloc[0] # veriyi str olarak verir.

# Takımlara göre oyuncuların ortalama maaş bilgileri.
sonuc = df.groupby("Team").mean()["Salary"]

# Kaç farklı takım mevcut?
sonuc = len(df.groupby("Team"))

# Her takımda kaç oyuncu var?
sonuc = df.groupby("Team").count()["Name"]
sonuc = df["Team"].value_counts()

# İsmi içinde "and" geçen kayıtlar.
df = df.dropna() # NaN olan satırlar silindi.
sonuc = df[df["Name"].str.contains("and")]

print(sonuc)

















