#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/27 16:43
"""

import getopt
import getpass

import fnmatch
import glob
import os


def run2():
    # for file in glob.glob('*.py'):
    #     print(file)
    #
    # for file in os.listdir('.'):
    #     if fnmatch.fnmatch(file, '*.py'):
    #         print(file)

    for file in os.listdir('.'):
        if fnmatch.translate('.*py'):
            print(file)


def run():
    s = getpass.getpass('input password: ')
    print(s)


def main():
    # run()
    run2()


if __name__ == '__main__':
    main()
