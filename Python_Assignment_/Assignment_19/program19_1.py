# 1.Write a program which accept N numbers from user and store it into List. Return addition of all
# elements from tha List.

def ListAdd(List):
    Sum = 0
    for i in range(len(List)):
        Sum = Sum + List[i]

    return Sum

def main():
    Value = int(input("Enter how many element you want in list :"))

    Data = 0
    List = []
    for _ in range(Value):
        Sum = 0
        Data = int(input())
        List.append(Data)

    Ret = ListAdd(Value)
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()