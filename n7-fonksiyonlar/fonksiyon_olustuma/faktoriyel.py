#Verilen sayının faktöriyelini bulan bir fonksiyon

def faktoriyelAl(sayi):
    sonuc=1
    if (sayi==0 or sayi==1):
        print('sonuç= ', 1)  
    elif sayi>1:
        for i in range(1, sayi+1, 1):
            sonuc*=i
        print ('sonuc=', sonuc)  
    else: print ('0 veya daha büyük sayisal bir değer girmelisiniz')
faktoriyelAl(int(input('Faktöriyeli alinacak sayiyi giriniz: ')))


