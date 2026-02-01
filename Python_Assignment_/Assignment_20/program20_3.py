# 3. : Design a Python application that creates two threads named EvenList and OddList.

# Both threads should accept a list of integers as input.
# The EvenList thread should :  
#       Extract all even elements from the list.
#       Calculate and display their sum.
# The OddList thread should:
#       Extract all odd elements from the list.
#       Calculate and display their sum.
# Threads should run concurrently.

import threading 

def EvenList(No):
    EvList = []
    Sum = 0
    for i in range(len(No)):
        if No[i] % 2 == 0:
            Sum = Sum + No[i]
            EvList.append(No[i])

    print("Addition of Even element is ",Sum)
    print(EvList)

def OddList(No):
    OdList = []
    Sum = 0
    for i in range(len(No)):
        if No[i] % 2 != 0:
            Sum = Sum + No[i]
            OdList.append(No[i])

    print("Addition of Odd element is ",Sum)
    print(OdList)

def main():
    List = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

    t1 = threading.Thread(target = EvenList, args = (List,))
    t2 = threading.Thread(target = OddList, args = (List,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()
