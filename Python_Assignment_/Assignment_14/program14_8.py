# Write a lambda function which accept two number and return Addition

#################################################################
# Lambda Function : Addition
# Description     : Accepts two integer as input and returns
#                   the Addition of numbers
# Input           : Integer Integer
# Output          : Integer Addition of two number
# Author          : Vivek Bhauraj Gautam
# Date            : 20 January 2026
#################################################################
Addition = lambda X, Y:  X + Y

#################################################################
# Function Name   : main
# Description     : Accepts a number from user, calls the Addition
#                   lambda function, and displays the result
# Input           : Integer (from user)
# Output          : Displays Addition of the given number
# Author          : Vivek Bhauraj Gautam
# Date            : 20 January 2026
#################################################################
def main():
    Ret = 0

    print("Enter the first number :")
    Value1 = int(input())

    print("Enter the Second number :")
    Value2 = int(input())

    Ret = Addition(Value1, Value2)

    print("Addition of two number is",Ret)

if __name__ == "__main__":
    main()