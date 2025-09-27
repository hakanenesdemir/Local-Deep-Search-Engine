# Soru 2: ornek.txt dosyasının toplam kelime sayısı hesapla ve ekrana yazdır.

with open("1.1_file_IO/dosyalar/belgeler/satir_numarali.txt","r",encoding="utf-8")as f:
    icerik=f.read().split()
    kelime_sayisi=len(icerik)
    print("Toplam kelime sayısı: {0}".format(kelime_sayisi))