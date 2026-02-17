import threading
import time

def SumEven(No):
    sum = 0

    for i in range(2,No + 1, 2):
        sum = sum + i

    print("Even sum is :",sum)

def SumOdd(No):
    sum = 0

    for i in range(1,No + 1, 2):
        sum = sum + i

    print("Odd sum is :",sum)

def main():
    Start_Time = time.time()
    
    t1 = threading.Thread(target = SumEven, args = (100000000,))
    t2 = threading.Thread(target = SumOdd, args = (100000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    End_Time = time.time()

    print("Time requird :",End_Time - Start_Time)

if __name__ == "__main__":
    main()