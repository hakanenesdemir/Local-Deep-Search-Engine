# .txt, .csv, .json, etc. dosyaları açmak için ve bu dosyalar içerisinde işlemler yapmak için
# open() kullanırız.

# open() fonksiyonu 2 arguman alır. 
# file = open('Açılacak dosyanın adı veya yolu', 'Hangi modda açılacağını belirtmek için kullanılır') 

# Basit kullanım örneği f = open("geek.txt", "r") eğer dosya yoksa FileNotFoundError
# file.close() bu with ile açılmayan dosya işlemlerinde kullanılması zorunludur.
# Bu geleneksel yöntemdir. f.close() yani dosyayı kapatmayı unutursak problem çıkar.

# dosyayı açarken tam yol verildiyse tam yol çıktı olarak alınır. Eğer sadece adı girildiyse o çıktı olur
# print("Filename:", f.name)

# # print("Mode:", f.mode) dosyanın hangi mod ile açıldığını verir.

# print("Is Closed?", f.closed) dosyanın kapalıysa f.close() çalıştıysa True kapalı değilse false döner

# Dosyanın tüm içeriğinin okunması için file.read() kullanılır

# f.read(5) ilk 5 harf okunur
# f.readline() il satır döner with ile açılıp bu kod tekrar tekrar çalıştırılırsa bir satır bir satır döner

# Dosya içeriği satır satır yazdırılır
# with open("demofile.txt") as f:
#   for x in f:
#     print(x)

# filemode= w,r,x,a 
# x: Create=> dosya zaten mevcutsa hata döner.

# delete file : os.remove("demofile.txt")

# Dosya var mı yok mu kontrolünden sonra silinebilir.
# import os 
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

#os.rmdir("myfolder") #klasör kaldırdık yalnızca boş klasör


# Burada belgeler/ornek.txt .py ile aynı dizinde olmalı ayrıca terminalde ilgili
# bölge açılmış olmalı
#open için 4 ayrı mod vardır
# r: read
# w: write
# a: append
# x: create

# readline() bir satır okur birden fazla çağırılırsa satırları sırasıyla döndürür.
# with open("ornek.txt", "r", encoding="utf-8") as f:
#     satir1 = f.readline()
#     satir2 = f.readline()

# Burada dosya okunum f'ye atanıyor daha sonra f dosyası içeriği bir satır listesi olduğu için
# her döngüde i değeri start dediğimiz değer satir da f dosyasının satırlarının her biri olmak üzere
# yazdırma işlemi yapılır
# with open("ornek.txt", "r", encoding="utf-8") as f:
#     for i, satir in enumerate(f, start=1):
#         print(f"{i}: {satir.strip()}")

# Yeni bir dosyaya tüm satırları tersten yazdırma
# with open("ornek.txt", "r", encoding="utf-8") as f:
#     satirlar = f.readlines()
# with open("ters_dosya.txt", "w", encoding="utf-8") as f:
#     for satir in reversed(satirlar):
#         f.write(satir)
# readlines() tüm satırları liste olarak verir
# with open("ornek.txt", "r", encoding="utf-8") as f:
#     satirlar = f.readlines()
#     for satir in satirlar:
#         print(satir.strip())  # satır sonu \n silinir



#Örnek:
# file open
f= open("1.1_file_IO/dosyalar/belgeler/ornek.txt","r",encoding="utf-8")

#file read
icerik=f.read()

print(icerik)

#file closed
f.close()