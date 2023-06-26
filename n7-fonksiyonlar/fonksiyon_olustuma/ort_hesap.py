#Kullanıcıdan liste olarak aldığı sayıların ortalamasını bulan bir fonksiyon
def ortalamaBul(sayilar):
    sayilarinToplami=0
    sayilarinOrtalamasi=0  
    for i in range(len(sayilar)):    
        sayilarinToplami+=sayilar[i]  
    sayilarinOrtalamasi=sayilarinToplami/len(sayilar)  
    return sayilarinOrtalamasi

#Sayıları kullanıcıdan alarak fonksiyonunuzu çağırabilirsiniz
sayiAdedi=int(input('Kaç adet sayinin ortalamasini alacaksiniz: '))
sayilarim=[]
for i in range(0,sayiAdedi):
    print (i+1, '. sayiyi giriniz?')   # indis sıfırdan başladığı için +1 kullandık 
    sayi=int(input())  
    sayilarim.append(sayi)
ortalamaBul(sayilarim)    
