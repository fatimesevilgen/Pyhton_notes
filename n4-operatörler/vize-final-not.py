# 5- Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayınız
# Eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın.
# a-) Ortamalama 50 olsa bile final notu en az 50 olmalıdır.
# b-) Finalden 70 alındığında ortalamanın önemi olmasın.

vize11= float(input("not gir: "))
vize22= float(input("not2 gir:") )
final= float(input("final gir:" ))

ort= ((vize11 + vize22)/2 )*0.6 + (final*0.4)
#result= ( ort=> 50 ) and (final=>50)
result= ( ort >= 50 ) or  (final >= 70)

print(f"ortalamaniz: {ort}  geçme durumuz: {result}")

#kosul ifadelerini henüz öğrenmediğiniz varsayılarak olusturulmus bir cevaptir

