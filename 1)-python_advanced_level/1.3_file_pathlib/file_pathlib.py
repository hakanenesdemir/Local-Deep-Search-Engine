from pathlib import Path

#Burada path içine yazılan ilk klasör adı python kodunun çalıştığı dizinde bulunmalı
# ya da tam yol belirtilmeli

p0 = Path("belgeler")     # Belgeler dizin
p1 = p0 / "txt_dosyaları" # Belgeler dizininin alt dizini
p2 = p1 / "deneme2.txt"   # Tam txt yolu

print(p2.name)      # ornek.txt
print(p2.stem)      # ornek   (uzantısız dosya adı)
print(p2.suffix)    # .txt
print(p2.parent)    # belgeler üstteki bütün klasör adları a/b/v/belgeler/ vs ama pat içerisindeki üst klasör bilgisi
print(p2.exists())  # True / False dosya var mı?
print(p2.is_file()) # dosya mı?
print(p2.is_dir())  # klasör mü?
# p2 dosyasının içerisine yazma
p2.write_text("Merhaba Dünya", encoding="utf-8")
print("******************************************************")
# p2 dosyasını okuma
icerik = p2.read_text(encoding="utf-8")
print("read yöntem 1")
print(f"{p2}:{icerik}")

print("******************************************************")
with p2.open("r", encoding="utf-8") as f:
    print("read yöntem 2")
    print(f.read())

print("******************************************************")
print('Bütün alt klasörleri taramak p.rglob("*.txt")')
for txt_dosyalar in p1.rglob("*.txt"):  # alt klasörler dahil
    print(txt_dosyalar)

print("******************************************************")
print("Sadece bir alt klasördeki dosya ve klasörleri listeler")
for altKlasorVeDosyalar in p0.iterdir():
    print(altKlasorVeDosyalar)

for altKlasorVeDosyalar in p1.iterdir():
    print(altKlasorVeDosyalar)


# p3 = Path("klasor") / "altklasor" / "ornek.txt"
# os.path.join("klasor", "altklasor", "ornek.txt")