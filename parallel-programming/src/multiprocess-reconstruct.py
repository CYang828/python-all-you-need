import multiprocessing
import time
import math


def task():
    # 计算密集型
    for _ in range(int(1e7)):
        math.sin(40) + math.cos(40)
    return


if __name__ == '__main__':
    start_time = time.time()
    processes = []
    for _ in range(6):
        p = multiprocessing.Process(target=task)
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("cost time: {:.4f}s".format(time.time() - start_time))
