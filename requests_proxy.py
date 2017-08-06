#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
proxies={
    'http':'http://123.169.84.88',
    'https':'http://121.232.145.223',
    'http':'http://121.232.145.33'
}
requests.get('https://www.taobao.com',proxies=proxies)