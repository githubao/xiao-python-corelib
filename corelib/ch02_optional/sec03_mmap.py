#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/27 15:56
"""

import mmap
from collections import UserString

word = b'qw'


def run():
    with open('C:\\Users\\BaoQiang\\Desktop\\1.txt', 'r+') as f:
        with mmap.mmap(f.fileno(), 0) as m:
            m.seek(0)

            loc = m.find(word)
            m[loc:loc + len(word)] = word[::-1]

            m.flush()


def main():
    run()


if __name__ == '__main__':
    main()
