import threading

print("S087 Akshat Halwai")

class FibonacciThread(threading.Thread):
    def __init__(self, n):
        super().__init__()
        self.n = n
        self.result = []

    def run(self):
        a, b = 0, 1
        for _ in range(self.n):
            self.result.append(a)
            a, b = b, a + b

if __name__ == "__main__":

    values = [4, 5, 6]
    threads = []

    for n in values:
        t = FibonacciThread(n)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()
        print(f"Fibonacci({t.n}) = {t.result}")

    print("\nAll threads completed.")