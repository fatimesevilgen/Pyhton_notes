#Bir sayının asal bir sayı olup olmadığını bulan bir fonksiyon

def asalMi(sayi):
    sayac=2      # tüm sayılar 1'e bölüneceğinden 2 ile başlattık  
    while sayac<=int(sayi/2):
        if sayi%sayac==0:
            return False
        sayac+=1  
    return True 
        
#Fonksiyonu çağırma
asalMi(113)


