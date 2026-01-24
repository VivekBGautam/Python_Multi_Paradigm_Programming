# Write one program which contain one function Named as CheckDivision()
# which Accept Marks from user and print divison


#################################################################
# Function Name : CheckDivision
# Description   : Accepts marks and print Division
# Input         : Integer number
# Output        : print Division 
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def CheckDivision(Marks):
    if Marks >= 75 and Marks <= 100:
        print("Distinction")
    elif Marks >= 60 and Marks < 75:
        print("First Division")
    elif Marks >= 50 and Marks <60:
        print("Secondd Division")
    elif Marks < 50:
        print("Fail")
    else:
        print("Invalid Marks please enter marks Between 1 To 100")


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes CheckDivision function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Value = None
    print("Enter the number :")
    Value = int(input())

    CheckDivision(Value)

if __name__ == "__main__":
    main()