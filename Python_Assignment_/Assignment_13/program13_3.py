# Write one program which contain one function Named as CheckPerfect()
# which Accept one number and check weather it is perfect number or not


#################################################################
# Function Name : CheckPerfect
# Description   : Accepts a number and check it it perfect or not
# Input         : Integer number
# Output        : Return true if it is perfect else return false
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def CheckPerfect(No):
    Sum = 0

    for i in range(1,No):
        if No % i == 0:
            Sum = Sum + i

    if Sum == No:
        return True 
    else:
        return False


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes CheckPerfect function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Value = None
    print("Enter the number :")
    Value = int(input())

    Ret = CheckPerfect(Value)

    if Ret == True:
        print(Value,"is a perfect Number")
    else:
        print(Value,"is Not a perfect Number")

if __name__ == "__main__":
    main()