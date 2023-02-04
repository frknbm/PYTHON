print(""""****************************
HESAP MAKİNESİ PROGRAMI

1-toplama işlemi

2-çıkarma işlemi

3-çarpma işlemi

4-bölme işlemi


 ***************************     """)

a = int(input("a sayisini giriniz:"))
b = int(input("b sayisini giriniz:"))

c = int(input("hangi islemi yapmak istersiniz:"))

if(c == 1):
    print("{}+{}={}".format(a,b,a+b))
elif(c == 2):
    print("{}-{}={}".format(a,b,a-b))
elif(c==3):
    print("{}*{}={}".format(a,b,a*b))
elif(c==4):
    print("{}/{}={}".format(a,b,a/b))
else:
    print("geçersiz işlem")