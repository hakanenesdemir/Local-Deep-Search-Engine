# Soru 1: ornek.txt dosyasını açıp Her satırın başına satır numarası ekleyerek
# satir_numarali.txt dosyasına yazın.

with open("1.1_file_IO/dosyalar/belgeler/ornek.txt","r",encoding="utf-8") as f:
    satirlar= f.readlines()

with open("1.1_file_IO/dosyalar/belgeler/satir_numarali.txt","w",encoding="utf-8") as f:
    for i,satir in enumerate(satirlar,start=1):
        f.write(f'{i} - {satir.strip()}\n')

with open("1.1_file_IO/dosyalar/belgeler/satir_numarali.txt","r",encoding="utf-8") as f:
    icerik= f.read()
    print(icerik)
