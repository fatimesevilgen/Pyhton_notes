'''
1-100 arasinda rastgele üretilecek bir sayiyi aşaği yukari ifadeleri ile buldurmaya calisin.(hak=5)
** "random modülü" için "python random" şeklinde arama yapin.
** 100 üzerinden puanlama yapin.Her soru 20 puan.
** Hak bilgisini kullanicidan alin ve her soru belirtilen can sayisi üzerinden hesaplansin
'''
import random

sayi=random.randint(1,100)
can=int(input("kaç hakkiniz olmasini istersiniz: "))
hak=can
sayac=0

while hak > 0:
    hak-=1
    sayac+=1
    tahmin=int(input("tahmini gir: "))

    if (sayi==tahmin):
        print(f"TEBRİKLER {sayac}. DEFADA BİLDİNİZ \nTOPLAM PUANINIZ {100-(100/can)*(sayac-1)}")    
        break
    elif sayi > tahmin:
        print("yukari")
    else:
        print("aşaği")    

    if hak==0:
        print(f"HAKKINIZ BİTTİ \nTUTULAN SAYI {sayi}")    
