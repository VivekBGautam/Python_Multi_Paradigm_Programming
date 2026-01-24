# Write one program which contain one function Named as CircleArea()
# which Accept Redius of circle and print area of a circle


#################################################################
# Function Name : CircleArea
# Description   : Accept Redius of circle and print area of a circle
# Input         : Integer number
# Output        : Print area of circle
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def CircleArea(Redius):
    PI = 3.14

    Area = PI * Redius * Redius

    return Area


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes CircleArea function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Value = None
    print("Enter the radius of circle :")
    Value = int(input())

    Ret = CircleArea(Value)

    print("Area of circle is :",Ret)

if __name__ == "__main__":
    main()