#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/27 14:33
"""

import operator
from collections import UserList, MutableSequence


def run3():
    lst = [1,2,{'a':1}]
    lst_cp = lst[:]
    lst_cp[2]['a'] = 2
    print(lst)

def run2():
    lst = [1, 2, 3]
    lst2 = [4, 5, 6]

    print(list(map(lambda x, y: x + y, lst, lst2)))
    print(list(map(operator.add, lst, lst2)))


def run():
    u = UserList()
    print(issubclass(UserList, MutableSequence))
    print(callable(UserList))
    print(callable(u))


def main():
    # run()
    # run2()
    run3()


if __name__ == '__main__':
    main()
