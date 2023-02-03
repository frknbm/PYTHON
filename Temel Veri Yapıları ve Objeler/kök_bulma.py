a = int(input("a sayisini giriniz:"))
b = int(input("b sayisini giriniz:"))
c = int(input("c sayisini giriniz:"))

delta = b ** 2 -4 * a * c
x1 = (-b - delta ** 0.5) / (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)

print("birinci kök:{} \n ikinci kök:{}".format(x1,x2))

