# Bu geleneksel yöntemdir. f.close() yani dosyayı kapatmayı unutursak problem çıkar.

# file open
# Burada belgeler/ornek.txt .py ile aynı dizinde olmalı ayrıca terminalde ilgili
# bölge açılmış olmalı
f= open("dosyalar/belgeler/ornek.txt","r",encoding="utf-8")

#file read
icerik=f.read()

print(icerik)

#file closed
f.close()