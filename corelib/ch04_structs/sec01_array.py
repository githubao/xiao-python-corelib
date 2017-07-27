#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/27 18:21
"""

import array
import sys

def little_endian():
    return ord(str(array.array('i', [1]).tostring()[0]))

def run2():
    print(little_endian())
    print(sys.byteorder)

def run():
    a = array.array('B', range(16))
    print(a)

    b = array.array('i', [2, 3, 4])
    print(b)
    print(repr(b.tostring()))
    print(b.tolist())


def main():
    # run()
    run2()


if __name__ == '__main__':
    main()
