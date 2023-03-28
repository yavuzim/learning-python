# Iterators, Python’a iterasyon özelliği kazandıran bir nesnedir.

liste = [1,2,3,4,5]

iterator = iter(liste)
print(next(iterator)) # 1
print(next(iterator)) # 2
print(next(iterator)) # 3
print(next(iterator)) # 4
print(next(iterator)) # 5

##################################################################################

dersler = ["Sayısal Yöntemler","Lineer Cebir","Veri Yapıları","Ayrık Matematik"]
iterator = iter(dersler)
while True:
    try:
        print(next(iterator))
    except StopIteration:
        break
    
##################################################################################
        
    class Numara:
        def __init__(self,baslangic,bitis):
            self.baslangic = baslangic
            self.bitis = bitis
            
        def __iter__(self):
            return self
        def __next__(self):
            if self.baslangic<=self.bitis:
                x = self.baslangic
                self.baslangic+=1
                return x
            else:
                raise StopIteration
                
listem = Numara(10,20)
for i in listem:
    print(i)
                
                
                
                
                
                
                
                
                
                
                
                
                
                