#!/usr/bin/env python
# encoding: utf-8

"""
@description: os path 模块

@author: BaoQiang
@time: 2017/7/27 11:49
"""

import os

def run7():
    print('text'.count('t'))
    print(list(item for item in dir('') if not item.startswith('__')))

def run6():
    print(os.stat(__file__))


class DirectoryWalker:
    def __init__(self, directory):
        self.stack = [directory]
        self.files = []
        self.index = 0

    def __getitem__(self, item):
        while 1:
            try:
                file = self.files[self.index]
                self.index += 1
            except IndexError:
                self.directory = self.stack.pop()
                self.files = os.listdir(self.directory)
                self.index = 0

            else:
                full_name = os.path.join(self.directory, file)
                if os.path.isdir(full_name) and not os.path.islink(full_name):
                    self.stack.append(full_name)

                return full_name


class A:
    def __getitem__(self, item):
        if item < 100:
            return item
        else:
            raise IndexError('333')
            # raise Exception('222')


def run5():
    s = []
    try:
        raise IndexError()
    except IndexError:
        s.pop()


def run4():
    a = A()
    for item in a:
        print(item)


def run3():
    walker = DirectoryWalker('../')
    print(list(walker))
    # for file in walker:
    #     print(file)


def run2():
    for root, files, dirs in os.walk('../'):
        print(root)
        print(files)
        print(dirs)
        print('*' * 20)


def run():
    file = './__init__.py'

    print(os.path.dirname(file))
    print(os.path.abspath(os.path.dirname(file)))
    print(os.path.splitext(file))

    print(os.path.expanduser('~/hello.py'))
    print(os.path.expandvars('$HOME/hello.py'))


def main():
    # run()
    # run2()
    # run3()
    # run4()
    # run5()
    # run6()
    run7()

if __name__ == '__main__':
    main()
