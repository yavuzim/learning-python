import pandas as pd

df = pd.read_csv("imdb.csv")

sonuc = df.columns
sonuc = df.info

sonuc = df.head(5)
sonuc = df.head(10)
sonuc = df.tail(5)
sonuc = df.tail(10)
sonuc = df["Movie_Title"]
sonuc = df["Movie_Title"].head(5)
sonuc = df[["Movie_Title","Rating"]].head(5)
sonuc = df[["Movie_Title","Rating"]].tail(7)
sonuc = df[5:][["Movie_Title","Rating"]].head()
sonuc = df[df["Rating"]>=8.0][["Movie_Title","Rating"]].head(50)
sonuc = df[(df["YR_Released"]>=2014) & (df["YR_Released"]<=2015)][["Movie_Title","YR_Released"]]
sonuc = df[(df["Runtime"]>=10000) | ((df["Rating"]>= 8) & (df["Rating"]<=9))][["Movie_Title","YR_Released","Runtime","Rating"]]