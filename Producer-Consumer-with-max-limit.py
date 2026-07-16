from multiprocessing import Process, Queue
import time
import random

# Producer
def producer(queue):
    for i in range(5):
        item = random.randint(1, 100)
        print(f"Producer produced: {item}")
        queue.put(item)      # Blocks if queue is full
        if queue.full():
            print("Failed to insert")
        time.sleep(0.5)

# Consumer
def consumer(queue):
    for i in range(5):
        time.sleep(2)         # Slow consumer intentionally
        item = queue.get()    # Blocks if queue is empty
        print(f"Consumer consumed: {item}")

if __name__ == "__main__":
    # Queue size limited to 3
    q = Queue(maxsize=3)

    p1 = Process(target=producer, args=(q,))
    p2 = Process(target=consumer, args=(q,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Producer and Consumer have finished.")
