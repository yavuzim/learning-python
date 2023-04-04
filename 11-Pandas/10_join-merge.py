import pandas as pd

# inner-merge
musteriler = {
        "MusteriId": [1,2,3,4],
        "Ad": ["Cem","Barış","Erkin","Barış"],
        "Soyad": ["Karaca","Manço","Koray","Akarsu"]        
    }
siparisler = {
        "SiparisId": [10,11,12,13],
        "MusteriId": [1,2,5,7],
        "SiparisTarih": ["2003-07-08","1997-09-08","2004-07-12","2005-12-09"]
    }

df_musteriler = pd.DataFrame(musteriler,columns=["MusteriId","Ad","Soyad"])
df_siparisler = pd.DataFrame(siparisler,columns=["SiparisId","MusteriId","SiparisTarih"])
print(df_musteriler)
print(df_siparisler)

# Musteriler ve Siparisleri birleştir.
sonuc = pd.merge(df_musteriler,df_siparisler,how="inner")
print(sonuc)

# Musteriler ve Siparisleri soldan birleştir. musterileri getir, siparişleri getirme.
sonuc = pd.merge(df_musteriler,df_siparisler,how="left")
print(sonuc)
# Musteriler ve Siparisleri sağdan birleştir. siparişlerigetir, musterileri  getirme.
sonuc = pd.merge(df_musteriler,df_siparisler,how="right")
print(sonuc)

###############################################################################

# concat 

musterilerA = {
        "MusteriId": [1,2,3,4],
        "Ad": ["Cem","Barış","Erkin","Barış"],
        "Soyad": ["Karaca","Manço","Koray","Akarsu"]        
    }
musterilerB = {
        "MusteriId": [5,6,7,8],
        "Ad": ["Sagopa","Model","Dr","Sansar"],
        "Soyad": ["Kajmer","XL","Fuchs","Salvo"]        
    }

df_musterilerA = pd.DataFrame(musterilerA,columns=["MusteriId","Ad","Soyad"])
df_musterilerB = pd.DataFrame(musterilerB,columns=["MusteriId","Ad","Soyad"])
print(df_musterilerA)
print(df_musterilerB)

sonuc = pd.concat([df_musterilerA,df_musterilerB]) # default axis=0, satıra göre birleştirir.
sonuc = pd.concat([df_musterilerA,df_musterilerB],axis=1) # sutuna göre birleştirir.
print(sonuc)


