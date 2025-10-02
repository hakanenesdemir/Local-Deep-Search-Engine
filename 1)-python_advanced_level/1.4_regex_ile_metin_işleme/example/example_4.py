# Bir raporlar klasöründe .txt dosyaları var.
# Her dosyanın içindeki e-mail adreslerini bul ve emails.csv dosyasına şu formatta yaz:

# dosya_adi, email
# ornek1.txt, test@gmail.com
# ornek2.txt, info@site.com

from pathlib import Path
import re

p=Path("raporlar")
p1=p/"emails.csv"

with p1.open("w",encoding="utf-8") as emailDosya:
    for txt_dosya in p.rglob("*.txt"):
        with txt_dosya.open("r",encoding="utf-8") as f:
            icerik=f.read()
            mailler=re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",icerik)
            for i in mailler:
                emailDosya.write(f"{txt_dosya.name},{i}\n")