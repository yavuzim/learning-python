import numpy as np

# python list
py_liste = [1,2,3,4,5,6,7,8,9]

# numpy array

np_array = np.array([1,2,3,4,5,6,7,8,9])

print(f"py_list -> {py_liste} {type(py_liste)}") # list
print(f"np_array -> {np_array} {type(np_array)}") # ndarray

py_multi = [[1,2,3],[4,5,6],[7,8,9]]
np_multi = np_array.reshape(3,3)
 
print(f"py_multi -> {py_multi} {type(py_multi)}") # list
print(f"np_multi -> {np_multi} {type(np_multi)}") # ndarray

