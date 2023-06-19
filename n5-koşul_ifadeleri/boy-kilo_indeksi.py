# 6- Kişinin kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
# Formül: (Kilo / boy uzunluğunun karesi)
# Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
# 0-18.4 => Zayıf
# 18.5-24.9 => Normal
# 25.0-29.9 => Fazla Kilolu
# 30.0-34.9 => Şişman (Obez)

kilo=float(input("kilonuzu giriniz: "))
boy=float(input("boyunuzu giriniz: "))

index= (kilo) / (boy**2)
if (index>=0) and (index<=18.4):
    print(f"kilo indexsiniz: {index} ve kilo degerlendirmeniz zayif")
elif (index>=18.5) and (index<=24.9):
    print(f"kilo indexsiniz: {index} ve kilo degerlendirmeniz normal")
elif(index>=25.0) and (index<=29.9):
    print(f"kilo indexsiniz: {index} ve kilo degerlendirmeniz fazla kilolu")
elif(index>=30.0) and (index<=45.0):
    print(f"kilo indexsiniz: {index} ve kilo degerlendirmeniz obez")
else:
    print("bilgileriniz hatali")


    