sayilar=[1,3,5,7,9,12,19,21]

# 1- sayilar listesindeki hangi sayilar 3 ün katidir?
for i in sayilar:
    if(i%3==0):
        print(i)

# 2- sayilar listesindeki saylarin toplami kaçtir?
toplam2=0
for sayi in sayilar:
    toplam2 += sayi
print("toplam:", toplam2)

toplam = sum(sayilar)  #döngü kullanılmadan boyle yapılabilir
print(toplam)


# 3- sayilar listesindeki tek sayilarin karesini aliniz.
for i in sayilar:
    if (i%2==1):
        print(i**2)


sehirler= ["kocaeli", "istanbul", "ankara", "izmir", "rize"]

# 4- sehirlerden hangileri en fazla 5 karakterlidir?
for i in sehirler:
    if (len(i)<=5):
        print(i)

 
urunler =[
{'name':'samsung s6' , 'prince': '3000'},
{'name':'samsung s7' , 'prince': '4000'},
{'name':'samsung s8' , 'prince': '5000'},
{'name':'samsung s9' , 'prince': '6000'},
{'name':'samsung s10' , 'prince': '7000'}
]

# 5-urunlerin fiyatlari toplami nedir?
toplam=0
for i in urunler:
    fiyat=int(i['prince'] )
    toplam += fiyat 
print(f"toplam ürün fiyati:{toplam}")
print("toplam ürün fiyati:{}".format(toplam) )

# 6- ürünlerin fiyati en fazla 5000 olan ürünleri gösteriniz.
liste=[]
for i in urunler:
    a = int(i['prince'])
    if a<=5000:
        liste.append(a)
print(liste)

for urun in urunler:
    if int(urun['prince']) <= 5000 :
        print(urun['name'])

