import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4]
plt.plot(x) 
plt.show()

######################################################################

x = [1,2,3,4]
y = [1,4,9,16]

plt.plot(x,y) # (1,1) (2,4) (3,9) (4,16)
plt.plot(x,y,"--g") # çizgi şeklini belirler.
plt.plot(x,y,"o-r") # çizgi şeklini belirler.
#plt.plot(x,y,color="blue",linewidth=5) # çizgi rengi ve çizgi kalınlığı

plt.axis([0,6,0,20]) # x'in min degeri 0, max degeri 6. y'nin min degeri 0 max degeri 20.

plt.title("Grafik Başlığı") # Grafiğe başlığı.
plt.xlabel("x ekseni") # x ekseninin adı.
plt.ylabel("y ekseni") # y ekseninin adı.
plt.show()

######################################################################

x = np.linspace(0,2,100)

plt.plot(x,x,label="Düzgün",color="red")
plt.plot(x,x**2,label="Karesel",color="yellow")
plt.plot(x,x**3,label="Kübik")

plt.xlabel("x ekseni")
plt.ylabel("y ekseni")

plt.title("Grafik Başlığı")

plt.legend()
plt.show()
