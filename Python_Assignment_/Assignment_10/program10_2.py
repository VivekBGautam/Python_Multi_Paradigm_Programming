# Write a program which contains one function named as Table() 
# That accept one number and print sum of first N number

#################################################################
# Function Name : Summesion
# Description   : This function which print summ of N number 
# Input         : No As value 
# Output        : It print of first N number
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def Summesion(No):
    Sum = 0
    for i in range(1,No+1):
        Sum = Sum + i
    return Sum


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes Summesion function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    
    print("Enter first number :")
    Value1 = int(input())
    
    Ret = Summesion(Value1)

    print("Sum of First N number is :",Ret)
    
if __name__ == "__main__":
    main()
