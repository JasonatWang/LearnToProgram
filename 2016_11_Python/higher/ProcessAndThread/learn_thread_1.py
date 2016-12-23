import threading
import time


def loop():
    print('thread %s is running...' % threading.current_thread().name)
    for n in range(1, 6):
        print('thread {0} >>> {1}'.format(threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s is end' % threading.current_thread().name)


if __name__ == '__main__':
    print('thread %s is running' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='LoopThread')
    t.start()
    t.join()
    print('thread %s is end' % threading.current_thread().name)