import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime


def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))


def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))


if __name__ == '__main__':
    # python3.8在OSX中存在的一个问题
    # https://docs.python.org/zh-cn/3/library/multiprocessing.html
    multiprocessing.set_start_method('fork')
    synchronizer = Barrier(2)
    serializer = Lock()
    Process(name='p1 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)).start()
    Process(name='p2 - test_with_barrier', target=test_with_barrier, args=(synchronizer, serializer)).start()
    Process(name='p3 - test_without_barrier', target=test_without_barrier).start()
    Process(name='p4 - test_without_barrier', target=test_without_barrier).start()
