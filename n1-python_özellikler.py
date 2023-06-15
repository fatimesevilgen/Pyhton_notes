website = 'http://www.sadikturan.com'
course = 'Python Kursu: Baştan Sona Python Proglama Rehberiniz (40 Saat)'

# 1-'course' karakter dizisinde kaç karakter vardır?
result = len(course)  #len fonk. dizedeki karakter sayısını verir
print(result)


# 2-  'website' içinden www karakterlerini alın
result=website[7:10]
print(result)


# 3- 'website' içinden com karakterini alın 
leght=len(website)
result=website[leght-3:leght]
print(result)


# 4- 'course' içinden ilk 15 ve son 15 karakterini alın.
result=course[0:15]
result2=course[-15:]
print(result)
print(result2)


# 5- 'course' ifadesindeki karakterileri tersten yazdırın.
result=course[::-1]
print(result)


# 6-' Hello World ' karakter dizisinin baş ve sondaki boşluk karakterini silin.
result=' Hello World '.strip()
result=' Hello World '.lstrip()  #soldaki boşluğu siler 
result=' Hello World '.rstrip()  #sağdaki boşluğu siler
print(result)


# 7- www.sadikturan.com içindeki sadikturan bilgisi haricindeki karakterleri silin 
result=website.strip('htp:/w.moc')
result='www.sadikturan.com'.strip('w.moc')   #böyle de olabilir
print(result)


# 8- 'course' karakter dizisindeki tüm harfleri küçük yapın 
result=course.lower()     # hepsini küçük harf yapar
result=course.upper()     # hepsini büyük harf yapar
result=course.title()     # her kelimenin baş harfini büyük yazar
print(result)


# 9- 'website içinde kaç tane a karakteri var.
result = website.count('a')  #içinde kaç tane a olduğunu söyler
result = website.count('www',0 ,10)   # 0 ve 10. indexler arasında 'www' aratır
print(result)


# 10- 'website' www ile başlayıp com ile bitiyor mu?
result = website.startswith('www')   # www ile başlıyor mu?
result = website.endswith('com')     # com ile bitiyor mu?
print(result)


# 11- 'website' içinde '.com' ifadesi var mı?
result=website.find('.com')
result=website.index('.com')
result=website.rindex('.com')     #sağdan başlayarak arar
print(result)


# 12- 'course' içindeki karakterlerin hepsi alfabetik mi?
result=course.isalpha()    #alfabede bulunan bir harf mi diye kontrol eder
result='123'.isdigit()
print(result)


# 13- 'contents' ifadesini satirda 50 karakter içerisine yerleştirip sağ ve soluna * ekleyin
result='contents'.center(50, '*')
result='contents'.ljust(50, '*')    # ifadeyi sola doğru yaslar yıldızları sağa yazdırır
result='contents'.rjust(50, '*')    # ifadeyi sağa doğru yaslar yıldızları sola yazdırır
print(result)


# 14- 'course' karakter dizisindeki tüm boşluk karakterlerini '_' ile değiştirin
result=course.replace(' ', '_')
result=course.replace(' ', '')     # boşlukları siler
print(result)


# 15- 'Hello World' karakter dizisindeki 'World' ifadesini 'There' ile değiştirin.
result='Hello World'.replace('World', 'There')
print(result)


# 16- 'course' karakter dizisini boşluk karakterlerinden ayırın.
result=course.split(' ')
print(result)


name='Bora'
surname='Yilmaz'
age='32'
job='mühendis'

# 17- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazınız.
'Benim adim Bora yilmaz , Yaşim 32 ve mesleğim mühendis'

print(f"Benim adim {name} {surname}, yaşim {age}, Mesleğim {job} ")
print("Benim adim {} {}, yaşim{}, Mesleğim {} ".format(name,surname,age,job))  # böyle de olabilir

# 18- 'Hello world' ifadesindeki w karakterini W ile değiştrin

message = "Hello world"
message = message.replace("w", "W")
print(message)

