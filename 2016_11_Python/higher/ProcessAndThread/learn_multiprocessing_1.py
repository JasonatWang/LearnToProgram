from multiprocessing import Process
import os


def run_process(name):
    print('run child process %s (%s)' % (name, os.getpid()))

if __name__ == '__main__':
    print('parent process', os.getpid())
    # 创建一个进程，target是指向一个函数，args是函数的参数元组，当元组的值只有一个时最后还需要加逗号
    p = Process(target=run_process, args=('test',))
    print('child process will start')
    p.start()
    p.join()
    print('child process ends.')