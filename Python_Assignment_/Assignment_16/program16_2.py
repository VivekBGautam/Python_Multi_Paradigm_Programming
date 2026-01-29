# Write a program which contais one function named as checkNum().
# Whcih accept one parameter as number if number is even then it should display " Even  number "
# Otherwise Display " Odd number " on console

def  CheckNum(No):
    if No % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")

def main():
    Value = 0

    Value = int(input("Enter the number : "))

    CheckNum(Value)

if __name__ == "__main__":
    main()