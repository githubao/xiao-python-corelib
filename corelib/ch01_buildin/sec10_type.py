#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/27 15:26
"""

import types
import inspect

def run():
    print(isinstance(1,int))
    print(type(1) == int)
    print(type(1) is int)

    print(inspect.isclass(int))

def main():
    run()


if __name__ == '__main__':
    main()