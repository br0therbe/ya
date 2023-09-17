# -*- coding: utf-8 -*-
# @Author      : br0therbe
# @Time        : 2023/7/17 7:42
# @Version     : Python 3.10.11
import json
import time
from pathlib import Path

import requests
from lxml import html

from t3 import ppp

url = 'https://sou-yun.cn/QR.aspx'
vs = {"平声": [{"name": "一东", "url": "https://sou-yun.cn/QR.aspx?ct=%e4%b8%9c"},
               {"name": "二冬", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%86%ac"},
               {"name": "三江", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%b1%9f"},
               {"name": "四支", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%94%af"},
               {"name": "五微", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%be%ae"},
               {"name": "六鱼", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%b1%bc"},
               {"name": "七虞", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%99%9e"},
               {"name": "八齐", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%bd%90"},
               {"name": "九佳", "url": "https://sou-yun.cn/QR.aspx?ct=%e4%bd%b3"},
               {"name": "十灰", "url": "https://sou-yun.cn/QR.aspx?ct=%e7%81%b0"},
               {"name": "十一真", "url": "https://sou-yun.cn/QR.aspx?ct=%e7%9c%9f"},
               {"name": "十二文", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%96%87"},
               {"name": "十三元", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%85%83"},
               {"name": "十四寒", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%af%92"},
               {"name": "十五删", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%88%a0"},
               {"name": "一先", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%85%88"},
               {"name": "二萧", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%90%a7"},
               {"name": "三肴", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%82%b4"},
               {"name": "四豪", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%b1%aa"},
               {"name": "五歌", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%ad%8c"},
               {"name": "六麻", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%ba%bb"},
               {"name": "七阳", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%98%b3"},
               {"name": "八庚", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%ba%9a"},
               {"name": "九青", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%9d%92"},
               {"name": "十蒸", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%92%b8"},
               {"name": "十一尤", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%b0%a4"},
               {"name": "十二侵", "url": "https://sou-yun.cn/QR.aspx?ct=%e4%be%b5"},
               {"name": "十三覃", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%a6%83"},
               {"name": "十四盐", "url": "https://sou-yun.cn/QR.aspx?ct=%e7%9b%90"},
               {"name": "十五咸", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%92%b8"}],
      "上声": [{"name": "一董", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%91%a3"},
               {"name": "二肿", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%82%bf"},
               {"name": "三讲", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%ae%b2"},
               {"name": "四纸", "url": "https://sou-yun.cn/QR.aspx?ct=%e7%ba%b8"},
               {"name": "五尾", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%b0%be"},
               {"name": "六语", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%af%ad"},
               {"name": "七麌", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%ba%8c"},
               {"name": "八荠", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%8d%a0"},
               {"name": "九蟹", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%9f%b9"},
               {"name": "十贿", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%b4%bf"},
               {"name": "十一轸", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%bd%b8"},
               {"name": "十二吻", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%90%bb"},
               {"name": "十三阮", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%98%ae"},
               {"name": "十四旱", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%97%b1"},
               {"name": "十五潸", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%bd%b8"},
               {"name": "十六铣", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%93%a3"},
               {"name": "十七筱", "url": "https://sou-yun.cn/QR.aspx?ct=%e7%ad%b1"},
               {"name": "十八巧", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%b7%a7"},
               {"name": "十九皓", "url": "https://sou-yun.cn/QR.aspx?ct=%e7%9a%93"},
               {"name": "二十哿", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%93%bf"},
               {"name": "二十一马", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%a9%ac"},
               {"name": "二十二养", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%85%bb"},
               {"name": "二十三梗", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%a2%97"},
               {"name": "二十四迥", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%bf%a5"},
               {"name": "二十五有", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%9c%89"},
               {"name": "二十六寝", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%af%9d"},
               {"name": "二十七感", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%84%9f"},
               {"name": "二十八俭", "url": "https://sou-yun.cn/QR.aspx?ct=%e4%bf%ad"},
               {"name": "二十九豏", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%b1%8f"}],
      "去声": [{"name": "一送", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%80%81"},
               {"name": "二宋", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%ae%8b"},
               {"name": "三绛", "url": "https://sou-yun.cn/QR.aspx?ct=%e7%bb%9b"},
               {"name": "四寘", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%af%98"},
               {"name": "五未", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%9c%aa"},
               {"name": "六御", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%be%a1"},
               {"name": "七遇", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%81%87"},
               {"name": "八霁", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%9c%81"},
               {"name": "九泰", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%b3%b0"},
               {"name": "十卦", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%8d%a6"},
               {"name": "十一队", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%98%9f"},
               {"name": "十二震", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%9c%87"},
               {"name": "十三问", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%97%ae"},
               {"name": "十四愿", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%84%bf"},
               {"name": "十五翰", "url": "https://sou-yun.cn/QR.aspx?ct=%e7%bf%b0"},
               {"name": "十六谏", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%b0%8f"},
               {"name": "十七霰", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%9c%b0"},
               {"name": "十八啸", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%95%b8"},
               {"name": "十九效", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%95%88"},
               {"name": "二十号", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%8f%b7"},
               {"name": "二十一个", "url": "https://sou-yun.cn/QR.aspx?ct=%e4%b8%aa"},
               {"name": "二十二祃", "url": "https://sou-yun.cn/QR.aspx?ct=%e7%a5%83"},
               {"name": "二十三漾", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%bc%be"},
               {"name": "二十四敬", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%95%ac"},
               {"name": "二十五径", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%be%84"},
               {"name": "二十六宥", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%ae%a5"},
               {"name": "二十七沁", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%b2%81"},
               {"name": "二十八勘", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%8b%98"},
               {"name": "二十九艳", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%89%b3"},
               {"name": "三十陷", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%99%b7"}],
      "入声": [{"name": "一屋", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%b1%8b"},
               {"name": "二沃", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%b2%83"},
               {"name": "三觉", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%a7%89"},
               {"name": "四质", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%b4%a8"},
               {"name": "五物", "url": "https://sou-yun.cn/QR.aspx?ct=%e7%89%a9"},
               {"name": "六月", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%9c%88"},
               {"name": "七曷", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%9b%b7"},
               {"name": "八黠", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%bb%a0"},
               {"name": "九屑", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%b1%91"},
               {"name": "十药", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%8d%af"},
               {"name": "十一陌", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%99%8c"},
               {"name": "十二锡", "url": "https://sou-yun.cn/QR.aspx?ct=%e9%94%a1"},
               {"name": "十三职", "url": "https://sou-yun.cn/QR.aspx?ct=%e8%81%8c"},
               {"name": "十四缉", "url": "https://sou-yun.cn/QR.aspx?ct=%e7%bc%89"},
               {"name": "十五合", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%90%88"},
               {"name": "十六叶", "url": "https://sou-yun.cn/QR.aspx?ct=%e5%8f%b6"},
               {"name": "十七洽", "url": "https://sou-yun.cn/QR.aspx?ct=%e6%b4%bd"}]}
ys = {}
try:
    for key, v in vs.items():
        for n in v:
            name = n['name']
            url = n['url']
            print(name, url)
            resp = requests.get(url)
            root = html.fromstring(resp.text)
            yun = ppp(root.xpath('//div[@class="char"]')[0].xpath('string()'))
            for k, y in yun.items():
                if k in ys:
                    ys[k].extend(y)
                else:
                    ys[k] = y
            time.sleep(1)
except Exception as e:
    print(e)
print(json.dumps(ys, ensure_ascii=False))
Path('ttt.json').write_text(json.dumps(ys, ensure_ascii=False), encoding='utf-8')
