#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/25 19:33
"""

import os
import json


def run3():
    with open('C:\\Users\\BaoQiang\\Desktop\\duitang.json', 'r', encoding='utf-8') as f, \
            open('C:\\Users\\BaoQiang\\Desktop\\out.txt', 'w', encoding='utf-8') as fw:
        for line in f:
            json_data = json.loads(line.strip())
            item_lst = (str(item).strip().replace('\n','').replace('\r','') for item in json_data.values())
            fw.write('{}\n'.format('\t'.join(item_lst)))


def run2():
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
    run3()


if __name__ == '__main__':
    main()
