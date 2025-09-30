# 1.2_file_os/ klasöründeki tüm dosya ve alt klasörleri listeleyin.
# Her klasörün ve dosyanın adını ekrana yazdırın.

import os

for klasor,altKlasor,dosya in os.walk("1.2_file_os/"):
    print(klasor)
    print(altKlasor)
    print(dosya)