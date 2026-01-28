# Write a lambda function using Filter() which accept a list of number
# And return list of Odd number 

#################################################################
# Function Name : CheckOdd
# Description   : Accepts List of number and returns the Odd of
#                 that list number using lambda function
# Input         : Integer
# Output        : Integer (Even number)
# Author        : Vivek Bhauraj Gautam
# Date          : 21 January 2026
#################################################################
CheckOdd = lambda X: (X % 2 != 0)

#################################################################
# Function Name : main
# Description   : Entry point of the program. Creates a list
#                 of numbers, applies filter() with lambda function
#                 to Check Odd element and displays the result
# Input         : None
# Output        : Displays original and Odd list
# Author        : Vivek Bhauraj Gautam
# Date          : 21 January 2026
#################################################################
def main():
    Data = (11, 12, 13, 14, 15)
    print("Actual Data is :", Data)

    #################################################################
    # Function Name : filter()
    # Description   : Applies the given function (CheckOdd) to each
    #                 element of the input iterable and returns
    #                 a new iterable containing Odd values
    # Input         : Function and iterable of integers
    # Output        : Iterable of Odd integers
    # Author        : Vivek Bhauraj Gautam
    # Date          : 21 January 2026
    #################################################################
    FData = list(filter(CheckOdd, Data))
    print("Data after filter is :", FData)

if __name__ == "__main__":
    main()



# CheckOdd = lambda X: ( X % 2 == 0 )

# def main():
#     Data = 11,12,13,14,15
#     print("Actual Data is :",Data)

#     FData = list(filter(CheckOdd, Data))
#     print("Data after filter is :", FData)

# if __name__ == "__main__":
#     main()