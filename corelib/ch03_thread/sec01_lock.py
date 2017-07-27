#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/27 17:36
"""

import threading
import time
import random


class Counter:
    def __init__(self):
        self.lock = threading.Lock()
        self.value = 0

    def increase(self):
        self.lock.acquire()
        self.value += 1
        print('{} get value: {}'.format(threading.current_thread().getName(), self.value))
        self.lock.release()


class Worker(threading.Thread):
    def __init__(self, counter):
        super().__init__()
        self.counter = counter

    def run(self):
        for i in range(10):
            self.counter.increase()
            time.sleep(random.randint(10, 100) / 1000)

        print('{} task done'.format(self.getName()))


def run():
    pass


def main():
    counter = Counter()
    for i in range(10):
        Worker(counter).start()


if __name__ == '__main__':
    main()
