#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/27 18:00
"""

import pipes
import signal
import time


def handler(signo, frame):
    print('got signo: ', signo)


def run2():
    signal.signal(signal.SIGTERM, handler)

    time.sleep(1)

    print('end')


def run():
    t = pipes.Template()
    t.append('sort', '--')
    t.append('uniq', '--')
    t.copy('samples/sample.txt', '')


def main():
    run2()


if __name__ == '__main__':
    main()
