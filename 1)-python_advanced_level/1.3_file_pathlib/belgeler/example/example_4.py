# Bir klasörde bulunan tüm .log dosyalarının içeriğini oku, dosya adını ve satır sayısını ekrana yazdır.
from pathlib import Path

p=Path("loglar")
for logDosyasi in p.glob("*.log"):
    with logDosyasi.open("r", encoding="utf-8") as f:
        satirSayisi = len(f.readlines())
    print(f"Dosya : {logDosyasi.name} | Satır Sayısı: {satirSayisi}")