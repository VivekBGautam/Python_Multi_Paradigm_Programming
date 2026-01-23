# Write one program which contain one function Named as Reverse()
# which Accept one number and reverse that number


#################################################################
# Function Name : Reverse
# Description   : Accepts a number and Reverse that Number
# Input         : Integer number
# Output        : Returns Reversed number 
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def Reverse(No):
    Rev = 0
    while No != 0:
        Digit = No % 10
        Rev = Rev * 10 + Digit
        No = int(No / 10)

    return Rev


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes Reverse function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Value = None
    print("Enter the number :")
    Value = int(input())

    Ret = Reverse(Value)

    print("Reverse number of ",Value ," is :",Ret)

if __name__ == "__main__":
    main()