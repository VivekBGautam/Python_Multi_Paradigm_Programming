# Write one program which contain one function Named as CheckPrime()
# which Accept one number and check that number is prime or not


#################################################################
# Function Name : CheckPrime
# Description   : Accepts a number and checks whether it is prime or not
# Input         : Integer number
# Output        : Returns True if number is prime, otherwise False
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def CheckPrime(No):
    Count = 0

    if No <= 1:
        return

    for i in range(1,int(No/2)):
        if No % i == 0:
            Count += 1

    if Count == 1:
        return True 
    else:
        return False

#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes CountDigit function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Value = None
    print("Enter the number :")
    Value = int(input())

    Ret = CheckPrime(Value)

    if Ret == True:
        print(Value, " is a prime Number ")
    else:
        print(Value, " is not a prime Number ")

if __name__ == "__main__":
    main()