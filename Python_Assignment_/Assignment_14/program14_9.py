# Write a lambda function which accept two number and return Multiplication

#################################################################
# Lambda Function : Multiplication
# Description     : Accepts two integer as input and returns
#                   the Multiplication of numbers
# Input           : Integer Integer
# Output          : Integer Multiplication of two number
# Author          : Vivek Bhauraj Gautam
# Date            : 20 January 2026
#################################################################
Multiplication = lambda X, Y:  X * Y

#################################################################
# Function Name   : main
# Description     : Accepts a number from user, calls the Multiplication
#                   lambda function, and displays the result
# Input           : Integer (from user)
# Output          : Displays Multiplication of the given number
# Author          : Vivek Bhauraj Gautam
# Date            : 20 January 2026
#################################################################
def main():
    Ret = 0

    print("Enter the first number :")
    Value1 = int(input())

    print("Enter the Second number :")
    Value2 = int(input())

    Ret = Multiplication(Value1, Value2)

    print("Multiplication of two number is",Ret)

if __name__ == "__main__":
    main()