# Write a lambda function using Filter() which accept a list of number
# And return list of Count Even number 

#################################################################
# Function Name : CountEven
# Description   : Accepts List of number and returns the Count Even of
#                 that list number using lambda function
# Input         : Integer
# Output        : Integer (Even number)
# Author        : Vivek Bhauraj Gautam
# Date          : 21 January 2026
#################################################################
CountEven = lambda X :(X % 2 == 0) 

#################################################################
# Function Name : main
# Description   : Entry point of the program. Creates a list
#                 of numbers, applies filter() with lambda function
#                 to Count Even element and displays the result
# Input         : None
# Output        : Displays original and Evened list
# Author        : Vivek Bhauraj Gautam
# Date          : 21 January 2026
#################################################################
def main():
    Data = (11, 12, 13, 14, 15)
    print("Actual Data is :", Data)

    #################################################################
    # Function Name : filter()
    # Description   : Applies the given function (CountEven) to each
    #                 element of the input iterable and returns
    #                 a new iterable containing Count of even element
    # Input         : Function and iterable of integers
    # Output        : Count Even element
    # Author        : Vivek Bhauraj Gautam
    # Date          : 21 January 2026
    #################################################################
    FData = list(filter(CountEven, Data))
    print("Element after filter is :",FData)
    print("Count of even elements after filter is :", len(FData))

if __name__ == "__main__":
    main()


# CountEven = lambda X: ( X % 2 == 0 )

# def main():
#     Data = 11,12,13,14,15
#     print("Actual Data is :",Data)

#     FData = list(filter(CountEven, Data))
#     print("Count of even after filter is :", FData)

# if __name__ == "__main__":
#     main()