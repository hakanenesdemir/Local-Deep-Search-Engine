# Regex metin içerisindeki belirli kalıpları bulmaya yarayan özel bir dil

# Örneğin:
# "2025-09-30" gibi tarihleri bulmak
# "abc123" içindeki sadece sayıları ayıklamak
# E-postaları doğrulamak
# Log dosyalarındaki "ERROR" satırlarını çekmek

import re
# Bir metin içerisinde python içerisinde kullanılan özel karakterler varsa örneğin \n
# ve bu metni ham haliyle kullanmak istersek başına r getiririz
normal_string_0 = "C:\kullanici\next_file"
normal_string_1 = r"C:\kullanici\next_file"
print(f"İçerisinde özel karakter bulunan String r olmadan: {normal_string_0}")
print(f"İçerisinde özel karakter bulunan String r varken: {normal_string_1}")

# Temel Regex Fonksiyonları

# 1=> re.search(pattern,string)
# metnin içindeki ilk eşleşmeyi bulur.

metin_1 ="Bugün tarih 2025-09-30"
metin_2 = "Telefonlar: 123-456, 987-654"
metin_3 = "Bugün kötü hava kötü , kötü"
metin_4 = "elma, armut;.;.. muz. kiraz"
metin_5 = "İletişim: test@gmail.com, info@firma.com"


# \d{4} 4 tane \d demek oluyor


sonuc=re.search(r"\d{4}-\d{2}-\d{2}",metin_1)
# Eğer ilgili metin içerisinde istenen düzende bir yapı varsa sonuc içerisine tüm bilgiler atanır.
# Eğer ilgili düzende bir metin yoksa none döner bu yüzden sonuc fonksiyonlarını kullanmadan önce none olup olmadığı kontrol edilmelidir.

if sonuc!=None:
    print(sonuc.group()) # Eşleşen ifadenin kendisini (yani metin içindeki tam karşılığını) bir string olarak döndürür.
    print(sonuc.start()) # Başlangıç indeksi
    print(sonuc.end())   # Bitiş indeksi
    print(sonuc.span())  # başlangıç ve bitiş indekslerini içeren bir tuple döndürür.


# Tüm eşleşmeleri liste içerisinde döndürür
sayilar = re.findall(r"\d{3}-\d{3}", metin_2)
print(sayilar)  # ['123-456', '987-654']

#Metin içerisindeki bütün kötü>güzel yapıyor
yeni = re.sub(r"kötü", "güzel", metin_3)
print(yeni)  # Bugün hava güzel

# Metni regex'e göre parçalar
# Burada [] içerisine yazılan her karakterden herhangi biri ayraç olarak kabul edilir
# \s boşluk karakteri
# + birden fazla olduğunu belirtir
liste = re.split(r"[,;.\s]+", metin_4)
print(liste)  # ['elma', 'armut', 'muz', 'kiraz']


emails=re.findall(r"[\w\d]+@[\w\d]+\.[\w]+",metin_5)
# Doğru yaklaşım bu olmalı
# emails=re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}",metin)
print(emails)

# |    Sembol     |       Anlamı                  |
# |      .        | Herhangi bir karakter         |                  
# |      ^        | Başlangıç                     |
# |      $        | Bitiş                         |
# |      \d       | Rakam(0-9)                    |
# |      \D       | Rakam Olmayan                 |
# |      \w       | Harfler,rakamlar,altçizgi(_)  |
# |      \s       | Boşluk karakteri              |
# |      +        | 1 veya daha fazla tekrar      |
# |      *        | 0 veya daha fazla tekrar      |
# |      ?        | 0 veya 1 tekrar               |
# |     {n}       | n kere tekrar                 |
# |    {n,m}      | n ile m arası tekrar          |



