# ornek.txt dosyasındaki tüm satırları ters sırayla başka bir dosyaya yazın (ters_dosya.txt).

with open("dosyalar/belgeler/ornek.txt","r",encoding="utf-8") as f:
    satirlar=f.readlines()
    print(satirlar)

with open("dosyalar/belgeler/ters_dosya.txt","w",encoding="utf-8") as f:
    for i in reversed(satirlar):
        f.write(f"{i.strip()}\n")