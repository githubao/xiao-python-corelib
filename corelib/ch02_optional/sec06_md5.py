#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/27 17:01
"""

from hashlib import md5
import base64
import crypt

def run2():
    print(crypt.crypt('ba','random_salt'))

def run():
    s = 'secret'
    secret = md5(s.encode()).hexdigest()
    print(secret)
    print(base64.encodebytes(secret.encode()))

def main():
    # run()
    run2()


if __name__ == '__main__':
    main()