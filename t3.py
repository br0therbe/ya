# -*- coding: utf-8 -*-
# @Author      : br0therbe
# @Time        : 2023/7/17 8:10
# @Version     : Python 3.10.11
import json
import re

RE_shen = re.compile(r'\w+声', re.S)


def ppp(text):
    line = text.strip()
    head = RE_shen.search(line)
    print(line)
    print(head)
    psy = head.group(0)
    yun = f'{psy[-3]}韵、{psy[-2:]}'
    sheng = '平' if psy[-2:] == '平声' else '仄'
    print(yun)
    print(sheng)
    start = False
    words = {}
    for word in line[len(psy):]:
        word = word.strip()
        if not word:
            continue
        if word == '[':
            start = True
        elif word == ']':
            start = False
        else:
            if start:
                continue
            if word not in words:
                words[word] = []
            words[word].append({
                '韵': yun,
                '平仄': sheng
            })

    print(json.dumps(words, ensure_ascii=False))
    return words
