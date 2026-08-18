import threading
import time

print("S087 Akshat Halwai")

SIZE = 5

buffer = [None] * SIZE

in_position = 0
out_position = 0

empty = threading.Semaphore(SIZE)
full = threading.Semaphore(0)

mutex = threading.Lock()


def producer():
    global in_position

    for item in range(1, 11):

        empty.acquire()
        mutex.acquire()

        buffer[in_position] = item

        print("Produced:", item)
        print("Buffer:", buffer)

        in_position = (in_position + 1) % SIZE

        mutex.release()
        full.release()

        time.sleep(1)


def consumer():
    global out_position

    for i in range(1, 11):

        full.acquire()
        mutex.acquire()

        item = buffer[out_position]
        buffer[out_position] = None

        print("Consumed:", item)
        print("Buffer:", buffer)

        out_position = (out_position + 1) % SIZE

        mutex.release()
        empty.release()

        time.sleep(2)



start_time = time.time()

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()

print("\nConsumer will start after 5 seconds...\n")
time.sleep(5)

consumer_thread.start()

producer_thread.join()
consumer_thread.join()


end_time = time.time()

total_time = end_time - start_time

print("\nProgram Finished")
print("Total execution time:", round(total_time, 2), "seconds")
