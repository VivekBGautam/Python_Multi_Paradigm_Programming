# Write a program which contais one function named as Add().
# Whcih accept Two number id number from user and return addition of that two number

def  Add(No1,No2):
    return No1 + No2

def main():
    Value1 = 0
    Value2 = 0

    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ret = Add(Value1,Value2)
    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()