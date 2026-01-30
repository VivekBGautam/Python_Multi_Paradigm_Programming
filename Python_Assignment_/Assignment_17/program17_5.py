# program17_5

# Write one program which accept one number from user.
# and check weaher number is prime or not

def CheckPrime(No):
    Count = 0
    for i in range(2,No):
        if No % 2 == 0:
            Count += 1

    if Count == 0:
        return True
    else:
        return False

def main():
    Value = int(input("Enter the number : "))

    Ret = CheckPrime(Value)

    if Ret == True:
        print(Value,"it is a prime number")
    else:
        print(Value,"it is not a prime number")

if __name__ == "__main__":
    main()