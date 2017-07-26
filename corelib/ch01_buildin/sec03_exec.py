#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/25 18:29
"""

from corelib import tmp


def run3():
    __import__('corelib.tmp')

    with open('../tmp.py', 'r', encoding='utf-8') as f:
        code = compile(f.read(), '../tmp.py', 'exec')

        exec(code)


def run2():
    body = """
print('hell')
    """
    code = compile(body, '<script>', 'exec')
    print(code)
    exec(code)


def run():
    s = '__import__("os").getcwd()'
    print(eval(s))
    # 限制可以导入的所有模块
    # print(eval(s, {'__builtins__': {}}))


def main():
    # run()
    # run2()
    run3()


if __name__ == '__main__':
    main()
