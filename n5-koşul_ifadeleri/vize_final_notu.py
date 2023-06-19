#5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
# b-) Finalden 70 alındığında ortalamanın önemi olmasın.


vize1=float(input("vize notu gir:"))
vize2=float(input("vize2 notunu gir:"))
final= float(input("final notunu gir:"))
ortalama= ((vize1+vize2)/2)*0.6 + (final*0.4)

# A ŞIKKI 
if ( ortalama>=50):
    if (final>=50):
        print(f"ögrencinin ortalamasi: {ortalama} ve geçme durumu: başarili ")
    else:
        print(f"ögrencinin ortalamasi: {ortalama} ve geçme durumu: başarisiz ")
else:
    print(f"ögrencinin ortalamasi: {ortalama} ve geçme durumu: başarisiz ")    


# B ŞIKKI
if (ortalama>=50):
    print(f"ögrencinin ortalamasi: {ortalama} ve geçme durumu: başarili ")
else:
    if (final>=70):
        print(f"ögrencinin ortalamasi: {ortalama} ve geçme durumu: başarili. Final notu sayesinde geçtiniz.")
    else:
        print(f"ögrencinin ortalamasi: {ortalama} ve geçme durumu: başarisiz ")    

