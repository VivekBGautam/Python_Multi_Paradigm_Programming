# 1.Write a program which accept N numbers from user and store it into List. Return addition of all
# elements from tha List.

def ListAddAndMin(List):
    Min = List[0]
    for i in range(len(List)):
        if Min > List[i]:
            Min = List[i]
    return Min

def main():
    Value = int(input("Enter how many element you want to store in list : "))
    Data = 0
    List = []
    for _ in range(Value):
        Sum = 0
        Data = int(input())
        List.append(Data)

    Ret = ListAddAndMin(Value)
    print("Min element is : ",Ret)


if __name__ == "__main__":
    main()