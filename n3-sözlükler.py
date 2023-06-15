'''
ogrenciler = {
    '120': { 
       'ad': 'Ali',
       'soyad':'Yilmaz',
       'telefon': '532 000 00 01'  
    },

    '125':{
       'ad': 'Can' ,
       'soyad': 'Korkmaz' ,
       'telefon': '532 000 00 02'
    },

    '128': {
       'ad': 'Volkan' ,
       'soyad': 'Yükselen' ,
       'telefon': '532 000 00 03'
    }

}
'''
# soru 1 = bilgileri verilen ogrencileri kullanıcıdan aldıgınız bilgilerle dictionary içinde saklayınız

ogrenciler={}
 
number = input ('ögrenci no: ')
name= input('ögrenci adi: ')
surname= input('ögrenci soyad: ')
telefon= input('ögrenci telefon: ')

ogrenciler.update({
    number : { 
       'ad': name,
       'soyad':surname,
       'telefon': telefon
   }
})

number = input ('ögrenci no: ')
name= input('ögrenci adi: ')
surname= input('ögrenci soyad: ')
telefon= input('ögrenci telefon: ')

ogrenciler.update({
    number : { 
       'ad': name,
       'soyad':surname,
       'telefon': telefon
   }
})

number = input ('ögrenci no: ')
name= input('ögrenci adi: ')
surname= input('ögrenci soyad: ')
telefon= input('ögrenci telefon: ')

ogrenciler.update({
    number : { 
       'ad': name,
       'soyad':surname,
       'telefon': telefon
   }
})

print(ogrenciler)

# soru 2 = ogrenci numarasını kullanıcıdan alıp ilgili ogrenci bilgisini gosterin 

orgnumber=input('ogrenci no gir: ')
ogrenci= ogrenciler[orgnumber]

print(f" Aradiginiz {orgnumber} nolu ogrencinin adi:{ogrenci['ad'] }  soyadi :{ogrenci['soyad']} telefonu ise {ogrenci['telefon']} ")