# Bir loglar klasöründe çok sayıda .log dosyası var.
# Her log dosyasındaki "[ERROR]" geçen satırları bulup tum_hatalar.txt adlı bir dosyada topla.

from pathlib import Path
import re

p = Path("loglar")
p1 = p / "tum_hatalar.txt"

with p1.open("w", encoding="utf-8") as hataDosyasi:
    for logDosyasi in p.rglob("*.log"):
        with logDosyasi.open("r", encoding="utf-8") as f:
            icerik = f.read()
            hatalar = re.findall(r".*\[ERROR\].*", icerik)
            for satir in hatalar:
                hataDosyasi.write(satir + "\n")
