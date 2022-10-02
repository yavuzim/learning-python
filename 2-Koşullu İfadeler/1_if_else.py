# 1- Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumu kontrolü.
#    Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.

isim = input("Ad Soyad : ")
yas = input("Yaş : ")
egitimDurum = input("Eğitim Durumu : ")
yas = int(yas)
egitimDurum = egitimDurum.capitalize()
if yas>=18 and (egitimDurum=="Lise" or egitimDurum=="Üniversite"):
    print("Ehliyet Alabilir.")
    print(f"İsim : {isim} ** Yaş : {yas} ** Eğitim Durumu : {egitimDurum}")
else :
    print("Ehliyet Alamaz.")
    print(f"İsim : {isim} ** Yaş : {yas} ** Eğitim Durumu : {egitimDurum}")

########################################################################################################

