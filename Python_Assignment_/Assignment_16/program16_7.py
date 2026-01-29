# Write a program which contais one function named as CheckDiv().
# Which accept one number and return true is number is divisible by 5 otherwise false

def  CheckDiv(No):
    if No % 5 == 0:
        return True
    else:
        return False
    
    
def main():
    Value1 = 0

    Value = int(input("Enter the first number : "))

    Ret =CheckDiv(Value)

    if Ret == True:
        print(Value ," is Divisible by 5")
    else:
        print(Value ," is Not Divisible by 5")

if __name__ == "__main__":
    main()