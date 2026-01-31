# 4.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which are even. Map function will calculate its square.
# Reduce will return addition of all that numbers.

# Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
# List after filter = [2, 4, 4, 2, 8, 10]
# List after map = [4, 16, 16, 4, 64, 100]
# Output of reduce = 204

#--------------------------------------------------------------------------------------------
from functools import reduce
CheckNumber = lambda A : (A % 2 == 0)
IncreaseValue = lambda A : A * A 
Product = lambda A, B : A + B

def main():
    List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]

    FData = list(filter(CheckNumber,List))
    print("Data after filter is : ",FData)

    MData = list(map(IncreaseValue,FData))
    print("Data after filter is : ",MData)

    RData = reduce(Product,MData)
    print("Data after filter is : ",RData)


if __name__ == "__main__":
    main()