#Bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan ortalamaya göre
# not aralığına karşılık gelen not bilgisini yazdırınız.
# 0-24 => 0
# 25-44 => 1
# 45-54 => 2
# 55-69 => 3
# 70-84 => 4
# 85-100 => 5

not1=float(input("not1 gir:"))
not2=float(input("not2 gir:"))
sozlu=float(input("sozlu gir:"))
ortalama= int((not1+not2+sozlu)/3)

if (ortalama>=0) and (ortalama<=24):
    print(f"ortalamaniz:{ortalama} ve notunuz:0")

elif (ortalama>=25) and (ortalama<=44):
    print(f"ortalamaniz:{ortalama} ve notunuz:1")

elif (ortalama>=45) and (ortalama<=54):
    print(f"ortalamaniz:{ortalama} ve notunuz:2")

elif (ortalama>=55) and (ortalama<=69):
    print(f"ortalamaniz:{ortalama} ve notunuz:3")

elif (ortalama>=70) and (ortalama<=84):
   print(f"ortalamaniz:{ortalama} ve notunuz:4")

elif (ortalama>=85) and (ortalama<=100):
   print(f"ortalamaniz:{ortalama} ve notunuz:5")

else:
   print("yanlis bilgi girdiniz")
