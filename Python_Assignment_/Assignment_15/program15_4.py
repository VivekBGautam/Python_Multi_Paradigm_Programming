# Write a lambda function using Filter() which accept a list of number
# And return Addition of numbers 
from functools import reduce

#################################################################
# Function Name : Addition
# Description   : Accepts two numbers and returns their Addition
#                 using lambda function
# Input         : Two Integers
# Output        : Integer (Addition of two numbers)
# Author        : Vivek Bhauraj Gautam
# Date          : 21 January 2026
#################################################################
Addition = lambda X, Y: X + Y


#################################################################
# Function Name : main
# Description   : Entry point of the program. Creates a list
#                 of numbers and applies reduce() with lambda
#                 function to calculate Addition of all elements
# Input         : None
# Output        : Displays original list and Addition result
# Author        : Vivek Bhauraj Gautam
# Date          : 21 January 2026
#################################################################
def main():
    Data = (11, 12, 13, 14, 15)
    print("Actual Data is :", Data)

    #################################################################
    # Function Name : reduce()
    # Description   : Applies the given function (Addition)
    #                 cumulatively to the elements of the iterable
    #                 and returns a single accumulated result
    # Input         : Function and iterable of integers
    # Output        : Integer (Addition of all elements)
    # Author        : Vivek Bhauraj Gautam
    # Date          : 21 January 2026
    #################################################################
    RData = reduce(Addition, Data)
    print("Addition of all elements of list is :", RData)


if __name__ == "__main__":
    main()




# Addition = lambda X , Y: X + Y

# def main():
#     Data = 11,12,13,14,15
#     print("Actual Data is :",Data)

#     FData = list(reduce(Addition, Data))
#     print("Addition of hole lemenets of list is :", FData)

# if __name__ == "__main__":
#     main()