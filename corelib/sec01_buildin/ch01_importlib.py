#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/25 17:29
"""

import importlib
import glob


def run2():
    for file in glob.iglob('./*.py'):
        print(file)


def run():
    """
    ['__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'hello', 'main']
    :return: 
    """

    module_name = 'ch02_dir'
    ch02 = importlib.import_module('corelib.sec01_buildin.{}'.format(module_name))
    print(dir(ch02))

    print(ch02.__loader__)
    print(ch02.__spec__)

    hello_func = getattr(ch02, 'hello')
    hello_func()


def main():
    run2()


if __name__ == '__main__':
    main()
