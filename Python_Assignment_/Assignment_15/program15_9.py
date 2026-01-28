# Write a lambda function using Filter() which accept a list of number
# And return Product of numbers 
from functools import reduce

#################################################################
# Function Name : Product = lambda X, Y: X + Y
# Description   : Accepts two numbers and returns their Addition
#                 using lambda function
# Input         : Two Integers
# Output        : Integer (Product of two numbers)
# Author        : Vivek Bhauraj Gautam
# Date          : 21 January 2026
#################################################################
Product = lambda X, Y: X * Y


#################################################################
# Function Name : main
# Description   : Entry point of the program. Creates a list
#                 of numbers and applies reduce() with lambda
#                 function to calculate Product of all elements
# Input         : None
# Output        : Displays original list and Product result
# Author        : Vivek Bhauraj Gautam
# Date          : 21 January 2026
#################################################################
def main():
    Data = (11, 12, 13, 14, 15)
    print("Actual Data is :", Data)

    #################################################################
    # Function Name : reduce()
    # Description   : Applies the given function (Product)
    #                 cumulatively to the elements of the iterable
    #                 and returns a single accumulated result
    # Input         : Function and iterable of integers
    # Output        : Integer (Product of all elements)
    # Author        : Vivek Bhauraj Gautam
    # Date          : 21 January 2026
    #################################################################
    RData = reduce(Product, Data)
    print("Product of all elements of list is :", RData)


if __name__ == "__main__":
    main()




# Product = lambda X , Y: X * Y

# def main():
#     Data = 11,12,13,14,15
#     print("Actual Data is :",Data)

#     FData = list(reduce(Product, Data))
#     print("Product of hole lemenets of list is :", FData)

# if __name__ == "__main__":
#     main()