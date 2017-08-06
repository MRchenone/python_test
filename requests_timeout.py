#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
r=requests.get('https://www.taobao.com',timeout=None)
print(r.status_code)