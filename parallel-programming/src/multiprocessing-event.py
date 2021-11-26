import multiprocessing
import time


def wait_for_event(e):
    print("wait_for_event: starting")
    e.wait()
    print("wairt_for_event: e.is_set()->" + str(e.is_set()))


def wait_for_event_timeout(e, t):
    print("wait_for_event_timeout:starting")
    e.wait(t)
    print("wait_for_event_timeout:e.is_set->" + str(e.is_set()))


if __name__ == "__main__":
    e = multiprocessing.Event()
    w1 = multiprocessing.Process(target=wait_for_event, args=(e,))
    w2 = multiprocessing.Process(target=wait_for_event_timeout, args=(e, 6))
    w1.start()
    w2.start()
    time.sleep(10)
    print("main: event setting")
    e.set()
    print("main: event is set")
