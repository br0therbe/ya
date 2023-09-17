# -*- coding: utf-8 -*-
# @Author      : br0therbe
# @Time        : 2023/7/17 7:59
# @Version     : Python 3.10.11
import json

import requests
from lxml import html

from t3 import ppp

url = 'https://sou-yun.cn/QR.aspx?ct=%e4%b8%9c'
resp = requests.get(url)
root = html.fromstring(resp.text)
yun = ppp(root.xpath('//div[@class="char"]')[0].xpath('string()'))
print(json.dumps(yun, ensure_ascii=False))
