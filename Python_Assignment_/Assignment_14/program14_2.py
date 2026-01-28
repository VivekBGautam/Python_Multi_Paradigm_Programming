# Write a lambda function which accept one number and return Cube of that number

#################################################################
# Lambda Function : Cube
# Description     : Accepts one integer as input and returns
#                   the Cube of that number using lambda function
# Input           : Integer
# Output          : Integer (Cube of given number)
# Author          : Vivek Bhauraj Gautam
# Date            : 20 January 2026
#################################################################
Cube = lambda X: X * X * X

#################################################################
# Function Name   : main
# Description     : Accepts a number from user, calls the Cube
#                   lambda function, and displays the result
# Input           : Integer (from user)
# Output          : Displays Cube of the given number
# Author          : Vivek Bhauraj Gautam
# Date            : 20 January 2026
#################################################################
def main():
    Ret = 0

    print("Enter the number :")
    Value = int(input())

    Ret = Cube(Value)

    print("Cube of ",Value ,"is",Ret)

if __name__ == "__main__":
    main()