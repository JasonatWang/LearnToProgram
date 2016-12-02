from multiprocessing import Pool
import os
import time
import random


def long_time_task(name):
    print('run task %s (%s)' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('task %s run %0.2f second' % (name, (end - start)))

if __name__ == '__main__':
    print('parent process', os.getpid())
    # 这里是限制进程的个数为4, 也就是说一开始只能有4个进程运行,
    # 多于4个的进程必须等到之前进程运行完后运行
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('waiting for subprocesses done')
    # 调用close之后就不能再添加新的进程了
    p.close()
    p.join()
    print('all subprocesses done')