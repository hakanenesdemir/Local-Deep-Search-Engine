# 1.2_file_os/ klasöründe "yeni_klasor" adında bir klasör oluşturun.
# Eğer klasör zaten varsa oluşturmayın.

import os

if not os.path.exists("1.2_file_os/yeni_klasor"):
    os.mkdir("1.2_file_os/yeni_klasor")