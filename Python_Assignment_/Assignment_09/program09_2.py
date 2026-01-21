# Write a program which contains one function named as ChkGreater() 
# That accept two number and prints the greater number

#################################################################
# Function Name : ChekGreater
# Description   : This function check creater number and return it
# Input         : No1 , No2 (Two values)
# Output        : Return Greater number
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def ChekGreater(No1,No2):
    if No1 > No2:
        return No1
    else:
        return No2


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes ChekGreater function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Ret = None

    print("Enter first number :")
    Value1 = int(input())

    print("Enter Second number :")
    Value2 = int(input())
    
    Ret = ChekGreater(Value1 ,Value2)

    if Ret == Value1:
        print(Value1," is greater")
    else:
        print(Value2," is greater")

if __name__ == "__main__":
    main()
