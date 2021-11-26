import multiprocessing
from multiprocessing import Process, Lock
import os, time


def work(lock):
    lock.acquire()
    print('%s is running' % os.getpid())
    time.sleep(2)
    print('%s is done' % os.getpid())
    lock.release()


if __name__ == '__main__':
    # python3.8在OSX中存在的一个问题
    # https://docs.python.org/zh-cn/3/library/multiprocessing.html
    multiprocessing.set_start_method('fork')
    lock = Lock()
    for i in range(3):
        p = Process(target=work, args=(lock,))
        p.start()
