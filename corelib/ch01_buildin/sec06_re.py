#!/usr/bin/env python
# encoding: utf-8

"""
@description: 正则模块

@author: BaoQiang
@time: 2017/7/27 14:04
"""

import re
import math

text = 'hello python, use PYTHON, this Python'

def run2():
    print(math.hypot(3,4))

    for item in dir(math):
        print(item)


def outer(word):

    def repl_callback(m):
        matched = m.group()
        if matched.isupper():
            return word.upper()
        elif matched.islower():
            return word.lower()
        elif matched[0].isupper():
            return word.capitalize()
        return word

    return repl_callback


def run():
    print(re.sub('python', outer(word='snack'), text,flags=re.IGNORECASE))


def main():
    # run()
    run2()


if __name__ == '__main__':
    main()
