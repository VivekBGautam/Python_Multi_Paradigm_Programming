# Write one program which contain one function Named as PrintReverseNumber()
# which Accept one number and print many number in reverse order


#################################################################
# Function Name : PrintReverseNumber
# Description   : Accepts a number and print all many number in reverse order
# Input         : Integer number
# Output        : Print all many number in reverse order
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def PrintReverseNumber(No):
    Fact = None

    for i in range(No+1,0,-1):
        print(i)


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes PrintReverseNumber function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Value = None
    print("Enter the number :")
    Value = int(input())

    PrintReverseNumber(Value)

if __name__ == "__main__":
    main()