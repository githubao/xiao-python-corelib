#!/usr/bin/env python
# encoding: utf-8

"""
@description: 

@author: BaoQiang
@time: 2017/7/27 17:44
"""

import threading
from queue import Queue
import time
import random

WORKER_NUM = 10


class Consumer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while 1:
            if self.queue.qsize() > 0:
                item = self.queue.get()
                print('{} get value: {}'.format(threading.current_thread().getName(), item))
                time.sleep(random.randint(10, 100) / 1000)
            else:
                print('{} done'.format(threading.current_thread().getName()))
                break


class Producer(threading.Thread):
    global num

    def __init__(self, queue):
        super().__init__()
        self.queue = queue
        self.index = 0

    def run(self):
        while self.index < 10:
            self.queue.put(self.index)
            self.index += 1


def run():
    queue = Queue()

    for i in range(WORKER_NUM):
        Producer(queue).start()

    for i in range(WORKER_NUM):
        Consumer(queue).start()


def main():
    run()


if __name__ == '__main__':
    main()
