import matplotlib.pyplot as plt
import numpy as np

yil = [2011,2012,2013,2014,2015]

oyuncu1 = [8,9,12,7,1]
oyuncu2 = [7,4,15,8,6]
oyuncu3 = [12,18,4,9,3]

# Stack Plot
plt.plot([],[],color="y",label="oyuncu1")
plt.plot([],[],color="r",label="oyuncu2")
plt.plot([],[],color="b",label="oyuncu3")

plt.stackplot(yil,oyuncu1,oyuncu2,oyuncu3,colors=["y","r","b"])

plt.title("Yıllara Göre Atılan Goller")
plt.xlabel("Yıl")
plt.ylabel("Gol")

plt.legend() 

plt.show()

# Pasta Grafiği
gol_tipleri = "Penaltı","Kaleye Atılan Şut","Serbest Vuruş"

goller = [12,35,7]
renkler = ["r","g","b"]

plt.pie(goller,labels=gol_tipleri,colors=renkler,shadow=True,explode=(0.05,0.05,0.05), autopct="%1.1f%%") # explode, pastalar arası mesafe.

plt.show()

# Sutun Grafiği
plt.bar([0.25,1.25,2.25,3.25,4.25],[50,40,70,80,20],label="BMW",width=.5)
plt.bar([0.75,1.75,2.75,3.75,4.75],[80,20,20,50,60],label="Audi",width=.5)

plt.legend()

plt.xlabel("Gün")
plt.ylabel("Mesafe (km)")
plt.title("Araç Bilgileri")

plt.show()

# Histogram Grafiği
yaslar = np.array(np.random.randint(0,101,100))
yas_gruplari = [0,10,20,30,40,50,60,70,80,90,100]

plt.hist(yaslar,yas_gruplari,histtype="bar",rwidth=0.8)

plt.xlabel("Yaş Grupları")
plt.ylabel("Kişi Sayısı")
plt.title("Histogram")

plt.show()