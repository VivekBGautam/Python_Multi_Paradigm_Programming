# 1. : Design a Python application that creates two separate threads named Even and Odd.

# The Even thread should display the first 10 even numbers.
# The Odd thread should display the first 10 odd numbers.
# Both threads should execute independently using the threading module.
# Ensure proper thread creation and execution.

import threading

def PrintEven(No):
    print("Even number is : ")
    for i in range(1,No+1):
        if i % 2 == 0:
            print(i)

def PrintOdd(No):
    print("Odd number is : ")
    for i in range(1,No+1):
        if i % 2 != 0:
            print(i)

def main():
    Value = 0

    Value = int(input("Enter the number : "))

    t1 = threading.Thread(target = PrintEven, args = (Value,))
    t2 = threading.Thread(target = PrintOdd, args = (Value,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()