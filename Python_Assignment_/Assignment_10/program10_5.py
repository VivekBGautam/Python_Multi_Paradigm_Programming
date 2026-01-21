# Write a program which contains one function named as PrintOdd() 
# That accept one number and print alll Odd number till that number

#################################################################
# Function Name : PrintOdd
# Description   : This function which print Odd number till input 
# Input         : No As value 
# Output        : Print Odd value till given number 
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def PrintOdd(No):
    Fact = 1
    for i in range(1,No+1):
        if i % 2 != 0:
            print(i)

#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes PrintOdd function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    
    print("Enter first number :")
    Value1 = int(input())
    
    PrintOdd(Value1)
    
if __name__ == "__main__":
    main()
