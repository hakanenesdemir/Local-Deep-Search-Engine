
from pathlib import Path
import re

p=Path("belgeler")
numaralar=[]
for txt_dosya in p.rglob("*.txt"):
    #print(txt_dosya.name)
    with txt_dosya.open("r",encoding="utf-8") as f:
        icerik = f.read()
        # 05xx-xxx-xxxx formatı
        numaralar = re.findall(r"05\d{2}-\d{3}-\d{4}", icerik)
        if numaralar:  # eğer bulunduysa
            print(f"Dosya: {txt_dosya.name} | Telefonlar: {numaralar}")
"""         metin=f.read()
        numaralar+=re.findall(r"05\d{2}-\d{3}-\d{4}",metin,re.MULTILINE)
        #print(f.read()+"\n")
print(numaralar) """