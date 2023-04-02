import pandas as pd

# dict ile Tablo oluşturma 1.
s1 = pd.Series([3,2,0,1])
s2 = pd.Series([0,3,7,2])
veri = dict(elma = s1, portakal = s2)
df = pd.DataFrame(veri)

###################################################################

# dict ile Tablo oluşturma 2.
veriler = [{
    "İsim" : "Kemal",
    "Soyisim" : "İMER",
    "Dersler" : ["Otomata","Veri Yapıları","Sayısal Analiz"]
    },{
       "İsim" : "Alp",
    "Soyisim" : "KAYA",
    "Dersler" : ["Elektrik Devreleri","Veri Yapıları","Sayısal Tasarım"]
       }]
df = pd.DataFrame(veriler)

###################################################################

# dict ile Tablo oluşturma 3.
veriler = {"İsimler" : ["Yavuz","Yeşim"],"Dersler" : ["Otomata","Veri Yapıları"]}
df = pd.DataFrame(veriler)
df = pd.DataFrame(veriler,index = [1,2])

###################################################################

# matris ile Tablo oluşturma.
veriler = [["Otomata","BA",79],["Veri Yapıları","BB",65],["Algortima Programlama","BA",78],["Sayısal Yöntemler","AA",85]]
df = pd.DataFrame(veriler)
df = pd.DataFrame(veriler,columns = ["Dersler","Harf","Notlar"])
df = pd.DataFrame(veriler,columns = ["Dersler","Harf","Notlar"],index=[101,201,102,404])
df = pd.DataFrame(veriler,columns = ["Dersler","Harf","Notlar"],index=[101,201,102,404],dtype = float)


