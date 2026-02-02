# 1. : Design a Python application that creates two threads named Prime and NonPrime.

# Both threads should accept a list of integers.
# The Prime thread should display all prime numbers from the list.
# The NonPrime thread should display all non-prime numbers from the list.

import threading

def Check_Prime(Data):
    Count = 0
    for i in range(Data):
        for i in range(2,int(Data / 2)+1):
            if Data % i == 0:
                Count = Count + 1
        if Count == 0:
            return True
        else:
            return False
    
def Prime(List):
    print("Prime number are : ")
    for i in range(len(List)):
        Ret = Check_Prime(List[i])

        if Ret == True:
            print(List[i], end = "  ")
    print()

def Non_Prime(List):
    print("Non prime number are : ")
    for i in range(len(List)):
        Ret = Check_Prime(List[i])

        if Ret == False:
            print(List[i], end = "  ")
    print()

def main():
    List = [2,5,4,7,16,3,10,11,56,23]

    t1 = threading.Thread(target = Prime, args = (List,))
    t2 = threading.Thread(target = Non_Prime, args = (List,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()