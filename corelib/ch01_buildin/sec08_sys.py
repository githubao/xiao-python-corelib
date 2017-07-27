#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/27 14:57
"""

import sys
import atexit


def clean_up(*args):
    print('clean: ', args)


def run3():
    atexit.register(clean_up)
    atexit.register(clean_up, 2, 3)


class Redirect:
    def __init__(self, stdout):
        self.stdout = stdout

    def write(self, s):
        self.stdout.write(s.lower())

    def flush(self):
        self.stdout.flush()


def run2():
    old_stdout = sys.stdout
    print('Hello')
    sys.stdout = Redirect(sys.stdout)
    print('Hello')
    sys.stdout = old_stdout
    print('Hello')


def run():
    # print('\n'.join(sys.path))
    # print('\n'.join(sys.builtin_module_names))
    # print('\n'.join(sys.modules))
    print(sys.platform)


def main():
    # run()
    # run2()
    run3()


if __name__ == '__main__':
    main()
