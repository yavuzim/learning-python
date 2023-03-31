import pandas as pd
import numpy as np

# Tamsayı dizisi, datatype: int64
sayilar = [10,20,30,40,50]
pandas_serileri = pd.Series(sayilar)
print(pandas_serileri)

# Karakter dizisi, datatype: object
harfler = ['a','b','c','d']
pandas_serileri = pd.Series(harfler)
print(pandas_serileri)

# Farklı veri tipleri, datatype: object
veriler = ['a','b','c','d',20,25.5]
pandas_serileri = pd.Series(veriler)
print(pandas_serileri)

# Tek bir eleman tanımlama.
a = 5
b = "kemal"
pnd1 = pd.Series(a) # datatype: int64
pnd2 = pd.Series(b) # datatype: object
print(pnd1)
print(pnd2)

# Key isimlerini değiştirme. Series() metodunun 2.parametresi key adlarını içerir.
arr = [45,87,96,12]
pnds = pd.Series(arr,["a","b","c","d"])
print(pnds)

# datayı numpy üzerinden oluşturma.
sayilar = np.random.randint(10,100,6)
pandasSeries = pd.Series(sayilar)
print(pandasSeries)

# pandas listesi içindeki elemanlara erişme.
sayilar = np.arange(10,100,10)
pandas_serileri = pd.Series(sayilar)
sonuc = pandas_serileri[0]
sonuc = pandas_serileri[:2]
sonuc = pandas_serileri[[0,1,2]]
print(sonuc)




















