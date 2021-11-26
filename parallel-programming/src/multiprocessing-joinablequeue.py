from multiprocessing import Process, JoinableQueue
import time


def reader_proc(queue):
    ## Read from the queue; this will be spawned as a separate Process
    while True:
        msg = queue.get()  # Read from the queue and do nothing
        queue.task_done()


def writer(count, queue):
    for ii in range(0, count):
        queue.put(ii)  # Write 'count' numbers into the queue


if __name__ == '__main__':
    for count in [10 ** 4, 10 ** 5, 10 ** 6]:
        jqueue = JoinableQueue()  # writer() writes to jqueue from _this_ process
        # reader_proc() reads from jqueue as a different process...
        reader_p = Process(target=reader_proc, args=((jqueue),))
        reader_p.daemon = True
        reader_p.start()  # Launch the reader process
        _start = time.time()
        writer(count, jqueue)  # Send a lot of stuff to reader_proc() (in different process)
        jqueue.join()  # Wait for the reader to finish
        print("Sending {0} numbers to JoinableQueue() took {1} seconds".format(count,
                                                                               (time.time() - _start)))
