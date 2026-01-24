# Write one program which contain one function Named as CalculateArea()
# which Accept Two number and as length and Width and print Area


#################################################################
# Function Name : CalculateArea
# Description   : Accepts Two number as length and Width and print Area
# Input         : Integer number
# Output        : Print Area of rectangle
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def CalculateArea(Length,Width):
    Area = Length * Width
    return Area

#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes CalculateArea function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Value1 = None
    Value2 = None

    print("Enter length :")
    Value1 = int(input())

    print("Enter weidth :")
    Value2 = int(input())

    Ret = CalculateArea(Value1, Value2)

    print("Area of rectangle is :",Ret)

if __name__ == "__main__":
    main()