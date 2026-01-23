# Write one program which contain one function Named as CheckPalindrome()
# which Accept one number and check weather it is palindrome number or not


#################################################################
# Function Name : Reverse
# Description   : Accepts a number and check weather it is palindrome or not
# Input         : Integer number
# Output        : Returns True if it is CheckPalindrome number else return False 
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def CheckPalindrome(No):
    RevNo = 0
    RealNo = No
    while No != 0:
        Digit = No % 10
        RevNo = RevNo * 10 + Digit
        No = int(No / 10)

    print(RevNo)
    if RealNo == RevNo:
        return True
    else:
        return False


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes CheckPalindrome function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Value = None
    print("Enter the number :")
    Value = int(input())

    Ret = CheckPalindrome(Value)

    if Ret == True:
        print(Value ," is A palindrome number")
    else:
        print(Value ," is not A palindrome number")

if __name__ == "__main__":
    main()