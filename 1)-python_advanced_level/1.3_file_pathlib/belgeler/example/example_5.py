# arsiv/ klasöründe şu işlemleri yapan bir kod yaz:
# 1)- Tüm .txt dosyalarını bul.
# 2)- İçinde "ERROR" kelimesi geçen satırları yakala.
# 3)- Bu satırları hata_raporu.txt adlı yeni bir dosyaya yaz.

from pathlib import Path

p=Path("arsiv")
p1=p / "hata_raporu.txt"
if(p1.exists):
    print("true")


with p1.open("w", encoding="utf-8") as rapor:                   # Yazma modunda aç
    for txt_dosyasi in p.glob("*.txt"):                         # Bütün txt dosyalarını bul
        with txt_dosyasi.open("r", encoding="utf-8") as f:      # txt dosyalarını okuma modunda aç
            for satir in f:                                     # her txt dosyasının satırlarını al
                if "HATA" in satir:                             # içerisinde HATA yazıyor mu diye kontrol et
                    rapor.write(f"{txt_dosyasi.name}: {satir}") # p1 ile açtığımız dosyanın içerisine yaz