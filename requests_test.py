#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests
r=requests.get('http://httpbin.org/get')
print(type(r.text))
print(r.json())
print(type(r.json()))
