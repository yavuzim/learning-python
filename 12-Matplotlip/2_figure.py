import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,9,20)
y = x**3
z = x**2

figure = plt.figure()
axes_kub = figure.add_axes([0.2,0.2,0.8,0.8]) # sağdan %20 alttan %20 alan, genişlik 0.8, yükseklik 0.8
axes_kub.plot(x,y,"b")
axes_kub.set_xlabel("x axis")
axes_kub.set_ylabel("y axis")
axes_kub.set_title("Küb")

axes_kare = figure.add_axes([0.2,0.6,0.3,0.3])
axes_kare.plot(x,z,"r")
axes_kare.set_xlabel("x axis")
axes_kare.set_ylabel("y axis")
axes_kare.set_title("Kare")

plt.show()

######################################################################

figure = plt.figure()

axes = figure.add_axes([0,0,1,1])
axes.plot(x,z,label="Karesel")
axes.plot(x,y,label="Küb")

axes.legend(loc=1)

plt.show()

######################################################################

fig,axes = plt.subplots(nrows=2,ncols=1,figsize=(8,8))
axes[0].plot(x,y)
axes[0].set_title("Karesel")
axes[1].plot(x,z)
axes[1].set_title("Kübik")

plt.tight_layout()

fig.savefig("figure1.png")

plt.show()  

























