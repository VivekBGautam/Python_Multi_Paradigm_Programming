import multiprocessing
import time
import os

def SumEven(No):
    print("PID of sumEven :",os.getpid())         # 51
    print("PPID of sumeven :",os.getppid())         # 21
    sum = 0

    for i in range(2,No + 1, 2):
        sum = sum + i

    print("Even sum is :",sum)

def SumOdd(No):
    print("PID of sumOdd :",os.getpid())         # 101
    print("PPID of sumOdd :",os.getppid())         # 21
    sum = 0

    for i in range(1,No + 1, 2):
        sum = sum + i

    print("Odd sum is :",sum)

def main():
    print("PID of Main :",os.getpid())         # 21
    print("PPID of Main :",os.getppid())         # 11

    Start_Time = time.time()
    
    t1 = multiprocessing.Process(target = SumEven, args = (100000000,))
    t2 = multiprocessing.Process(target = SumOdd, args = (100000000,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    End_Time = time.time()

    print("Time requird :",End_Time - Start_Time)

if __name__ == "__main__":
    main()