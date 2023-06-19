#Email ve parola bilgileri ile giriş kontrolü yapınız.

email="sadik@turan.com"
password="12345"

girilenemail=input("email gir: ")
girilenpassword= input("password gir: ")

if(email==girilenemail):
    if(password==girilenpassword):
        print("uygulamaya giriş başarili")
    else:
        print("password hatali")
else:
    print("email hatali")
