# belgeler/deneme.txt dosyasının adı,uzantısı, bulunduğu klasör yolunu ekrana yazdıran kod?

from pathlib import Path

p=Path("belgeler") / "deneme.txt"

print(f"Dosyanın adı: {p.name}")
print(f"Dosyanın uzantısı: {p.suffix}")
print(f"Dosyanın bulunduğu klasörün yolu: {p.parent}")