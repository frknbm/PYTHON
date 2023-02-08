print("""***********************

FAKTORIYEL BULMA

programdan cikmak icin 'q'ya basiniz.
***********************""")

while True:
    sayi=input("sayi giriniz:")
    if(sayi=="q"):
        print("isleminiz sonlandiriliyor")
        break
    else:
        sayi = int(sayi)
        faktoriyel=1
        for i in range(2,sayi+1):
            faktoriyel *=i
        print("faktoriyel:",faktoriyel)
