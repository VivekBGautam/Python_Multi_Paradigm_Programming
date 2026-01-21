# Write a program which contains one function named as Cube() 
# That accept one number and printCube of that number 

#################################################################
# Function Name : Cube
# Description   : This function which find  Cube of that number
# Input         : No As value to find Cube of that number 
# Output        : Return Cube 
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def Cube(No):
    Square = 0

    Square = No * No * No

    return Square


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes Cube function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Ret = None

    print("Enter first number :")
    Value1 = int(input())
    
    Ret = Cube(Value1)

    print("Cube of :",Value1, "is",Ret)

if __name__ == "__main__":
    main()
