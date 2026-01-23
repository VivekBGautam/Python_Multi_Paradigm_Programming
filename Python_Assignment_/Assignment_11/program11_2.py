# Write one program which contain one function Named as CountDigit()
# which Accept one number and count digit of that number


#################################################################
# Function Name : CountDigit
# Description   : Accepts a number and checks How many digits in that number
# Input         : Integer number
# Output        : Returns How many digits in a number 
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def CountDigit(No):
    Count = 0

    while No != 0:
        Count += 1
        No = int(No / 10)

    return Count


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes CountDigit function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Value = None
    print("Enter the number :")
    Value = int(input())

    Ret = CountDigit(Value)

    print("In ",Value ,"Total Number of Digits is :",Ret)  

if __name__ == "__main__":
    main()