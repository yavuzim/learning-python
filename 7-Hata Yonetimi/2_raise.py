x = 10

if x>10:
    raise Exception("x 5 den büyük değer alamaz.")
else: 
    print("x : ",x)
    
#################################################################################################
    
def parola_kontrol(parola):
    if len(parola)<7:
        raise Exception("Parola en az 7 karakter olmalıdır!")
    return parola

parloaSonuc = parola_kontrol("11")
print(parloaSonuc)