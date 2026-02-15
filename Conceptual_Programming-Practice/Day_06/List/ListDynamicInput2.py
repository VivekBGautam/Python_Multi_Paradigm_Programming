
def main():
    Size = 0
    Value = 0
    Sum = 0

    print("Enter the number of element :",Size)
    Size = int(input())

    Data = list()

    print("Eneter the elements :")
    for i in range(Size):
        Value = int(input())
        Data.append(Value)

    print(Data)

    for i in range(Size):
        Sum = Sum + Data[i]

    print("Summetion is :",Sum)
    
if __name__ == "__main__":
    main()