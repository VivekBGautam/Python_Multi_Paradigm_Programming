# Write a program which contains one function named as Factorial() 
# That accept one number and Find Factorial of that number

#################################################################
# Function Name : Factorial
# Description   : This function which find factorial of that number
# Input         : No As value 
# Output        : It return Factorial
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def Factorial(No):
    Fact = 1
    for i in range(1,No+1):
        Fact = Fact * i
    return Fact


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes Factorial function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    
    print("Enter first number :")
    Value1 = int(input())
    
    Ret = Factorial(Value1)

    print("Factorial of ",Value1,"is :",Ret)
    
if __name__ == "__main__":
    main()
