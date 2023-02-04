kilo=int(input("kilonuzu giriniz:"))
boy=float(input("boynuzu giriniz:"))
bki=kilo/(boy**2)
print("bkyindeksiniz:",bki)

if(bki<=18.5):
    print("zayıfsınız bkiniz:",bki)
elif(bki>18.5 and bki<=25):
    print("normalsiniz bkniz:",bki)
elif(bki>25 and bki<=32):
    print("kilolusunuz bkiniz:",bki)
else:
    print("obezsiniz bkniz:",bki)

