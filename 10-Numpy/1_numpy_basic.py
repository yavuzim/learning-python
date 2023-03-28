# NumPy, Sayısal Python’un kısaltmasıdır. Her tür bilimsel hesaplamayı yapmanıza yardımcı olan bir Python kitaplığıdır.

import numpy as np

# python list
liste = [1,2,3,4,5,6,7,8,9,10]

# numpy array
np_dizi = np.array([10,20,30,40,50,60,70,80,90,100])
print(np_dizi)

# python matris
py_matris = [[1,2,3],[4,5,6],[7,8,9]]

# numpy matris
np_dizi = np.array([45,89,78,45,44,12,1,38,36,55,31,74])
np_matris = np_dizi.reshape(4,3) # 3x3 matris.
print(np_matris)

print(np_dizi.ndim) # ndim 1 boyutlu olduğunu yazar.
print(np_matris.ndim) # ndim 2 boyutlu olduğunu yazar.

print(np_matris.shape) # shape (3,3) olduğunu gösterir.