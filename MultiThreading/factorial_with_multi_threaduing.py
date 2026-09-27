import threading


print("S087 Akshat Halwai")
def calculate_factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    print(f"[Thread-{number}] Factorial of {number} is: {result}")

numbers = [5, 7, 10, 3, 12]
threads = []

print("Starting Factorial Calculations............")

for num in numbers:
    thread = threading.Thread(target=calculate_factorial, args=(num,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("=== All factorial threads completed! ===")