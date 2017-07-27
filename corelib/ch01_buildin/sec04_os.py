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


def run5():
    cmd = 'notepad'
    args = (__file__,)

    envs = os.environ['PATH']
    for path in envs.split(os.pathsep):
        file = os.path.join(path, cmd) + '.exe'

        try:
            res = os.spawnv(os.P_WAIT, file, (file,) + args)
            print(res)
            return
        except os.error as e:
            # print(e)
            pass


# Linux 运行其他系统命令
def run4():
    # cmd = 'ls'
    # args = ('-l',)

    cmd = 'echo'
    args = ('hello', '>', '1.txt')

    pid = os.fork()

    if not pid:
        os.execvp(cmd, (cmd,) + args)
    print(os.wait())
    # return os.wait()[0]


def run_cmd(cmd):
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    return [line for line in proc.stdout]


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
    # run3()
    run5()


if __name__ == '__main__':
    main()
