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

