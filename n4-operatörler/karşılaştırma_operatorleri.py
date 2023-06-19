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
