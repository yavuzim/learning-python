import pandas as pd

veri = pd.read_csv("nba.csv")
print(veri)
print(veri.columns)
veri.dropna(inplace=True)

sonuc = veri["Name"].str.upper() # Name kolonundaki bütün verileri büyük harfe çevirir.
sonuc = veri["Name"].str.lower() # Name kolonundaki bütün verileri küçük harfe çevirir.
print(sonuc)

# index adındaki yeni sutunumuza o satırdaki Name sutununun a harfinin indeksini yazdırdık.
veri["index"] = veri["Name"].str.find("a")
# Name sutununda Jordan olan veriler varsa True yoksa False yazar.
sonuc = veri.Name.str.contains("jordan")
# Name sutununda Jordan olan verileri getir.
sonuc = veri[veri.Name.str.contains("Jordan")]
# Team sutunundaki verilerin boşluk karakterleri yerine çizgi ekler
sonuc = veri["Team"].str.replace(' ','-')
# Name kolonunu ad ve soyad olarak ayırma.
veri[["Ad","Soyad"]] = veri["Name"].loc[veri["Name"].str.split().str.len()==2].str.split(expand=True)
print(veri.head(10))