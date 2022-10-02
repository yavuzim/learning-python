# Değişken Tanımlama 1

ogrenciAd = "Kemal Yavuz"
ogrenciSoyad = "İMER"
dersAdi = "Biçimsel Diller ve Otomata Teorisi"
vize = 85
final = 95
ortalama = (vize*40/100)+(final*60/100)
print("Ortalama : ",ortalama)  # Ortalama :  91.0

#####################################################################################

# Değişken Tanımlama 2

isim,soyad,yas,ogrenciMi = ("Kemal Yavuz","İMER",24,True)
print("İsim : ",isim,"\n Soyisim : ",soyad,"\n Yaş : ",yas,"\n Öğrenci mi? ",ogrenciMi)
#İsim :  Kemal Yavuz 
#Soyisim :  İMER 
# Yaş :  24 
#Öğrenci mi?  True

#####################################################################################

# String ifadeleri birleştirme

ad = "Kemal Yavuz"
soyad = "İMER"
adSoyad = ad+" "+soyad
print(adSoyad) # Kemal Yavuz İMER