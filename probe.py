# -*- coding: utf-8 -*-
# @Author      : br0therbe
# @Time        : 2023/7/11 8:18
# @Version     : Python 3.10.11
import json
from contextlib import suppress
from pathlib import Path

yun = json.loads(Path('韵.json').read_text('utf-8'))
poem = (Path('poems') / '202312' / '第二方案').read_text('utf-8').strip()
if '}' == poem[-1]:
    poem, con = poem.rsplit('\n', 1)
    poem = poem.strip()
conform = {}
with suppress(Exception):
    for k, vs in json.loads(con).items():
        for v in vs:
            conform[v] = k

pz = ''
more = {}

for line in poem.strip().split('\n'):
    line = line.strip()
    pz += line + '  ->  '
    ys = ''
    for word in line:
        if not word.strip():
            pz += word
            continue
        if word in conform:
            y = conform[word]
        else:
            y = yun[word]['平仄']
            if y == '多':
                more[word] = [w['韵'] for w in yun[word]['韵']]
        ys += y
    pz += f'{ys}  ->  {ys[1]}{ys[3]}{ys[5] if len(ys) > 5 else ""}\n'
print(pz)
print(json.dumps(more, ensure_ascii=False))
