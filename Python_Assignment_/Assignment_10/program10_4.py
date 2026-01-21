# Write a program which contains one function named as PrintEven() 
# That accept one number and print alll even number till that number

#################################################################
# Function Name : PrintEven
# Description   : This function which print even number till input 
# Input         : No As value 
# Output        : Print Even value till given number 
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def PrintEven(No):
    Fact = 1
    for i in range(1,No+1):
        if i % 2 == 0:
            print(i)

#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes PrintEven function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    
    print("Enter first number :")
    Value1 = int(input())
    
    PrintEven(Value1)
    
if __name__ == "__main__":
    main()
