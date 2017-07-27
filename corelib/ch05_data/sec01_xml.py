#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/27 18:45
"""

import xml.etree.ElementTree as et
import requests


def run():
    res = requests.get('http://planet.python.org/rss20.xml').content.decode()
    doc = et.fromstring(res)
    for item in doc.iterfind('channel/item'):
        title = item.findtext('title')
        print(title)


def main():
    run()


if __name__ == '__main__':
    main()
