# 4. : Design a Python application that creates two threads.

# Thread 1 should compute the sum of elements from a list.
# Thread 2 should compute the product of elements from the same list.
# Return the results to the main thread and display them.

import threading
SumResult = 0
MultResult = 1 

def Addition(List):
    global SumResult
    Sum = 0
    for i in range(len(List)):
        Sum = Sum + List[i]

    SumResult = Sum

def Multiplication(List):
    global MultResult
    Mult = 1
    for i in range(len(List)):
        Mult = Mult * List[i]

    MultResult = Mult

def main():
    List = [98,27,9,26,18,67,38,54,22,76]

    t1 = threading.Thread(target = Addition, args = (List,))
    t2 = threading.Thread(target = Multiplication, args = (List,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    print("Summetion is : ",SumResult)
    print("Multiplication is : ",MultResult)

if __name__ == "__main__":
    main()