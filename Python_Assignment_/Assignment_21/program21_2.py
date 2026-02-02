# 2. : Design a Python application that creates two threads.

# Thread 1 should calculate and display the maximum element from an list.
# Thread 2 should calculate and display the minimum element from the same list.
# The list should be accepted from the user.

import threading

def Maximum(List):
    Max = List[0]
    for i in range(len(List)):
        if List[i] > Max: 
            Max = List[i]
    print("Maximum element is : ",Max)

def Minimum(List):
    Min = List[0]
    for i in range(len(List)):
        if List[i] < Min: 
            Min = List[i]
    print("Minimum element is : ",Min)

def main():
    List = [98,27,9,26,18,67,38,54,22,76]

    t1 = threading.Thread(target = Maximum, args = (List,))
    t2 = threading.Thread(target = Minimum, args = (List,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()
