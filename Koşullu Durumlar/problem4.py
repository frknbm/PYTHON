geometrik=input("dörtgen mi üçgenin mi tipini bulmak istersin:")

sys_geometrik="dortgen"
sys_geometrik1="ücgen"

if(sys_geometrik==geometrik):
       kenar1=int(input("kenarın kaç olduğunu giriniz:"))
       kenar2 = int(input("kenarın kaç olduğunu giriniz:"))
       kenar3=int(input("kenarın kaç olduğunu giriniz:"))
       kenar4=int(input("kenarın kaç olduğunu giriniz:"))
       if(kenar1==kenar2 and kenar3==kenar4 and kenar3==kenar2):
           print("karedir bu seçtiğiniz dörtgen")
       elif(kenar1==kenar2 and kenar3==kenar4 and kenar3!=kenar2):
           print("dikdörtgendir seçtiğiniz dörtgen")
       else:
           print("sadece dörtgendir")
elif(sys_geometrik1==geometrik):
    k1=int(input("kenarini giriniz:"))
    k2=int(input("2. kenarı giriniz:"))
    k3=int(input("3.kenarı giriniz:"))
if(k1==k2 and k2==k3):
         print("eşkenar üçgendir")
elif(k1==k2 and k2!=k3):
         print("ikizkenar üçgendir")
else:
         print("siradan üçgendir")

