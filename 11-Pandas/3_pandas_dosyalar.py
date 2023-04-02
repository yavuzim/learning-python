import pandas as pd

df = pd.read_json("sinif_bilgisi.json")
df = pd.read_excel("dersler.xlsx")
print(df)