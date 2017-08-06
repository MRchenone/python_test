#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#亲测可用
import requests
r=requests.get('https://d.pcs.baidu.com/file/82e328b778995f3ef7db9a1843351904?fid=2373288888-250528-43775702879086&time=1501073461&rt=sh&sign=FDTAERVY-DCb740ccc5511e5e8fedcff06b081203-%2FSoh18q%2FUvA354%2Bzu%2BMIcZpZ66k%3D&expires=8h&chkv=1&chkbd=0&chkpc=et&dp-logid=4797870709522528848&dp-callid=0&r=163472520')
with open('spiderman.mp4','wb') as f:
    f.write(r.content)
    f.close()
