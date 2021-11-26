import time
import random
import multiprocessing


class Producer(multiprocessing.Process):
    def __init__(self, productList, condition):
        multiprocessing.Process.__init__(self)
        self.productList = productList  # type: List
        self.condition = condition  # type: multiprocess.Condition

    def run(self):
        while True:
            product = random.randint(0, 100)
            with self.condition:
                print("条件锁：被 生产者 获取")
                self.productList.append(product)
                print(f"生产者：产生了 {product}。")
                print("生产者：唤醒消费者线程")
                self.condition.notify()
                print("条件锁：被 生产者 释放")
            time.sleep(1)


class Customer(multiprocessing.Process):

    def __init__(self, productList, condition):
        multiprocessing.Process.__init__(self)
        self.productList = productList  # type: List
        self.condition = condition  # type: multiprocess.Condition

    def run(self):
        while True:
            with self.condition:
                print("条件锁：被 消费者 获取")
                while True:
                    if self.productList:
                        product = self.productList.pop()
                        print(f"消费者：消费了 {product}")
                        break
                    print("消费者：等待生产者")
                    self.condition.wait()
                print("条件锁：被 消费者 释放")


def main():
    manager = multiprocessing.Manager()
    productList = manager.list()
    condition = multiprocessing.Condition()
    process_producer = Producer(productList, condition)
    process_customer = Customer(productList, condition)
    process_producer.start()
    process_customer.start()
    process_producer.join()
    process_customer.join()


if __name__ == '__main__':
    main()
