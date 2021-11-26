from multiprocessing import Pool
import time
import math


def task(a):
    # 计算密集型
    for _ in range(int(1e7)):
        math.sin(40) + math.cos(40)
    return


if __name__ == '__main__':
    start_time = time.time()

    with Pool(processes=8) as p:
        res = p.map(task, list(range(6)))
    print("cost time: {:.4f}s".format(time.time() - start_time))
