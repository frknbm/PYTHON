a =int(input("1. sayi giriniz:"))
b=int(input("2.sayiyi giriiniz:"))
c=int(input("3.sayiyi giriniz:"))

if(a>=b and a>=c):
        print("en büyük sayi :",a)
elif(b>=a and b>=c):
        print("en büyük sayi:",b)
elif(c>=a and c>=b):
        print("en büyük sayi",c)