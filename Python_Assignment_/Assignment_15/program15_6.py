# Write a lambda function using Filter() which accept a list of number
# And return Minimum of numbers 
from functools import reduce

#################################################################
# Function Name : Minimum
# Description   : Accepts two numbers and returns their Maximum
#                 using lambda function
# Input         : Two Integers
# Output        : Integer (Minimum of two numbers)
# Author        : Vivek Bhauraj Gautam
# Date          : 21 January 2026
#################################################################
Minimum = lambda X, Y: X if X < Y else Y


#################################################################
# Function Name : main
# Description   : Entry point of the program. Creates a list
#                 of numbers and applies reduce() with lambda
#                 function to calculate Minimum of all elements
# Input         : None
# Output        : Displays original list and Minimum result
# Author        : Vivek Bhauraj Gautam
# Date          : 21 January 2026
#################################################################
def main():
    Data = (11, 12, 13, 14, 15)
    print("Actual Data is :", Data)

    #################################################################
    # Function Name : reduce()
    # Description   : Applies the given function (Minimum)
    #                 cumulatively to the elements of the iterable
    #                 and returns a single accumulated result
    # Input         : Function and iterable of integers
    # Output        : Integer (Minimum of all elements)
    # Author        : Vivek Bhauraj Gautam
    # Date          : 21 January 2026
    #################################################################
    RData = reduce(Minimum, Data)
    print("Minimum of all elements of list is :", RData)


if __name__ == "__main__":
    main()




# Minimum = lambda X , Y: X if X < Y else Y

# def main():
#     Data = 11,12,13,14,15
#     print("Actual Data is :",Data)

#     FData = list(reduce(Minimum, Data))
#     print("Minimum of hole lemenets of list is :", FData)

# if __name__ == "__main__":
#     main()