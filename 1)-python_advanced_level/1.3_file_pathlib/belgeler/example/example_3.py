# veriler/ klasöründeki tüm alt klasörleriyle birlikte .csv uzantılı dosyaları bul ve her birinin tam yolunu ekrana yazdır.

from pathlib import Path

p=Path("veriler")

for csv_dosyalari in p.rglob("*.csv"):
    print(csv_dosyalari)