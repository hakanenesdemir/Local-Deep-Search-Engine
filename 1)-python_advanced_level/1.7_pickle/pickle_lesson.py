# Pickle (Python’a Özel)
# Özellikleri:
# • Python objelerini binary formatta saklar.
# • JSON/YAML’den farklı olarak sadece Python’da çalışır.
# • Makine öğrenmesinde model kaydetmek/yüklemek için çok kullanılır.

# pickle modülü, JSON'a benzer şekilde dört ana fonksiyon etrafında döner:
# 1)- pickle.dump(obj, file)    Python objesini alıp dosyaya yazar.	                            json.dump()
# 2)- pickle.load(file)	        Dosyadan ikili veriyi okur ve Python objesine dönüştürür.	    json.load()
# 3)- pickle.dumps(obj)	        Python objesini alıp ikili (bytes) bir dize olarak döndürür.	json.dumps()
# 4)- pickle.loads(bytes)	    İkili dizeyi alıp Python objesine dönüştürür.	                json.loads()

# Sınıf Nesnelerini Saklama

import pickle
import os

# Özel bir sınıf tanımlayalım
class Ayar:
    def __init__(self, ad, durum):
        self.ayar_adi = ad
        self.aktif_mi = durum
        self.olusturma_zamani = "Şimdi" # pickle bunu da saklayacak!

# Sınıf örneğini oluşturalım
kullanici_ayari = Ayar("Karanlık Mod", True)
kullanici_ayari.son_guncelleme = "Az Önce" # Dinamik olarak eklenen nitelik

dosya_adi = "ayar.pkl" # İkili dosya uzantısı (pkl: Pickle)

# --- PICKLING (Serileştirme: Python Objesi -> Dosya) ---
print(f"--- '{dosya_adi}' dosyasına yazılıyor (Pickling) ---")
try:
    # Dosyayı ikili yazma modunda aç (wb: write binary)
    with open(dosya_adi, 'wb') as f:
        pickle.dump(kullanici_ayari, f,)
    print("Yazma başarılı.")
except Exception as e:
    print(f"Pickle yazma hatası: {e}")


# --- UNPICKLING (Seri Kaldırma: Dosya -> Python Objesi) ---
print(f"\n--- '{dosya_adi}' dosyasından okunuyor (Unpickling) ---")
okunan_ayar = None
try:
    # Dosyayı ikili okuma modunda aç (rb: read binary)
    with open(dosya_adi, 'rb') as f:
        # Saklanan objeyi geri yükle
        okunan_ayar = pickle.load(f)
    print("Okuma başarılı.")
except Exception as e:
    print(f"Pickle okuma hatası: {e}")


# Yüklenen objeyi kontrol et none ise zaten false döner
if okunan_ayar:
    print(f"Yüklenen Obje Tipi: {type(okunan_ayar)}")
    print(f"Ayar Adı: {okunan_ayar.ayar_adi}")
    print(f"Durumu: {okunan_ayar.aktif_mi}")
    # Dinamik eklediğimiz nitelik de geri geldi!
    print(f"Son Güncelleme: {okunan_ayar.son_guncelleme}") 
    
    #os.remove(dosya_adi) # Örnek dosyayı silinebilir

a1 = pickle.dumps("5")
a2 = pickle.dumps("Hakan")
a3 = pickle.dumps("1")
a4 = pickle.dumps(10)
print(a1)
print(a2)
print(a3)
print(a4)