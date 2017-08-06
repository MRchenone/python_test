#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from urllib.parse import urlencode
params={
    'name':'germey',
    'age':22
}
base_url='http://www.baidu.com?'
url=base_url+urlencode(params)
print(url)