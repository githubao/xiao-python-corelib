#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/26 13:35
"""

import os
import subprocess
import sys

def run_cmd(cmd):
    x = subprocess.Popen(cmd,stdout=subprocess.PIPE,shell=True)
    return x.communicate(sys.stdout)

def run3():
    # res = subprocess.check_output(['dir',])
    # print(res)
    print(run_cmd('time'))

def run2():
    print(os.name)
    print(os.system('dir'))

def run():
    st = os.stat(__file__)

    f = open(__file__)
    st2 = os.fstat(f.fileno())

    print(st)
    print(st2)


def main():
    # run()
    # run2()
    run3()


if __name__ == '__main__':
    main()
