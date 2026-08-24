import threading
import time

print("S087 Akshat Halwai")

readers = 0
data = 0

mutex = threading.Semaphore(1)
write_lock = threading.Semaphore(1)

def reader(name):
    global readers

    mutex.acquire()
    readers += 1
    if readers == 1:
        write_lock.acquire()
    mutex.release()

    print(name, "is reading")
    time.sleep(1)
    print(name, "finished reading")

    mutex.acquire()
    readers -= 1
    if readers == 0:
        write_lock.release()
    mutex.release()

def writer(name):
    global data

    write_lock.acquire()

    data += 1
    print(name, "is writing")
    time.sleep(1)
    print(name, "finished writing")

    write_lock.release()

threads = []

for i in range(3):
    t = threading.Thread(target=reader, args=("Reader " + str(i + 1),))
    threads.append(t)

for i in range(2):
    t = threading.Thread(target=writer, args=("Writer " + str(i + 1),))
    threads.append(t)

for t in threads:
    t.start()

for t in threads:
    t.join()

print("Final data:", data)