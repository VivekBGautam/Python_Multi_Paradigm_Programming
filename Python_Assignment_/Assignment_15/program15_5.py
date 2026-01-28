# Write a lambda function using Filter() which accept a list of number
# And return Maximum of numbers 
from functools import reduce

#################################################################
# Function Name : Maximum
# Description   : Accepts two numbers and returns their Maximum
#                 using lambda function
# Input         : Two Integers
# Output        : Integer (Maximum of two numbers)
# Author        : Vivek Bhauraj Gautam
# Date          : 21 January 2026
#################################################################
Maximum = lambda X, Y: X if X > Y else Y


#################################################################
# Function Name : main
# Description   : Entry point of the program. Creates a list
#                 of numbers and applies reduce() with lambda
#                 function to calculate Maximum of all elements
# Input         : None
# Output        : Displays original list and Maximum result
# Author        : Vivek Bhauraj Gautam
# Date          : 21 January 2026
#################################################################
def main():
    Data = (11, 12, 13, 14, 15)
    print("Actual Data is :", Data)

    #################################################################
    # Function Name : reduce()
    # Description   : Applies the given function (Maximum)
    #                 cumulatively to the elements of the iterable
    #                 and returns a single accumulated result
    # Input         : Function and iterable of integers
    # Output        : Integer (Maximum of all elements)
    # Author        : Vivek Bhauraj Gautam
    # Date          : 21 January 2026
    #################################################################
    RData = reduce(Maximum, Data)
    print("Maximum of all elements of list is :", RData)


if __name__ == "__main__":
    main()




# Maximum = lambda X , Y: X if X > Y else Y

# def main():
#     Data = 11,12,13,14,15
#     print("Actual Data is :",Data)

#     FData = list(reduce(Maximum, Data))
#     print("Maximum of hole lemenets of list is :", FData)

# if __name__ == "__main__":
#     main()