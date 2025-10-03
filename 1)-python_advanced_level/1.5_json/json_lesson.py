# json modülü, temel olarak dört ana fonksiyon etrafında döner:

# json.dumps() : Python nesnesini alıp tek bir JSON dizesi (string) olarak döndürür. 

import json
import datetime

python_sozluk = {
    "isim": "Python",
    "yıl": 1991,
    "versiyon": 3.10,
    "aktif": True,
    "etiketler": ["oop", "scripting"]
}

# Serileştirme: Python Sözlüğünü JSON dizesine dönüştür
json_dizesi = json.dumps(python_sozluk)

print(type(json_dizesi))  # <class 'str'>
print(json_dizesi)

# Veriyi bir dosyaya yazma
with open('veri.json', 'w', encoding='utf-8') as f:
    # ensure_ascii: Varsayılan olarak True'dur. True olduğunda, Türkçe karakterler (ç, ğ, ı, ö, ş, ü) gibi ASCII dışı karakterler 
    # Unicode kaçış dizileri (\u....) olarak kodlanır. Bu karakterlerin okunabilir şekilde yazılması için False yapılmalıdır.
    # 'indent=4' çıktıyı okunur hale getirmek için girinti ekler
    json.dump(python_sozluk, f, ensure_ascii=False, indent=4) #sort_keys=True anahtarları sıralar

    # Virgül ve iki nokta üst üste arasında boşluk bırakılmaz seperators
    #json.dumps(data, separators=(',', ':'))

# Seri Kaldırma (JSON Dizesinden Python Nesnesine)
# json.loads(): JSON formatındaki bir dizeyi (string) alıp, karşılık gelen Python nesnesine (sözlük/liste) dönüştürür.
# 

# Seri kaldırma: JSON dizesini Python Sözlüğüne dönüştür
python_nesnesi = json.loads(json_dizesi)

print(type(python_nesnesi))  # <class 'dict'>
print(python_nesnesi['isim']) # Çıktı: Python

# Dosyadan veri okuma
with open('veri.json', 'r', encoding='utf-8') as f:
    # Dosyadaki JSON verisini doğrudan Python Sözlüğüne yükler
    yuklenen_veri = json.load(f)

print(type(yuklenen_veri))  # <class 'dict'>
print(yuklenen_veri['etiketler'][0]) # Çıktı: oop


liste = [
    {"urun_adi": "Akıllı Saat", "fiyat": 7500.0, "indirimli": True},
    {"urun_adi": "Kablosuz Kulaklık", "fiyat": 2500.0, "indirimli": False},
    {"urun_adi": "Telefon Kılıfı", "fiyat": 150.0, "indirimli": True},
]

with open("data.jsonl", "w", encoding="utf-8") as out:
    for obj in liste:
        out.write(json.dumps(obj, ensure_ascii=False) + "\n")

# oku
okunan_veriler = []
with open("data.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        obj = json.loads(line)
        okunan_veriler.append(obj)

print("Yazılan Kayıt Sayısı:", len(okunan_veriler))
print("Okunan İlk Kayıt:", okunan_veriler[0])

# Karşılaşılan problem: Python nesneleri JSON değil
# datetime, numpy array, özel sınıflar doğrudan JSON’a dönmez. Çözüm:
# Basit: serileştirilebilir tiplere dönüştür (datetime → ISO string).
# Gelişmiş: default parametresi ile custom encoder:

# Python'daki datetime veya date nesneleri standart JSON tipleri değildir.
# Bu nesneleri JSON'a dönüştürürken de yine TypeError alırsınız.
# En iyi uygulama, bu nesneleri serileştirmeden önce ISO 8601 formatında bir dizeye (string) dönüştürmektir.

def default(o):
    if isinstance(o, datetime.datetime):
        return o.isoformat()
    raise TypeError

with open("data.jsonl", "w", encoding="utf-8") as out:
    for obj in liste:
        out.write(json.dumps(obj, ensure_ascii=False) + "\n")
        
json.dumps({"t": datetime.datetime.now()}, default=default)




class Calisan:
    def __init__(self, ad, pozisyon):
        self.ad = ad
        self.pozisyon = pozisyon
        self.yil = 2023 # JSON'a aktarmak istemediğimiz bir veri

# Dönüştürücü fonksiyon
def calisan_to_json(obj):
    # Eğer nesne Calisan tipindeyse, onu bir sözlüğe dönüştür
    if isinstance(obj, Calisan):
        # Yalnızca istediğimiz alanları alıyoruz
        return {"ad": obj.ad, "pozisyon": obj.pozisyon}
    # Başka bilinmeyen tipler gelirse, hata fırlatmasını sağlayabiliriz
    raise TypeError(f"'{type(obj).__name__}' tipinde nesne serileştirilemiyor.")

# Kullanım:
personel = Calisan("Ali", "Geliştirici")

# 'default' argümanı ile kendi fonksiyonumuzu çağırıyoruz
json_veri = json.dumps(personel, default=calisan_to_json,ensure_ascii=False, indent=4)

print(json_veri)



gecersiz_json = '{"isim": "Ayşe" ... }'

try:
    data = json.loads(gecersiz_json)
except json.JSONDecodeError as e:
    print(f"Hata: Geçersiz JSON formatı. Detay: {e}")
    # Hata durumunda varsayılan bir değer atayabilir veya loglama yapabilirsiniz
    data = {}