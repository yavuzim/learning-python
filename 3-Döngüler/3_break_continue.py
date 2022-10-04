isim = "Kemal Yavuz İMER"

for i in isim:
    if i=="İ":
        break # İ'ye geldiğinde döngü sona erecek
    print(i) # Kemal Yavuz
print("Bitti")

for i in isim:
    if i=="İ":
        continue # İ'ye geldiğinde print satırına gelmeyecek döngüye devam edecek. Kemal Yavuz MER
    print(i)

