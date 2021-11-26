from multiprocessing import Process
import os, time


def work():
    print('%s is running' % os.getpid())
    time.sleep(2)
    print('%s is done' % os.getpid())


if __name__ == '__main__':
    for i in range(3):
        p = Process(target=work)
        p.start()
