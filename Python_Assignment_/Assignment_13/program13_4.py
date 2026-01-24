# Write one program which contain one function Named as DecimalToBinary()
# which Accept one number and print Binary equivalent


#################################################################
# Function Name : DecimalToBinary
# Description   : Accepts a number and convert Decimal To Binary
# Input         : Integer number
# Output        : print Binary equivalent
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def DecimalToBinary(No):
    Binary = ""

    while No != 0:
        Rem = No % 2
        Binary = str(Rem) + Binary
        No = No // 2

    return Binary


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes DecimalToBinary function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Value = None
    print("Enter the number :")
    Value = int(input())

    Ret = DecimalToBinary(Value)

    print("Binary Equivalent of", Value,"is",Ret)

if __name__ == "__main__":
    main()