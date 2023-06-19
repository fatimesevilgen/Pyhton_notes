# 1- Kullanıcıdan yaş ve eğitim bilgilerini isteyip ehliyet alabilmedurumunu kontrol ediniz.
# Ehliyet alma koşulu en az 18 ve eğitim durumu lise ya da üniversite olmalıdır.
     
yas= int(input("yas gir:"))
egitim= input("egitim durumu: ")
 
if ( yas >= 18 ):
    if(egitim == "universite") or (egitim=="lise" ):
        print(" ehliyet alabilirsiniz")
        
    else:
        print("ehliyet alamazsiniz egitim durumunuz yetersiz.")    
else:
    print("ehliyet alamazsiniz yasiniz tutmuyor.")  

# 2- Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere
# göre hesaplayınız.
# 1. Bakım => 1. yıl
# 2. Bakım => 2. yıl
# 3. Bakım => 3. yıl

days=int(input("araciniz kaç gundur trafikte: "))
if (days<=365):
    print("1.servis araliği")
elif (days>=365) and (days<365*2):
    print("2.servis araligi")
elif(days>=365*2) and (days<=365*3):
    print("3.servis araligi")
else:
    print("hatali islem")


# 3- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
sayi=float(input("bir sayi gir:"))
if (sayi>=0) and (sayi<=100):
    print("sayi0 ve 100 arasinda ")
else:
    print("sayi 0 ve 100 arasinda degil")


# 4- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
a=int(input("sayi gir:"))
if(a>0):
    if(a%2==0):
        print("a sayisi çift ve pozitiftir")
    else:
        print("girilen sayi pozitif ancak tektir")
else:
    print("girilen sayi negatiftir")

    
    
# 5- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

x=int(input("sayi gir:"))
y=int(input("sayi gir:"))
z=int(input("sayi gir:"))

if (x>y) and (x>z):
    print("x en büyük sayidir")
elif (y>x) and (y>z):
    print(" y en büyük sayidir.")
elif (z>x) and (z>y):
    print("z en büyük sayidir.")
