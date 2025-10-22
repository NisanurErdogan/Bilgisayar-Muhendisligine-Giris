ilkSayi = int( input("İlk sayıyı giriniz. "))
ikinciSayi = int(input("İkinci sayıyı giriniz. "))
islem = input("""Yapmak istediğiniz işlemi giriniz. 
(Toplama: +, Çıkarma: -, Çarpma:*, Bölme: /)              
""")

if islem == "+":
    print("Sonuç: "+str(ilkSayi+ikinciSayi))

elif islem == "-":
    print("Sonuç: "+str(ilkSayi-ikinciSayi))

elif islem == "*":
    print("Sonuç: "+str(ilkSayi*ikinciSayi))

elif islem == "/":
    print("Sonuç: "+str(ilkSayi/ikinciSayi))