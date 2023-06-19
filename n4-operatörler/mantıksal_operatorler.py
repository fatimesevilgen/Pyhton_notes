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
