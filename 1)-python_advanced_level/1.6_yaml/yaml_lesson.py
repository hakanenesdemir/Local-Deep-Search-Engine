# pip install pyyaml

# Kural: Harici ve güvenilmeyen kaynaklardan gelen YAML dosyalarını okurken daima
# yaml.safe_load() veya yaml.safe_load_all() kullanın.

yaml_veri = """
---
a: 1
---
b: 2
"""

# safe_load_all ile tüm belgeleri okur ve bir liste olarak alır
belgeler = list(yaml.safe_load_all(yaml_veri))

print(belgeler)
# Çıktı: [{'a': 1}, {'b': 2}] 

print(belgeler[0])
# Çıktı: {'a': 1} (İlk belge)

import yaml
from pathlib import Path

p=Path("config.yaml")

data={"db":{"host":"localhost","port":5432}}

with p.open("w",encoding="utf-8") as f:
    yaml.safe_dump(data,f,allow_unicode=True)
    print

with p.open("r",encoding="utf-8") as f:
    # yaml.load() kötü amaçlı kod çalıştırabilir. Onun için kullanma.
    cfg=yaml.safe_load(f)
    print(cfg)

