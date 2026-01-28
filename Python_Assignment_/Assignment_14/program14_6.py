# Write a lambda function which accept one number and return Ture if it is Odd else False 

#################################################################
# Lambda Function : CheckOdd
# Description     : Accepts one integer as input and returns
#                   True if it is Odd else False using lambda function
# Input           : Integer
# Output          : Boolean (return True if it is Odd else False )
# Author          : Vivek Bhauraj Gautam
# Date            : 20 January 2026
#################################################################
CheckOdd = lambda No: True if No % 2 != 0 else False

#################################################################
# Function Name   : main
# Description     : Accepts a number from user, calls the CheckOdd
#                   lambda function, and displays the result
# Input           : Integer (from user)
# Output          : Boolean if it is True Odd else false
# Author          : Vivek Bhauraj Gautam
# Date            : 20 January 2026
#################################################################
def main():
    Ret = 0

    print("Enter the number :")
    Value = int(input())

    Ret = CheckOdd(Value)

    if Ret == True:
        print(Value,"Is Odd Number")
    else:
        print(Value,"Is Even Number")

if __name__ == "__main__":
    main()