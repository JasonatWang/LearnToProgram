from multiprocessing import Process, Queue
import os
import time
import random


def write(q):
    print('Process to write:', os.getpid())
    for value in ['A', 'B', 'C']:
        print('Put', value, 'to Queue...')
        q.put(value)
        time.sleep(random.random())


def read(q):
    print('Process to read:', os.getpid())
    while True:
        value = q.get(True)
        print('Get', value, 'from Queue...')


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()