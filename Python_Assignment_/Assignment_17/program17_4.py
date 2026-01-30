# program17_9

# Write one program which accept one number from user.
# and return addition of its factors

def SumFactor(No):
    FactSum = 0
    for i in range(1,int((No/2) + 1)):
        if No % i == 0:
            FactSum = FactSum + i


    return FactSum

def main():
    Value = int(input("Enter the number : "))

    Ret = SumFactor(Value)

    print("Sum Factors of  Value ",Value,"is : -> ",Ret)

if __name__ == "__main__":
    main()