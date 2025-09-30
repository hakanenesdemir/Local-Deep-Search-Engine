# kaç tane .txt dosyası var
from pathlib import Path

p=Path("raporlar")

sayac=0
for i in p.iterdir():
    if i.suffix==".txt":
        sayac+=1
        print(f"{sayac} : {i.name}")

print(f"Toplam {sayac} tane .txt dosyası var")

# Tek düzeyde arama
# for i in p.glob("*.txt"):
#     print(i)
#
# Üst üste arama altklasörler dahil
# for i in p.rglob("*.txt"):
#     print(i)