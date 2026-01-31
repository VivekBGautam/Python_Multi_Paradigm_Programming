# 5. Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().


from MarvellousNum import CheckPrime

def ListPrime(Value):
    Data = 0
    Ret = 0
    List = []
    PrimeSum = 0
    print("Enter the element of list ",Value ," Times")
    for _ in range(Value):
        Data = int(input())
        List.append(Data)

    for i in range(Value):
        Ret = CheckPrime(List[i])
        if Ret == True:
            PrimeSum += (List[i])

    return PrimeSum
    
def main():
    No = int(input("Enter how many element you want in list : "))

    Ret = ListPrime(No)
    print("Additon of all prime number from list is :-> ",Ret)

if __name__ == "__main__":
    main()