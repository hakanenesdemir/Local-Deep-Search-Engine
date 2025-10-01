from pathlib import Path
import re

p=Path("belgeler")
p1=p/ "metin.txt"
a=[]
with p1.open("r",encoding="utf-8") as f:
    for satir in f:
        if re.search("2025",satir):
            print(satir,end="")



"""     metin=f.read()
    a=re.findall(r"^.*2025.*",metin,re.MULTILINE) """



# Yapay zekanın çözümü
# with p1.open("r", encoding="utf-8") as f:
#     for satir in f:
#         if re.search(r"2025", satir):
#             # Eşleşen satırı listeye eklerken sondaki '\n' karakterini .strip() ile temizliyoruz.
#             eslesen_satirlar.append(satir.strip())


