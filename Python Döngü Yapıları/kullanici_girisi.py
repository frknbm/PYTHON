print("""*****************************

kullanıcı girisi

*****************************""")

sys_kullanici_adi="furkan"
sys_parola="1234"
giris_hakki=3

while True:
    kullanici_adi=input("kullanici adini giriniz:")
    parola=input("parolayi giriniz:")
    if(sys_kullanici_adi!=kullanici_adi and sys_parola==parola):
        print("kullaniz adini yanlis girdiniz")
        giris_hakki-=1
    elif(sys_kullanici_adi==kullanici_adi and sys_parola!=parola):
        print("parolanizi yanlis girdniz")
        giris_hakki-=1
    elif(sys_kullanici_adi!=kullanici_adi and sys_parola!=parola):
        print("kullanici adiniz ve parolaniz yanlis")
        giris_hakki-=1
    else:
        print("basariyla giris yapildi")
        break
    if (giris_hakki == 0):
        print("giris hakkiniz biit programiniz sonlandırılıyor")
        break


