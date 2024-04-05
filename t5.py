# -*- coding: utf-8 -*-
# @Author      : br0therbe
# @Time        : 2023/8/6 8:38
# @Version     : Python 3.10.11
import re
from pathlib import Path

RE_han = re.compile(r'[\u4e00-\u9fa5]')
content = Path('全唐诗.txt').read_text('utf-8')
hanz = {}
for han in RE_han.findall(content):
    hanz[han] = hanz.get(han, 0) + 1

hanz = dict(sorted(hanz.items(), key=lambda x: -x[1]))
hanz = list(hanz.keys())
for i in range(0, len(hanz), 25):
    print(''.join(hanz[i:i+25]))
