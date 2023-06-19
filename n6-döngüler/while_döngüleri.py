sayilar=[1,3,5,7,9,12,19,21]

# 1- sayilar listesini while ile ekrana yazdiralim 
i=0
while (i<len(sayilar)):
    print(sayilar[i])
    i+=1
    
# 2- Başlangic ve bitiş degerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.

baslangic=int(input("başlangic: "))
bitis=int(input("bitiş: "))

i=baslangic
while i <= bitis:
    i+=1
    if (i%2==1):
        print(i)

# 3- 1-ile 100 arasindaki sayilari azalan sekilde yazdirin.

i=100
while i>0:
    i -= 1
    print(i)

# 4- kullanıcıdan alacaginiz 5 sayıyı ekrana sıralı bir sekılde yazdırın
numbers=[]
i=0
while i<5:
    sayi=int(input("sayi: "))
    numbers.append(sayi)
    i+=1
numbers.sort()
print(numbers)

# 5- kullanıcıdan alacaginiz sınırsız urun bilgisini urunler listesinde saklayınız
# ** ürün sayısını kullanıcıya sorun.
# ** dictionary listesi yapısı (name, price) şeklinde olsun.
# ** ürün ekleme işlemi bittiğinde ürünleri ekrana while ile listeleyin.

urunler=[]
adet=int(input("kaç urun eklemek istiyorsunuz:"))
i=0
while (i<adet):
    name=input("ürün ismi: ")
    price=input("ürün fiyati: ")
    urunler.append({
        'name':name,
        'price':price
    })
    i+=1
for urun in urunler:
    print(f"ürün adi: {urun['name']} ürün fiyati: {urun['price']}")    
