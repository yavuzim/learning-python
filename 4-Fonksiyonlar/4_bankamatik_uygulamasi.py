# Bankamatik Uygulaması

from asyncio.windows_events import NULL


kemalHesap = {
    "ad" : "Kemal Yavuz İMER",
    "hesapNo" : "13245678",
    "bakiye" : 3000,
    "ekHesap" : 2000
}
tanerHesap = {
    "ad" : "Taner ÇOLAK",
    "hesapNo" : "15967844",
    "bakiye" : 4000,
    "ekHesap" : 3000
}

def paraCek(ad,cekilecekTutar):
    liste = [kemalHesap,tanerHesap]
    deger = NULL
    for item in liste:
        if ad == item["ad"]:
            deger = item
            break
    if(cekilecekTutar<=deger['bakiye']):
        deger['bakiye'] -=cekilecekTutar
        print(f"Kalan Ek Bakiye : {deger['bakiye']}")
    else:
        sec = input("Bakiyeniz Yetersiz. Ek Hesaptan Çekmek İster misiniz(e|h) : ")
        sec = sec.lower()
        if sec=="h":
            print("Çıkış Yaptınız.")
        else:
            _cekilecekTutar = input("Çekilecek Tutar : ")
            _cekilecekTutar = float(_cekilecekTutar)
            if cekilecekTutar<=deger['ekHesap']:
                deger['ekHesap'] -=_cekilecekTutar
                print(f"Kalan Ek Bakiye : {deger['ekHesap']}")
            else: print("Bakiyeniz Yetersiz.")


ad = input("Ad Soyad : ")
cekilecekTutar = input("Çekilecek Tutar : ")
cekilecekTutar = float(cekilecekTutar)
paraCek(ad,cekilecekTutar)