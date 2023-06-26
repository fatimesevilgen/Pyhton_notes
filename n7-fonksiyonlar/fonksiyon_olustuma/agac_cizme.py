#ağaç çizme kodlarını bir fonksiyon hâline getir
def agacCiz(agacinYuksekligi, karakter='*'):
    b=agacinYuksekligi
    for i in range(1,agacinYuksekligi+1):
        print(b*' ',(2*i-1)*karakter)
        b-=1

#Şimdi, fonksiyonu kullanıcıdan aldığınız parametrelerle çağırabiliriz.       
agacYuksekligi=int(input("Ağacin yüksekliği kaç satir olsun? : "))
agacKarakteri=input("Ağaç için bir sembol veya karakter girin? : ")
if agacKarakteri!='' and agacYuksekligi>=1:
    agacCiz(agacYuksekligi, agacKarakteri[0])
elif agacKarakteri=='' and agacYuksekligi>=1:
    agacCiz(agacYuksekligi)
else: print('Hatali giriş')


