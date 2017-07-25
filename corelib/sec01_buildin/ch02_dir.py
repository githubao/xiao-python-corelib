#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/25 17:31
"""

import json


a = 1

class C:
    c = 1
    def __init__(self,d):
        self.d = d

def run3():
    """
    命名空间的字典
    :return: 
    """

    b = 2

    print(vars())
    print(locals())
    print(globals())
    print(vars(C))

def run2():
    print(isinstance(1,object))
    print(issubclass(int,object))

def run():
    """
    模块，类，实例 的所有成员列表
    :return: 
    """
    print(dir([]))
    print(dir(json))


def hello():
    print('ch02 run')


def main():
    # run()
    # run2()
    run3()


if __name__ == '__main__':
    main()
