# Write a lambda function which accept two number and return Maximum number

#################################################################
# Lambda Function : Maximum
# Description     : Accepts two integer as input and returns
#                   the Maximum number
# Input           : Integer Integer
# Output          : Integer Maximum
# Author          : Vivek Bhauraj Gautam
# Date            : 20 January 2026
#################################################################
Maximum = lambda X, Y:  X if X > Y else Y

#################################################################
# Function Name   : main
# Description     : Accepts a number from user, calls the Maximum
#                   lambda function, and displays the result
# Input           : Integer (from user)
# Output          : Displays Maximum of the given number
# Author          : Vivek Bhauraj Gautam
# Date            : 20 January 2026
#################################################################
def main():
    Ret = 0

    print("Enter the first number :")
    Value1 = int(input())

    print("Enter the Second number :")
    Value2 = int(input())

    Ret = Maximum(Value1, Value2)

    print("Maximum number is",Ret)

if __name__ == "__main__":
    main()