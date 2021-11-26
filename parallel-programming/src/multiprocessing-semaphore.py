import multiprocessing
from multiprocessing import Process, current_process, Semaphore
import time


def worker(s, i):
    s.acquire()
    print(current_process().name + "acquire");
    time.sleep(i)
    print(current_process().name + "release\n");
    s.release()


if __name__ == "__main__":
    multiprocessing.set_start_method('fork')
    s = Semaphore(2)
    for i in range(5):
        p = Process(target=worker, args=(s, i * 2))
        p.start()
