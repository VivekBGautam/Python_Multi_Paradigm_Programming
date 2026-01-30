# program17_9

# Write one program which accept one number from user.
# and return number of digits in that number  

def CountDigits(No):
    Count = 0
    while No != 0:
        Count += 1
        No = int(No / 10)
    return Count

def main():
    Value = int(input("Enter the number : "))

    Ret = CountDigits(Value)

    print("Counts of digits in Value ",Value,"is : -> ",Ret)

if __name__ == "__main__":
    main()