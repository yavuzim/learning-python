import math  
sayi = 4
fact = math.factorial(sayi)
karekok = math.sqrt(sayi)
asagiYuvarla = math.floor(sayi*0.10)
yukariYuvarla = math.ceil(sayi*0.10)
print(f"sayi : {sayi}")
print(f"fact : {fact}")
print(f"karekok : {karekok}")
print(f"asagiYuvarla : {asagiYuvarla}")
print(f"yukariYuvarla : {yukariYuvarla}")

print("##############################################")

import math as islem # math yerine islem yazmamızı sağlar.
sayi = 8
karekok = islem.sqrt(sayi)

print("##############################################")

from math import * # * modülün hepsini import eder.
from math import sqrt # sadece sqrt()'yi import eder.



