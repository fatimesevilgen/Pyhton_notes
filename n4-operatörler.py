#*********ATAMA OPERATORLERİ*************

x, y, z = 2, 5, 107

numbers = 1, 5, 7, 10, 6

# 1- Kullanıcıdan aldığınız 2 sayının çarpımı ile x,y,z toplamının farkı nedir?
a= int(input('1.sayi: '))
b= int(input('2.sayi: '))

result= (a*b) - (x+y+z)
print(result)

# 2- y' nin x' e kalansız bölümünü hesaplayınız.
result= y//x
print(result)

# 3- (x,y,z) toplamının mod 3' ü nedir ?
toplam=int
toplam=(x+y+z)
result= toplam % 3
print(result)

# 4- y' nin x. kuvvetini hesaplayın
result= (y**x)
print(result)

# 5- x, *y, z = numbers işlemine gore z nin küpü kaçtır?
x, *y,  z= 1, 5, 7, 10, 6
result= z**3
print(result)

# 6- x, *y, z = numbers işlemine göre y nin değerleri toplamı kaçtır?
x, *y, z = 1, 5, 7, 10, 6
toplamy= y[0]+y[1]+y[2]
print(toplamy)



#****************KARŞILAŞTIRMA OPERATORLERİ**************

# 1- Girilen 2 sayıdan hangisi büyüktür ?
a=int(input('1.sayi gir: '))
b=int(input('2.sayi gir: '))

result= (a>b)

print(f'{a} sayisi {b} sayisindan büyüktür : {result}')

# 2- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız. 
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.

vize1 = float(input('vize1 gir: '))
vize2 = float(input('vize2 gir: '))
final = float(input('final gir: '))

ortalama= (((vize1+vize2)/2)*0.6) + (final*0.4)

print(f'not ortalamaniz : {ortalama} ve geçme durumunuz : {ortalama>=50}')


# 3- Girilen bir sayının tek mi çift mi olduğunu yazdırın.

bx=int(input("sayi gir: "))
result=((bx%2) == 0 )
print(f"girilen {bx} sayisi çifttir: {result}")

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
cx=int(input("sayi gir: "))
result=(cx<0)
print(f"{cx} sayisi negatiftir:{result}")


# 5- Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.

email= "fatimesevilgen@gmail.com"
parola="12345"

girilenemail=input("email adresi gir: ")
girilenparola= input("parola gir: ")

isemail= (email == girilenemail.lower().strip())
isparola= ( parola == girilenparola)

print(f"email bilgisi dogru mu {isemail} ve parola bilgisi dogru mu {isparola}")



#************MANTIKSAL OPERATÖRLER*******************

# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.
x= float (input("sayi gir: "))
result =(x>0) and (x<100)
print(result)


# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz.
sayix = int(input("sayi gir: " ))
result= (sayix>0) and (sayix % 2  == 0 )
print(f"girilen sayı pozitif çift:{result}")


# 3- Girilen 3 sayıyı büyüklük olarak karşılaştırınız.

a= int(input("sayi gir: "))
b =int(input("2.sayiyi gir: "))
c= int(input("3.sayiyi gir:" ))

result= (a>b) and (a>c)
print(f"a en büyük sayidir:{result}")

result= (b>a) and(b>c)
print(f"b en büyük sayidir:{result}")

result= (c>a) and (c>b)
print(f"c en büyük sayidir:{result}")

# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
# b-) Finalden 70 alındığında ortalamanın önemi olmasın.

vize11= float(input("not gir: "))
vize22= float(input("not2 gir:") )
final= float(input("final gir:" ))

ort= ((vize11 + vize22)/2 )*0.6 + (final*0.4)
#result= ( ort=> 50 ) and (final=>50)
result= ( ort >= 50 ) or  (final >= 70)

print(f"ortalamaniz: {ort}  geçme durumuz: {result}")


# 6- Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
# Formül: (Kilo / boy uzunluğunun karesi)
# Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
# 0-18.4 => Zayıf
# 18.5-24.9 => Normal
# 25.0-29.9 => Fazla Kilolu
# 30.0-34.9 => Şişman (Obez)

adiniz= input("adinizi giriniz:  ")
kg= input("kilonuzu giriniz: ")
hg= input("boyunuzu giriniz: ")

index= (kg) / (hg**2)
zayif=(index>=0) and (index<=18.4)
Normal=(index>=18.5) and (index<=24.9)
fazlakilolu =(index>=25.0) and (index<=29.9)
obez=(index>=30.0) and (index<=34.9)

print (f"{adiniz} kilo indexsin: {index} , kilo degerlendirmen : {zayif} ")
print (f"{adiniz} kilo indexsin: {index} , kilo degerlendirmen : {Normal} ")
print(f"{adiniz}  kilo indexsiniz {index}, kilo degerlendirmen: {fazlakilolu}  ")
print (f"{adiniz} kilo indexsin: {index} , kilo degerlendirmen : {obez} ")

