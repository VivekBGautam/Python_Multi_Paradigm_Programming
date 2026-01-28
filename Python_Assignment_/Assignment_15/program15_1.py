# Write a lambda function using map() which accept a list of number
# And return list of square of each number 

#################################################################
# Function Name : Square
# Description   : Accepts one number and returns the square of
#                 that number using lambda function
# Input         : Integer
# Output        : Integer (Square of given number)
# Author        : Vivek Bhauraj Gautam
# Date          : 21 January 2026
#################################################################
Square = lambda X: X * X

#################################################################
# Function Name : main
# Description   : Entry point of the program. Creates a list
#                 of numbers, applies map() with lambda function
#                 to calculate square of each number and
#                 displays the result
# Input         : None
# Output        : Displays original and squared list
# Author        : Vivek Bhauraj Gautam
# Date          : 21 January 2026
#################################################################
def main():
    Data = (11, 12, 13, 14, 15)
    print("Actual Data is :", Data)

    #################################################################
    # Function Name : map()
    # Description   : Applies the given function (Square) to each
    #                 element of the input iterable and returns
    #                 a new iterable containing squared values
    # Input         : Function and iterable of integers
    # Output        : Iterable of squared integers
    # Author        : Vivek Bhauraj Gautam
    # Date          : 21 January 2026
    #################################################################
    MData = list(map(Square, Data))
    print("Data after map is :", MData)

if __name__ == "__main__":
    main()



# Square = lambda X: X * X

# def main():
#     Data = 11,12,13,14,15
#     print("Actual Data is :",Data)

#     MData = list(map(Square, Data))
#     print("Data after map is :",MData)

# if __name__ == "__main__":
#     main()