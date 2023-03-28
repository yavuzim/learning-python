import numpy as np

sayilar = np.array([0,5,10,15,20,25,50,75])
print(sayilar[5])       # 25
print(sayilar[0:3])     # [ 0  5 10]
print(sayilar[:4])      # [ 0  5 10 15]
print(sayilar[3:])      # [15 20 25 50 75]
print(sayilar[::])      # [ 0  5 10 15 20 25 50 75]
print(sayilar[::-1])    # [75 50 25 20 15 10  5  0]

print("###########################################################")

matris = np.array([[0,5,10],[15,20,25],[50,75,85]]) 
print(matris)           # 3x3 matris
print(matris[0])        # [ 0  5 10]
print(matris[1])        # [15 20 25]
print(matris[2])        # [50 75 85]
print(matris[0,2])      # 10
print(matris[1,1])      # 20
print(matris[:])        # Tüm satırları seçer.
print(matris[:,2])      # [10 25 85]
print(matris[:,0])      # [ 0 15 50]
print(matris[:,0:2])    # [[ 0  5] [15 20] [50 75]] 
print(matris[1,:])      # [15,20,25]
print(matris[-1,:])     # [50 75 85]
print(matris[:3,:3])    # [[ 0  5 10] [15 20 25][50 75 85]]
print(matris[:2,:2])    # [[ 0  5] [15 20]]

print("###########################################################")

arr1 = np.arange(0,10)
arr2 = arr1     # aynı referans
print(f"arr1 : {arr1}   -   arr2 : {arr2}")
arr2[0] = 20    
print(f"arr1 : {arr1}   -   arr2 : {arr2}")

print("###########################################################")

arr1 = np.arange(0,10)
arr2 = arr1.copy()     # farklı referans
print(f"arr1 : {arr1}   -   arr2 : {arr2}")
arr2[0] = 20
print(f"arr1 : {arr1}   -   arr2 : {arr2}")
