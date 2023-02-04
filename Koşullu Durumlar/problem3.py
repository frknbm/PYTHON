vize=int(input("vize notunuzu giriniz:"))
final=int(input("final notunuz girinz:"))
proje=int(input("proje notunuzu giriniz:"))

toplamnot=(vize*30)/100 + (final*40)/100 +(proje*30)/100

if(toplamnot>=90):
      print("aa")
elif(toplamnot>=85):
      print("ba")
elif(toplamnot>=80):
      print("cc")
elif(toplamnot>=60):
      print("dd")
else:
      print("kaldınız")