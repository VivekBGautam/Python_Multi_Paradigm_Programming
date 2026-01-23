# Write one program which contain one function Named as SumOfDigits()
# which Accept one number and count Sum of digit of that number


#################################################################
# Function Name : SumOfDigits
# Description   : Accepts a number and Count the Sum of digits in that number
# Input         : Integer number
# Output        : Returns Sum of digits in a number 
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def SumOfDigits(No):
    Sum = 0
    while No != 0:
        Digit = No % 10
        Sum = Sum + Digit
        No = int(No / 10)

    return Sum


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes SumOfDigits function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Value = None
    print("Enter the number :")
    Value = int(input())

    Ret = SumOfDigits(Value)

    print("Sum Of Digits of ",Value ," is :",Ret)

if __name__ == "__main__":
    main()