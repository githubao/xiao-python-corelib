#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/27 17:17
"""

import zlib


def run():
    s = zlib.compress('222'.encode())
    with open('C:\\Users\\BaoQiang\\Desktop\\1.zip', 'wb') as fw:
        fw.write(s)

    with open('C:\\Users\\BaoQiang\\Desktop\\1.zip', 'rb') as f:
        content = f.read()
        print(zlib.decompress(content))


def main():
    run()


if __name__ == '__main__':
    main()
