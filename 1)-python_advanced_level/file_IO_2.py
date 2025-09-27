# a-> append: Dosyanın sonuna ekleme yapar.
# "rb" / "wb" ->binary ses dosyaları 
# UTF-8'in Önemi: UTF-8, günümüzde internetin ve yazılımların büyük çoğunluğunun
# kullandığı evrensel bir kodlama standardıdır. Özellikle Türkçe'deki (ğ, ı, ş, ö, ç, ü)
# ve diğer dillerdeki özel karakterleri (Çince, Arapça, Kiril alfabesi vb.) doğru şekilde
# okuyup yazabilmek için bu kodlamayı kullanmalısınız.

# r-> read: Dosyayı sadece okuma (read) amaçlı açtığımızı belirtir.
with open("dosyalar/belgeler/ornek.txt","r",encoding="utf-8") as f:
    icerik=f.read()
    print(icerik)

# w-> write: Dosya mevcutsa içeriği siler, yoksa oluşturur.
#with open("dosyalar/belgeler/ornek.txt","w",encoding="utf-8") as f:
    #f.write("Yeni içerik yazıldı")
    #icerik=f.read()
    #print(icerik)

# "r+" : Dosyayı hem okuma hem de yazma yetkisiyle çağırmak
with open("dosyalar/belgeler/ornek.txt","r+",encoding="utf-8") as f:
    ilk_satir = f.readline().strip()
    print(f"Okunan ilk satır: {ilk_satir}")

    # 2. Yazma için imleci dosyanın sonuna taşıma (opsiyonel)
    # Eğer bu adımı yapmazsanız, yazacağınız şey okuduğunuz içeriğin üzerine yazar.
    # Bu örnekte, dosyanın sonuna ekleme yapmak için imleci sona taşıyalım:
    # f.seek(offset,whence)
    # offset: İmlecin ne kadar hareket edeceğini gösterir
    # whence: Hareketin başlangıç noktasını belirler
    # 0 (VARSAYILAN): Dosyanın başı. (f.seek(0) yazmak yeterlidir.)
    # 1: Geçerli imleç konumu. (Genellikle ikili modda kullanılır.)
    # 2: Dosyanın sonu.

    #f.seek(0, 0) # (0, 0) imleci dosyanın başına taşır.
    f.seek(0, 0)
    f.write("Başşşşaaaa22222222222222baaxx")

    f.seek(0,2) # (0, 2) imleci dosyanın sonuna taşır.
    
    # 3. Yazma (Dosyanın sonuna yeni bir satır ekler)
    f.write("\n--- Güncellendi: Not eklendi.")


# 'night_sky.jpg' adlı ikili dosyayı okuma
#
print("resimler")
with open("dosyalar/resimler/night_sky.jpg", "rb") as f:
    bayt_veri = f.read()
    #print(bayt_veri)
    print(bayt_veri[:10])
    # bayt_veri artık bir <class 'bytes'> nesnesidir.
    # print(bayt_veri[:10])  # -> Çıktı: b'\xff\xd8\xff\xe0\x00\x10JFIF...'
    # byte dizisi olduğu için başında b olması şarttır.