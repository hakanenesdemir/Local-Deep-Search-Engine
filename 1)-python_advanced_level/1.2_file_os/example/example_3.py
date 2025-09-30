# 1.2_file_os/ klasöründeki tüm .txt dosyalarını alt klasörler dahil tarayın

#Beklenen çıktı
#Dosya: ornek.txt | Klasör: belgeler/subklasor | Satır Sayısı: 12
#Dosya: deneme.txt | Klasör: belgeler | Satır Sayısı: 7

import os

for klasor, altKlasor, dosyalar in os.walk("1.2_file_os/"):
    for dosya in dosyalar:
        if dosya.endswith(".txt"):
            #iki tane string değeri default path / ya da \ olmasına göre aralarına işaret koyar ve birleştirir
            with open(os.path.join(klasor, dosya), "r", encoding="utf-8") as f:
                satirlar = f.readlines()
                print(f"Dosya: {dosya} | Klasör: {klasor} | Satır Sayısı: {len(satirlar)}")



