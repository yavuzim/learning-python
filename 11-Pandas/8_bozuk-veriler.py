import pandas as pd
import numpy as np

veri = np.random.randint(10,100,15).reshape(5,3)
df = pd.DataFrame(veri, index = ["a","c","e","f","h"], columns =["Sutun1","Sutun2","Sutun3"])
df = df.reindex(["a","b","c","d","e","f","g","h"])
print(df)

sonuc = df.drop("Sutun1",axis=1)
sonuc = df.drop(["Sutun1","Sutun2"],axis=1)
sonuc = df.drop("a",axis=0)
sonuc = df.drop(["a","b"],axis=0)

sonuc = df.isnull() # NaN alanlar True değer içerenler False döner.
sonuc = df.notnull() # NaN alanlar False değer içerenler True döner.
sonuc = df.isnull().sum() # NaN olanların sayısını dönderir.
sonuc = df.notnull().sum() # NaN olmayanların sayısını dönderir.
sonuc = df["Sutun1"].isnull().sum() # Sutun1'deki NaN verilerinin sayısı.
sonuc = df["Sutun1"].notnull().sum() # Sutun1'deki NaN olmayan verilerin sayısı.

yeniSutun = [np.nan,30,np.nan,51,np.nan,30,np.nan,10]
df["Sutun4"] = yeniSutun
print(df)

sonuc = df[df["Sutun1"].isnull()] # Sutun1 deki NaN değerleri getir.
sonuc = df[df["Sutun1"].isnull()]["Sutun1"] # Sutun1 deki NaN değerleri getir. Ekranda sadece Sutun1 görünsün.
sonuc = df[df["Sutun1"].isnull()][["Sutun1","Sutun2"]] # Sutun1 deki NaN değerleri getir. Ekranda sadece Sutun1 ve Sutun2 görünsün.

sonuc = df.dropna() # Satıra göre silme işlemi yapar. Satırda NaN varsa siler. varsayılan olarak axis=1
sonuc = df.dropna(axis=0) # Sutuna göre silme işlemi yapar. Sutunda NaN varsa siler.
sonuc = df.dropna(how="any") # Bir tanesi NaN olması durumunda siler.
sonuc = df.dropna(how="all") # Satırda hepsi NaN ise satırı siler.
sonuc = df.dropna(subset=["Sutun1","Sutun4"],how="all") # Sutun1 ve Sutun2 de NaN varsa o satırı siler.
sonuc = df.dropna(subset=["Sutun1","Sutun4"],how="any") # Sutun1 veya Sutun2 de NaN varsa o satırı siler.
sonuc = df.dropna(thresh=2) # NaN değeri harici 2 tane normal veri varsa getir.
sonuc = df.dropna(thresh=4) # NaN değeri harici 4 tane normal veri varsa getir.

sonuc = df.fillna(value="veri yok") # NaN olan alanlara veri yok yazar.
sonuc = df.fillna(value=1) # NaN olan alanlara 1 yazar.

sonuc = df.sum() # # df deki toplam sayıları sutun sutun verir.
sonuc = df.sum().sum() # df deki toplam sayıları verir.
sonuc = df.size # eleman sayısı verir.
sonuc = df.isnull().sum().sum() # NaN değerlerinin toplamı.

# NaN olmayan verilen ortalamasını NaN olan verilerin yerine yaz.
def ortalama(df):
    toplam = df.sum().sum()
    adet = df.size - df.isnull().sum().sum()
    return toplam/adet
sonuc = df.fillna(value=ortalama(df))