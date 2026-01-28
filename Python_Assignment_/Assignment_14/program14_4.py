# Write a lambda function which accept two number and return Minimum number

#################################################################
# Lambda Function : Minimum
# Description     : Accepts two integer as input and returns
#                   the Minimum number
# Input           : Integer Integer
# Output          : Integer Minimum
# Author          : Vivek Bhauraj Gautam
# Date            : 20 January 2026
#################################################################
Minimum = lambda X, Y:  X if X < Y else Y

#################################################################
# Function Name   : main
# Description     : Accepts a number from user, calls the Minimum
#                   lambda function, and displays the result
# Input           : Integer (from user)
# Output          : Displays Minimum of the given number
# Author          : Vivek Bhauraj Gautam
# Date            : 20 January 2026
#################################################################
def main():
    Ret = 0

    print("Enter the first number :")
    Value1 = int(input())

    print("Enter the Second number :")
    Value2 = int(input())

    Ret = Minimum(Value1, Value2)

    print("Minimum number is",Ret)

if __name__ == "__main__":
    main()