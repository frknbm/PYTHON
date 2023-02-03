a=int(input("a sayisini giriniz:"))
b=int(input("b sayisini giriniz:"))

print("a sayisi:{},b sayisi:{}\ndegerleri birbirleriyle değiştirilcek".format(a,b))
a,b=b,a

print("a sayisinin yeni hali:{}\nb sayisininin yeni hali:{}".format(a,b))
