#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/25 19:33
"""

import os

def run222():
    print(222)

def run():
    file_cnt = 0
    for path, dirs, files in os.walk('.'):
        file_cnt += len(files)

        print(path)
        print(dirs)
        print(files)
        print('*' * 20)

    print(file_cnt)


def main():
    run222()


if __name__ == '__main__':
    main()
    # print(333)
