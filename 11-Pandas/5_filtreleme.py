import pandas as pd
import numpy as np

data = np.random.randint(10,100,75).reshape(15,5)
df = pd.DataFrame(data,columns=["Sayi1","Sayi2","Sayi3","Sayi4","Sayi5"])

sonuc = df.columns # kolon başlığını liste şeklinde getirir.
sonuc = df.head(5) # ilk 5 satır getir.
sonuc = df.head(10) # ilk 10 satır getir.
sonuc = df.tail(5) # sondan 5 satır getir.
sonuc = df.tail(10) # sondan 10 satır getir.
sonuc = df["Sayi1"].head # Sayi1 kolonundaki verileri getirir.
sonuc = df.Sayi1.head # Sayi1 kolonundaki verileri getirir.
sonuc = df["Sayi1"].head(5) # Sayi1 kolonundaki ilk 5 veriyi getirir.
sonuc = df["Sayi1"].tail(5) # Sayi1 kolonundaki son 5 veriyi getirir.
sonuc = df[["Sayi1","Sayi2"]].head(5) # Sayi1 ve Sayi2 kolonundaki ilk 5 veri.
sonuc = df[5:15][["Sayi1","Sayi2"]].head(5) # 5-15 satırları arasında Sayi1 ve Sayi2 kolonundaki 5 veriyi getir.

sonuc = df > 50 # 50 den büyük sutunlara True, aksi False verir.
sonuc = df[df>50] # 50 den büyük olanları değiştirmez, küçük olanları NaN yapar.
sonuc = df[df["Sayi1"]>50][["Sayi1","Sayi2"]]

print(sonuc)