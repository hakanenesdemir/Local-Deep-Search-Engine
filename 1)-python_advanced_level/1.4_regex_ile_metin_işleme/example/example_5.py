# Bütün klasörlerdeki .txt dosyalarını tara
# Bu dosyaların içindeki tüm satırları tara ve sadece büyük harflerle yazılmış kelimeleri (ör. "HATA", "CPU", "RAM") bul.
# Bulunan kelimeleri buyuk_harfler.txt dosyasına tekrarsız (unique) olacak şekilde yaz.

from pathlib import Path
import re

p = Path("belgeler")
p1 = p / "buyuk_harfler.txt"

buyuk_harfler = set() # Tekrarsız olsun diye set kullanıyoruz

for txt_dosya in p.glob("*.txt"):
    with txt_dosya.open("r", encoding="utf-8") as f:
        icerik = f.read()
        bulunan = re.findall(r"\b[A-ZÇĞİÖŞÜ]{2,}\b", icerik)
        buyuk_harfler.update(bulunan)  # set'e ekle (otomatik tekrarsız)

# Sonuçları dosyaya yaz
with p1.open("w", encoding="utf-8") as out_dosya:
    for kelime in sorted(buyuk_harfler):  # alfabetik sıralı
        out_dosya.write(kelime + "\n")
                