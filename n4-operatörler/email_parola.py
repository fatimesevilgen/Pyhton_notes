#Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.

email= "fatimesevilgen@gmail.com"
parola="12345"

girilenemail=input("email adresi gir: ")
girilenparola= input("parola gir: ")

isemail= (email == girilenemail.lower().strip())
isparola= ( parola == girilenparola)

print(f"email bilgisi dogru mu {isemail} ve parola bilgisi dogru mu {isparola}")


