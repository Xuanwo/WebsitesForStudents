# !/usr/bin/python3
# -*- coding: utf-8 -*-
#This is for hactoberfest. Please dont delete

"""
This script is used to test websites' accessibility

author: Xuanwo
email: xuanwo.cn@gmail.com
"""

import requests
import json

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
    'User-Agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                   'AppleWebKit/537.36 (KHTML, like Gecko) '
                   'Chrome/46.0.2490.86 '
                   'Safari/537.36')
}

with open('badsite.json') as f:
    data = json.load(f)

with open('sites.txt') as site:
    for i in site:
        print(i[:len(i) - 1])  # remove the '\n'
        try:
            # test a website with get method and set timeout 10s and hearers
            r = requests.get(i[:len(i) - 1], timeout=10, headers=headers)
        except:
            # update badsite data
            if i[:len(i) - 1] in data:
                data[i[:len(i) - 1]] += 1
            else:
                data[i[:len(i) - 1]] = 1
        else:
            if r.status_code == requests.codes.ok:
                print("go")
            else:
                print("need verify!")

with open('badsite.json', mode='w') as f:
    json.dump(data, f, indent=4)
