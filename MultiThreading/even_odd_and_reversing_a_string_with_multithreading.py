import threading


print("S087 Akshat Halwai")
def print_even_odd(limit):
    print("--- [Task 1] Printing Even/Odd Numbers ---")
    for i in range(1, limit + 1):
        status = "Even" if i % 2 == 0 else "Odd"
        print(f"[Even/Odd Thread] {i} is {status}")
    print("--- [Task 1] Finished ---")

def reverse_string(text):
    print("--- [Task 2] Reversing String ---")
    reversed_text = text[::-1]
    print(f"[String Thread] Original: '{text}' | Reversed: '{reversed_text}'")
    print("--- [Task 2] Finished ---")

number_limit = 10
input_string = "MultithreadingInPython"

t1 = threading.Thread(target=print_even_odd, args=(number_limit,))
t2 = threading.Thread(target=reverse_string, args=(input_string,))

t1.start()
t2.start()

t1.join()
t2.join()

print("=== All concurrent tasks completed! ===")