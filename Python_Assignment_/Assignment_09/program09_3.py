# Write a program which contains one function named as Square() 
# That accept one number and print squre of that number 

#################################################################
# Function Name : Square
# Description   : This function which find  Square of that number
# Input         : No As value to find square of that number 
# Output        : Return Square 
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def Square(No):
    Square = 0

    Square = No * No

    return Square


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes Square function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Ret = None

    print("Enter first number :")
    Value1 = int(input())
    
    Ret = Square(Value1)

    print("Square of :",Value1, "is",Ret)

if __name__ == "__main__":
    main()
