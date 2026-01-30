# program17_9

# Write one program which accept one number from user.
# and return Addition of digits in that number  

def AddOfDigits(No):
    Digit = 0
    Sum = 0
    while No != 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = int(No / 10)
    return Sum

def main():
    Value = int(input("Enter the number : "))

    Ret = AddOfDigits(Value)

    print("Addition of digits in Value ",Value,"is : -> ",Ret)

if __name__ == "__main__":
    main()