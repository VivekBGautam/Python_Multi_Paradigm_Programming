# Write a program which contains one function named as Table() 
# That accept one number and print the Multiplication table of that number

#################################################################
# Function Name : Table
# Description   : This function which print multiplication number of that number
# Input         : No As value 
# Output        : It print multiplication table
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def Table(No):
    for i in range(1,10+1):
        Tab = No * i
        print(Tab)


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes Table function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():

    print("Enter first number :")
    Value1 = int(input())
    
    Table(Value1)
    
if __name__ == "__main__":
    main()
