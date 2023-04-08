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

plt.plot(x,x,label="Doğrusal",color="red")
plt.plot(x,x**2,label="Karesel",color="yellow")
plt.plot(x,x**3,label="Kübik")

plt.xlabel("x ekseni")
plt.ylabel("y ekseni")

plt.title("Grafik Başlığı")

plt.legend()
plt.show()

######################################################################

x = np.linspace(0,2,100)

fig,axs = plt.subplots(3)

axs[0].plot(x,x,color="red")
axs[0].set_title("Doğrusal")

axs[1].plot(x,x**2,color="blue")
axs[1].set_title("Karesel")

axs[2].plot(x,x**3,color="yellow")
axs[2].set_title("Kübik")

plt.tight_layout()

plt.show()

######################################################################

x = np.linspace(0,2,100)

fig,axs = plt.subplots(2,2)
fig.suptitle("Grafik Ana Başlığı")

axs[0,0].plot(x,x,color="red")
axs[0,1].plot(x,x**2,color="red")
axs[1,0].plot(x,x**3,color="red")
axs[1,1].plot(x,x**4,color="red")

plt.show()