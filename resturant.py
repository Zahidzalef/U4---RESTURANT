import os
os.system("cls")


masalar = dict()
for a in range(20):
    masalar[a] = 0

def hesap_ekle():
    masa_no = int(input("Masa numarası : "))
    bakiye = masalar[masa_no]
    eklenecek_ucret = float(input("Eklenecek ücret : "))
    guncel_bakiye = bakiye+eklenecek_ucret
    masalar[masa_no]=guncel_bakiye
    print("İşleminiz tamamlandı.")
def hesap_odeme():
    masa_no = int(input("Masa numarası : "))
    bakiye = masalar[masa_no]
    print("Masa {}'in hesabı : {} TL".format(masa_no,bakiye))
    masalar[masa_no] = 0
    print("Hesap ödendi.")
def dosya_kontrolu(dosya_adi):
    try:
        dosya = open(dosya_adi,"r",encoding="utf-8")
        veri = dosya.read()
        veri = veri.split("\n")
        veri.pop()
        dosya.close()
        for a in enumerate(veri):
            masalar[a[0]] = float(a[1])

    except FileNotFoundError:
        dosya = open(dosya_adi,"w",encoding="utf-8")
        dosya.close()
        print("Kayıt dosyası oluşturuldu.")
def dosya_guncelle(dosya_adi):
    dosya = open(dosya_adi,"w",encoding="utf-8")
    for a in range(20):
        bakiye = masalar[a]
        bakiye = str(bakiye)
        dosya.write(bakiye+"\n")
    dosya.close()

def ana_islem():
    dosya_kontrolu("bakiye.txt")
    while True:
        print("""
            ZALEF RESTURANT UYGULAMASI
            0) KAPAT
            1) MASALARI GÖRÜNTÜLE
            2) HESAP EKLE
            3) HESAP ÖDEME
            """)
        secim = input("Lütfen seçimi yapınız : ")
        if secim == "0":
            exit(1)
        elif secim == "1":
            for a in range(20):
                print("Masa {} için hesap : {} TL".format(a,masalar[a]))
        elif secim=="2":
            hesap_ekle()
        elif secim=="3":
            hesap_odeme()
        else:
            print("Hatalı seçim yaptınız.\nLütfen yeniden seçim yapınız.")
        dosya_guncelle("bakiye.txt")
        input("Ana menüye geri dönmek için enter'a basınız : ")
        os.system("cls")
ana_islem()