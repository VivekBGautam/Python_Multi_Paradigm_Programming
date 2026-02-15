def Summetion(Arr):
    Sum = 0
    
    for i in range(len(Arr)):
        Sum = Sum + Arr[i]

    return Sum

def main():
    Size = 0
    Value = 0
    Ret = 0

    print("Enter the number of element :")
    Size = int(input())

    Data = list()

    print("Eneter the elements :")

    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print(Data)

    Ret = Summetion(Data)

    print("Summetion is :",Ret)

    
if __name__ == "__main__":
    main()