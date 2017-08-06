#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import requests

headers={
    'Cookie':'q_c1=f6075c363b284c2b92fd771a8d7209e9|1499836239000|1499836239000; _zap=e660591c-5bb6-4ea2-a027-24ccce56db7e; d_c0="ACACIGiMFgyPTiGEerm1SP75MgrqhXNi4JI=|1500451632"; cap_id="ZTkzYjNjODlhMDI2NDgwNWI1ZjY1Y2Q4NTg5NDUwNjU=|1501254555|a148df867d91d39a5972dc84c7cee68a3d2f27a6"; l_cap_id="MzQyY2FlMDU4NzRmNDBjNTg1MjM3NTg4ODc4YzgzMjI=|1501254555|827e6ba82354d002773384eb4d37539300b7d393"; auth_type="c2luYQ==|1501254842|45dc00f660c7a6af42f115cf01aa22a6a38787e7"; token="Mi4wMFd5NUtMR0VBNzIyRDJhZTExZTIxMWNVZXN2S0U=|1501254842|ecccd7a95d434a45e9e0db4fc18104c5a495a577"; client_id="NTY2MTgxNTk3Ng==|1501254842|ad4267fd7d27a44420a561337d450476fa084a95"; z_c0=Mi4wQVFDQ2ZYV0VJZ3dBSUFJZ2FJd1dEQmNBQUFCaEFsVk54LUdpV1FEN2xJak1QeFdSM28xR3ZXYWVPQjY5c0QxX0NR|1501254855|0814ec91f6d2700e362621154f5e8b8eadba60c8; _xsrf=891b4b9b-67a4-48ea-a5d5-5f5ed32a483c',
    'Host': 'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'
}

r=requests.get('http://www.zhihu.com',headers=headers)
print(r.text)