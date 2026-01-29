# Write a program which contais one function named as CheckNum().
# Which accept one number and check weather that number is positive negative or zero

def  CheckNum(No):
    if No > 0:
        print(No," is Positive Number")
    elif No < 0:
        print(No," is Negative number")
    else:
        print(No," is Zero")
    
    
def main():
    Value1 = 0

    Value = int(input("Enter the first number : "))

    CheckNum(Value)

if __name__ == "__main__":
    main()