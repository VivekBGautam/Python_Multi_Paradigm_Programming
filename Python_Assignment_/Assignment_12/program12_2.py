# Write one program which contain one function Named as Factor()
# which Accept one number and print a factor of that number


#################################################################
# Function Name : Factor
# Description   : Accepts a number and print all factor of that number
# Input         : Integer number
# Output        : Print all factor of given number
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def Factor(No):
    Fact = None

    for i in range(1,No):
        if No % i == 0:
            print(i)


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes Factor function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Value = None
    print("Enter the number :")
    Value = int(input())

    Factor(Value)

if __name__ == "__main__":
    main()