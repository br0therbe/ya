import json
from pathlib import Path

file = Path('1.txt')
text = file.read_text('utf-8')
words = {}
for line in text.split('\n'):
    line = line.strip()
    if not line:
        continue
    head, sub_words = line.split('：', 1)
    yun = f'{head[-1]}韵、{head[:2]}'
    sheng = '平' if head[1] == '平' else '仄'
    print(yun)
    print(sheng)
    start = False
    sub_words = sub_words.strip()
    for word in sub_words:
        if word == '[':
            start = True
        elif word == ']':
            start = False
        else:
            if start is True:
                continue
            if word not in words:
                words[word] = []

            words[word].append({
                '韵': yun,
                '平仄': sheng,
            })

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
Path('韵1.json').write_text(json.dumps(nw, ensure_ascii=False), encoding='utf-8')
