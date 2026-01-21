# Write a program which contains one function named as CheckDivisible() 
# That accept one number and check it will  divisibel by 3 or not 

#################################################################
# Function Name : CheckDivisible
# Description   : This function which to check it will divisible by 3 or not
# Input         : No As value to Check which are divisible by 3 or not 
# Output        : It return true if divisible by 3 else retuen false
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def CheckDivisible(No):
    if No % 3 == 0:
        return True
    else:
        return False


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes CheckDivisible function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Ret = None

    print("Enter first number :")
    Value1 = int(input())
    
    Ret = CheckDivisible(Value1)

    if Ret == True:
        print(Value1," is Divisible by 3")
    else:
        print(Value1," is Not divisible by 3")

    
if __name__ == "__main__":
    main()
