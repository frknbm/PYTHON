print("""******************
      MÜKEMMEL SAYİYİYİ BULMA 
      
Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
      
      cikmak icin 'q' ya basin
*****************      """)

while True:
    sayi=(input("sayi giriniz:"))
    if(sayi=="q"):
        print("islemini sonlandiriliyor")
        break
    else:
        for i in range(2,sayi):


