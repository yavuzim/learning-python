import pandas as pd
from numpy.random import randn

df = pd.DataFrame(randn(3,3),index=["A","B","C"],columns=["Sutun1","Sutun2","Sutun3"])
print(df)

sonuc = df["Sutun1"] # Sutun1 kolonunu getirir.

sonuc = type(df["Sutun1"]) # Sutun1 kolonunun tipini getirir.

sonuc = df[["Sutun1","Sutun2"]] # Birden fazla kolon getirme.

sonuc = df.loc["A"] # A satırı.
sonuc = df.iloc[0] # A satırına denk gelir.

sonuc = df.loc["A","Sutun1"] # A satırı Sutun1 kolonu.

sonuc = df.loc[:,"Sutun1"] # sadece bir kolon seçilir.

sonuc = df.loc[:,["Sutun1","Sutun2"]] # sadece iki kolon seçilir.

sonuc = df.loc[:,"Sutun1":"Sutun3"] # Sütun1 ve Sütun3 kolonları arasındaki kolonları getirir. (Sutun1-Sutun3 dahil)

sonuc = df.loc[:,:"Sutun3"] #  Başlangıçtan itibaren Sutun3 e kadar git. (Sütun1-Sütun3 dahil)

sonuc = df.loc["A":"B",:"Sutun3"] #  Başlangıçtan itibaren Sutun3 e kadar A ve B satırlatını al. (Sutun1-Sutun3 dahil)

sonuc = df.loc["A","Sutun2"] # A satırı Sutun2 sutunundaki veri.

sonuc= df.loc[["A","B"],"Sutun2"] # A ve B satırları Sutun2 sutunundaki veriler.

df["Sutun4"] = pd.Series(randn(3),["A","B","C"]) # yeni kolon ekleme.
df["Sutun5"] = df["Sutun1"] + df["Sutun2"] # Sutun1 ve Sutun2 kolonlarının toplamı Sutun5 de yazar.

sonuc = df.drop("Sutun5",axis=1) # orijinal df üzerinden silmez.
df.drop("Sutun5",axis=1, inplace=True) # orijinal df üzerinden siler.