# 1.Write a program which accept N numbers from user and store it into List. Return addition of all
# elements from tha List.

def ListAddAndMin(List,No):
    Count = 0 
    for i in range(len(List)):
        if No == List[i]:
            Count = Count + 1
    return Count

def main():
    Value1 = int(input("Enter how many element you want to store in list : "))
    Data = 0
    List = []
    for _ in range(Value1):
        Sum = 0
        Data = int(input())
        List.append(Data)

    Value2 = int(input("Enter the value whose you want to coint frequency : "))

    Ret = ListAddAndMin(Value1,Value2)
    print("Count of ",Value1 ,"is :-> ",Ret)


if __name__ == "__main__":
    main()