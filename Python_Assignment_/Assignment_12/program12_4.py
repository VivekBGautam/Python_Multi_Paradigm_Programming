# Write one program which contain one function Named as PrintNumber()
# which Accept one number and print many number starting from 1


#################################################################
# Function Name : PrintNumber
# Description   : Accepts a number and print all many number starting from 1
# Input         : Integer number
# Output        : Print all many number staring from 1
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def PrintNumber(No):
    Fact = None

    for i in range(1,No+1):
        print(i)


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes PrintNumber function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Value = None
    print("Enter the number :")
    Value = int(input())

    PrintNumber(Value)

if __name__ == "__main__":
    main()