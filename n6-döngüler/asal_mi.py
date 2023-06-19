#Girilen sayinin asal olup olmadıgını bulduran progrmaı yaziniz.

sayi=int(input("sayi gir:"))
if sayi==1:
    print("1 sayisi asal değildir.")

asalmi=True
for i in range(2,sayi):
    if sayi%i==0:
        asalmi=False
        break
if asalmi==True:       
    print("sayi asaldir")
else:    
    print("sayi asal değildir")