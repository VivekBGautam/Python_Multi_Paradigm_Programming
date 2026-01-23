# Write one program which contain one function Named as PrintSumSubMultDiv()
# which Accept Two number and print Addition Substraction Multiplication And Division


#################################################################
# Function Name : PrintSumSubMultDiv
# Description   : Accepts two number and print Addition Substraction Multiplication And Division
# Input         : Integer number
# Output        : Print Addition Substraction Multiplication And Division
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def PrintSumSubMultDiv(No1,No2):
    # Sum = None
    # Sub = None
    # Mult = None
    # Div = None

    Sum = No1 + No2
    print("Addition is ",Sum)

    Sub = No1 - No2
    print("Substraction is ",Sub)

    Mult = No1 * No2
    print("Multiplication is ",Mult)

    Div = No1 / No2
    print("Division is ",Div)

#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes PrintSumSubMultDiv function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Value1 = None
    Value2 = None

    print("Enter the first number :")
    Value1 = int(input())

    print("Enter the second number :")
    Value2 = int(input())

    PrintSumSubMultDiv(Value1, Value2)

if __name__ == "__main__":
    main()