# -*- coding: utf-8 -*-
# @Author      : br0therbe
# @Time        : 2023/7/17 8:32
# @Version     : Python 3.10.11
import json
from pathlib import Path

words = json.loads(Path('ttt.json').read_text('utf-8'))

nw = {}
for word, yuns in words.items():
    pz = set(yun['平仄'] for yun in yuns)
    if len(pz) > 1:
        pz = '多'
    else:
        pz = list(pz)[0]
    nw[word] = {
        '平仄': pz,
        '韵': yuns
    }

print(json.dumps(nw, ensure_ascii=False))
Path('韵.json').write_text(json.dumps(nw, ensure_ascii=False), encoding='utf-8')
