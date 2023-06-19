'''
6- Kişinin ad, kilo ve boy bilgilerini alip kilo indekslerini hesaplayiniz.
Formül: (Kilo / boy uzunluğunun karesi)
Aşağidaki tabloya göre kişi hangi gruba girmektedir.
0-18.4 => Zayif
18.5-24.9 => Normal
25.0-29.9 => Fazla Kilolu
30.0-34.9 => Şişman (Obez)
'''
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

#kosul ifadelerini henüz öğrenmediğiniz varsayılarak olusturulmus bir cevaptir