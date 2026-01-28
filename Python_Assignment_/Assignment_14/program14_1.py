# Write a lambda function which accept one number and return square of that number

#################################################################
# Lambda Function : Square
# Description     : Accepts one integer as input and returns
#                   the square of that number using lambda function
# Input           : Integer
# Output          : Integer (Square of given number)
# Author          : Vivek Bhauraj Gautam
# Date            : 20 January 2026
#################################################################
Square = lambda X: X * X

#################################################################
# Function Name   : main
# Description     : Accepts a number from user, calls the Square
#                   lambda function, and displays the result
# Input           : Integer (from user)
# Output          : Displays square of the given number
# Author          : Vivek Bhauraj Gautam
# Date            : 20 January 2026
#################################################################
def main():
    Ret = 0

    print("Enter the number :")
    Value = int(input())

    Ret = Square(Value)

    print("Suare of ",Value ,"is",Ret)

if __name__ == "__main__":
    main()