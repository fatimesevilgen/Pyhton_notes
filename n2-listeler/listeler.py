# 1 "Bmw, Mercedes, Opel, Mazda" elemanlarına sahip bir liste oluşturunuz.
arabalar=['Bmv', 'Mercedes', 'Opel' ,'Mazda']


# 2 Liste Kaç elemanlıdır ?
result= len(arabalar)
print(result)


# 3 Listenin ilk ve son elemanı nedir ?
result=arabalar[0]
result=arabalar[-1]
print(result)


# 4 Mazda değerini Toyota ile değiştirin.
arabalar[-1]= 'Toyota'
print(arabalar)


# 5 Mercedes listenin bir elemanı mıdır ?
result= 'Mercedes' in arabalar
print(result)


# 6 Listenin -2 indeksindeki değer nedir ?
result=arabalar[-2]
print(result)


# 7 Listenin ilk 3 elemanını alın.
result=arabalar[0:3]
print(result)


# 8 Listenin son 2 elemanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
arabalar[-2:] = ["Toyota", "Renault"]
print(arabalar)


# 9 Listenin üzerine "Audi" ve "Nissa" değerlerini ekleyin.
arabalar.append('Audi')
arabalar.append('Nissan')
result= arabalar + ["Audi", "Nissa"]   #böyle de olabilir
print(result)


# 10 Listenin son elemanını silin.
del arabalar[-1]
print(arabalar)


# 11 Liste elemanlarını tersten yazdırınız.
result= arabalar[::-1]
print(result)


# 12 Aşağıdaki verileri bir liste içinde saklayınız.
# studentA: Yiğit Bilgi 2010, (70,60,70)
# studentB: Sena Turan 1999, (80,80,70)
# studentC: Ahmet Turan 1998, (80,70,90)

studentA= ['Yiğit','Bilgi',2010, [70,60,70]]
studentB= ['Sena' ,'Turan', 1999, [80,80,70]]
studentC= ['Ahmet' ,'Turan' ,1998, [80,70,90]]


names = ['Ali', 'Yağmur', 'Hakan', 'Deniz']
years= [1998, 2000, 1998, 1987]

# 13 "Cenk" ismini listenin sonuna ekleyiniz.
names.append("Cenk")
print(names)


# 14 "Sena" değerini listenin başına ekleyiniz.
names.insert(0,'Sena')
print(names)


# 15 "Deniz" ismini listeden siliniz.
names.remove('Deniz')  
names.pop()     #listenin sonundaki elemanı siler ve döndürür
print(names)


# 16 "Deniz" isminin indeksi nedir ?
index=names.index('Deniz')
print(index)


# 17 "Ali" listenin bir elemanı mı?
result= 'Ali' in names
print(result)


# 18 Liste elemanlarını ters çevirin.
names.reverse()
print(names)


# 19 Liste elemanlarını alfabetik olarak sıralayınız.
names.sort()
print(names)


# 20 years listesini rakamsal büyüklüğe göre sıralayınız.
years.sort()
print(years)


# 21 str = "Chevrolet, Dacia" karakter dizisini listeye çeviriniz.
str ="Chevrolet , Dacia"
result= str.split(',')
print(result)


# 22- years dizisinin en büyük ve en küçük elemanı nedir ?
min = min(years)
max = max(years)
print(min, max)


# 23- years dizisinde kaç tane 1998 değeri vardır?
result= years.count(1998)
print(result)


# 24 years dizisinin tüm elemanlarını siliniz
years.clear()
print(years)

# 25- Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
markalar=[]
marka= input("marka giriniz: ")
markalar.append(marka)

marka= input("marka giriniz: ")
markalar.append(marka)

marka= input("marka giriniz: ")
markalar.append(marka)
print(markalar)

