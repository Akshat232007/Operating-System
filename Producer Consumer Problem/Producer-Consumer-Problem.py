from multiprocessing import Process, Queue
import random
import time

def create_data(q):
    count = 1
    while count <= 5:
        value = random.randint(10, 99)
        print("Produced:", value)
        q.put(value)
        time.sleep(0.5)
        count += 1

def use_data(q):
    count = 1
    while count <= 5:
        value = q.get()
        print("Consumed:", value)
        time.sleep(0.7)
        count += 1

if __name__ == "__main__":
    data_queue = Queue()

    producer_process = Process(target=create_data, args=(data_queue,))
    consumer_process = Process(target=use_data, args=(data_queue,))

    producer_process.start()
    consumer_process.start()

    producer_process.join()
    consumer_process.join()

    print("Execution Completed")
