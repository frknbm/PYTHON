print("""************************
ATM makinesine hosgeldiniz

1.BAKİYE SORGULAMA
2.PARA YATIRMA
3.PARA ÇEKME

    programdan cikmak icin 'q' ya basin

***********************
""")

bakiye=1000

while True:
    islem=input("islemi seciniz:")
    if (islem=='q'):
        print("isleminiz sonlandırılıyor..............")
        break
    elif(islem=='1'):
        print("bakiyeniz:",bakiye)
    elif(islem=='2'):
        miktar=int(input("ne kadar para yatirmak istiyorsunuz:"))
        print("yeni bakiyeniz:",miktar+bakiye)
    elif(islem=='3'):
        miktar=int(input("ne kadar para cekmek istiyorsunuz:"))
        if(miktar>bakiye):
            print("bu parayi cekmek icin yeterli bakiyeniz yoktur")
            break
        print("yeni bakiyeniz:",bakiye-miktar)
    else:
        print("gecersiz islemmmm......... programdan cikiliyorrrrr")
        break
