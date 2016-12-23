import threading


def add_up():
    return local_add.x1 + local_add.x2


def run_thread(x, y):
    print('Thread {0} is running...'.format(threading.current_thread().name))
    lock.acquire()
    try:
        local_add.x1, local_add.x2 = x, y
        print('The finally result is {0} in {1}'.format(add_up(), threading.current_thread().name))
    finally:
        lock.release()

if __name__ == '__main__':
    print('Thread {0} is running...'.format(threading.current_thread().name))
    th_1 = threading.Thread(target=run_thread, args=(1, 2))
    th_2 = threading.Thread(target=run_thread, args=(4, 9))
    local_add = threading.local()
    lock = threading.Lock()
    th_1.start()
    th_2.start()
    result_1 = th_1.join()
    result_2 = th_2.join()
    print('Thread {0} end'.format(threading.current_thread().name))