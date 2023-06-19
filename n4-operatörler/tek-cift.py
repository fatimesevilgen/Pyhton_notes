#Girilen bir sayının tek mi çift mi olduğunu yazdırın.

bx=int(input("sayi gir: "))
result=((bx%2) == 0 )
print(f"girilen {bx} sayisi çifttir: {result}")

# 4- Girilen bir sayının negatif pozitif durumunu yazdırın.
cx=int(input("sayi gir: "))
result=(cx<0)
print(f"{cx} sayisi negatiftir:{result}")
