#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/27 16:28
"""

from io import StringIO
import traceback
import sys
import errno

def run2():
    try:
        raise ValueError('nothing')
    except ValueError as e:
        print(sys.exc_info())
        for file, lineno, func, text in traceback.extract_tb(sys.exc_info()[2]):
            print(file, lineno, func, text, sep='\n')


def run():
    try:
        raise ValueError('nothing')
    except:
        s = StringIO()
        traceback.print_exc(file=s)
        print(s.getvalue())


def main():
    # run()
    run2()


if __name__ == '__main__':
    main()
