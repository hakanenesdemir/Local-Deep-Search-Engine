# 🔹 1. venv’in Önemi
# Python’da venv (sanal ortam), projeni izole etmek için kullanılır.
# 👉 Neden önemli?
# Her proje farklı Python paket sürümleri isteyebilir.
# Global (tüm sistem) Python ortamına paket yüklemek karışıklık yaratır.
# venv, projeye özel bir Python ortamı yaratır → bağımlılıklar çakışmaz.
# Bir projede Django 4.2 kullanırken, diğerinde Django 5.0 kullanabilirsin.
# Daha güvenli: sistemin Python’una zarar vermezsin.
# Yani: venv = proje için özel, izole edilmiş Python dünyası.

# 🔹 2. venv Nasıl Oluşturulur?
# Bir klasör içinde sanal ortam yaratmak için:
# python -m venv venv

# aktifleştirmek için

# bash(windows):
# venv\Scripts\activate

# Linux/Mac:
# source venv/bin/activate

#Devre dışı bırakmak: deactivate

# Dosya yapısı ve içerikleri
# venv/
# ├── Include/        # (Windows'ta bulunur) C header dosyaları
# ├── Lib/            # Paketlerin kurulduğu yer (site-packages burada)
# │   └── site-packages/
# ├── Scripts/ (Windows) veya bin/ (Linux/Mac)
# │   ├── activate    # Ortamı aktifleştiren script
# │   ├── pip         # Bu ortama özel pip
# │   └── python      # Bu ortama özel python
# ├── pyvenv.cfg      # Ortam ayarlarını tutan dosya


# Bir projede kullanım düzeni
# proje_adi/
# ├── venv/                 # Sanal ortam (genelde .gitignore edilir)
# ├── src/ veya app/        # Kaynak kodların
# │   ├── __init__.py
# │   └── main.py
# ├── requirements.txt      # Ortam bağımlılıklarının listesi
# └── README.md

#=================================================================================================================================================
#       Komut                       |           Anlamı                                                   |       Nerede Çalışır?
# pip freeze > requirements.txt	    |pip freeze, o anda etkin olan sanal ortama (venv)                   |Projenin geliştirildiği bilgisayarda,
#                                   |hangi paketlerin hangi versiyonlarla kurulduğunu listeler.          |venv etkinleştirilmişken.
#                                   |> işareti ise bu çıktıyı terminale yazdırmak yerine,                |   
#                                   |requirements.txt adındaki bir dosyaya kaydetmeye yarar.	         | 

# Önemi:	Bu, projenizin bir "paket listesi manifestosu"dur. Bu dosyayı projenizin kaynak koduna (GitHub/GitLab vb.) dahil edersiniz.


# Alttaki komut requirements.txt içerisinde olan bağımlılıkların yüklenmesini sağlar.
#=================================================================================================================================================

# Komut	                                                Anlamı	                                                         Nerede Çalışır?
# pip install -r requirements.txt	 |pip install komutunun yanındaki -r (recursive veya requirements    |Projenin yeni klonlandığı bilgisayarda, yeni
#                                    |kelimesinden gelir) bayrağı, pip'e tek bir paket kurmak yerine,    |venv etkinleştirildikten sonra. 
#                                    |belirtilen dosyadaki (requirements.txt) tüm paketleri listeye göre |
#                                    |kurmasını söyler.	                                                 |
       
# Önemi:	Bu komut sayesinde, projeyi klonlayan herkes (veya projeyi dağıttığınız sunucu), tek bir komutla projenin ihtiyaç duyduğu yüzlerce paketi (ve doğru versiyonlarını) otomatik olarak kurabilir.

# Kısaca:
# Neden Bu Kadar Önemli?
# Bu iki adım, Python'daki tekrar üretilebilirlik (reproducibility) ilkesinin temelini oluşturur.
#   • Projemi 6 ay sonra a.tığımda, tüm bağımlılıkları hatırlamak zorunda kalmam.
#   • Takım arkadaşımızın projesi, benim bilgisayarımdaki paket versiyonları farklı olduğu için bozulmaz.

# source venv/bin/activate

# Kurulu kütüphanenin sürümünü sanal ortamdaysak kontrol edelim normal bash içerisindeysek kontrol etmek için
# pip show library_name   

# Dosya düzeni böyle olmalı

# local-deepsearch/
# ├── .gitignore
# ├── README.md
# ├── pyproject.toml        # opsiyonel (poetry/modern paketleme)
# ├── requirements.txt      # production deps
# ├── requirements-dev.txt  # geliştirme deps (lint, test tool)
# ├── venv/                 # sanal ortam (genelde .gitignore edilir)
# ├── src/                  # kaynak kod (package layout önerisi)
# │   └── deepsearch/
# │       ├── __init__.py
# │       ├── main.py
# │       └── utils.py
# ├── tests/
# │   └── test_utils.py
# └── scripts/
#     └── dev_run.sh
