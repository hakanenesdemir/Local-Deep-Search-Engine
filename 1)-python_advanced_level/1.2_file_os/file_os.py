import os

# klasör var mı kontrol et, yoksa oluştur
if not os.path.exists("1.2_file_os/yeni_klasor"):
    os.mkdir("1.2_file_os/yeni_klasor")#Klasör oluştur
    print("Yeni klasor oluşturuldu")

dosyalar = os.listdir("1.1_file_IO")
print(dosyalar)  # klasördeki tüm dosyalar

a=0
for klasor_yolu, alt_klasorler, dosyalar in os.walk("1.1_file_IO"):
    print(a)
    a=a+1
    print("Klasör:", klasor_yolu)
    print("Alt klasörler:", alt_klasorler)
    print("Dosyalar:", dosyalar)

# 0
# Klasör: 1.1_file_IO
# Alt klasörler: ['dosyalar', 'example']
# Dosyalar: ['file_IO_1.py', 'file_IO_2.py']
# 1
# Klasör: 1.1_file_IO\dosyalar
# Alt klasörler: ['belgeler', 'resimler']
# Dosyalar: []
# 2
# Klasör: 1.1_file_IO\dosyalar\belgeler
# Alt klasörler: []
# Dosyalar: ['ornek.txt', 'satir_numarali.txt', 'ters_dosya.txt']
# 3
# Klasör: 1.1_file_IO\dosyalar\resimler
# Alt klasörler: []
# Dosyalar: ['bos_resim.jpg', 'night_sky.jpg']
# 4
# Klasör: 1.1_file_IO\example
# Alt klasörler: []
# Dosyalar: ['example_1.py', 'example_2.py', 'example_3.py']

# Birden fazla klasör oluşturma
# os.makedirs("duzenlenmis/altklasor1/altklasor2", exist_ok=True) #exist_ok=True =>varsa hata verme 