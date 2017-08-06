#!/usr/bin/env python3
# -*- coding:utf-8 -*-
from urllib.parse import urlunsplit
data=['http','www.baidu.com','index.html','a=6','comment']
print(urlunsplit(data))