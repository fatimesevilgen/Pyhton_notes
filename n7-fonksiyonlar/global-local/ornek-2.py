# ornek-2
karsilamaMesaji='Merhaba'   #global degisken
kullaniciYasi=35      #global degisken
dogumGunuMu=True    #global degisken
if kullaniciYasi==35 and dogumGunuMu==True:
    karsilamaMesaji='Yolun yarisi'   #local değişken  
    kullaniciYasi+=1     #local değişken 
    print(dogumGunuMu)

dogumGunuMu=False   #global degisken

print (kullaniciYasi)   
print(dogumGunuMu)   
print(karsilamaMesaji)  

