print("""
***********************

KULLANICI GİRİŞİ
      
***********************      
      
      """)
sys_kullaniciadi= "murat"
sys_parola="123456"

kullaniciadi = input("kullanici adini giriniz:")
parola = input("parolayı giriniz:")

if (kullaniciadi==sys_kullaniciadi and parola!=sys_parola):
    print("parolayı yanlış girdiniz")
elif(kullaniciadi!=sys_kullaniciadi and parola==sys_parola):
    print("kullanıcı adini yanlış girdiniz")
elif(kullaniciadi==sys_kullaniciadi and parola==sys_parola):
    print("başarıyla giriş yaptınız")
elif(kullaniciadi!=sys_kullaniciadi and parola!=sys_parola):
    print("kullanıcı adını ve parolayı yanlış girdiniz")

