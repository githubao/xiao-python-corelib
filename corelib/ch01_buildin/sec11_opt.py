#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/27 15:33
"""

from collections import UserDict
import random
from io import StringIO

def run3():
    s = StringIO('1\n2\n3\n')
    for line in s:
        print(line,end='')

def run2():
    print(random.random())
    print(random.sample([1, 3, 4, 2],2))
    print(random.randint(1, 3))


class MyDict(UserDict):
    pass


def run():
    dic = MyDict()
    print(dir(dic))


def main():
    # run()
    # run2()
    run3()


if __name__ == '__main__':
    main()
