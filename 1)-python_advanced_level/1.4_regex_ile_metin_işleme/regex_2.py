import re
log = """
[INFO] Sistem başlatıldı
[ERROR] Bağlantı hatası
[WARNING] Bellek düşük
[ERROR] Disk doldu
"""
hatalar = re.findall(r"\[ERROR\].*", log)
print(hatalar)  
# ['[ERROR] Bağlantı hatası', '[ERROR] Disk doldu']

# Adımlar:
# - Desen, metnin başında [ERROR] arar, bulamaz ([INFO] var).
# - \n karakterini atlar ve ilerler.
# - Birinci Eşleşme: [ERROR] Bağlantı hatası kısmını bulur. Nokta (.) operatörü hatası kelimesinden sonraki \n karakterini eşlemediği için, eşleşme tam o satırın sonunda durur.
# - \n[WARNING] kısmını atlar ve ilerler.
# - İkinci Eşleşme: [ERROR] Disk doldu kısmını bulur. Eşleşme, metnin sonuna kadar gider.

# Dipnot: operatörünün varsayılan olarak yeni satır karakterini atlaması sayesinde,
# her bir hata kaydı tek bir satır kaydı gibi ayrı ayrı listelenir.


