
# Time concept
import time

def Factorial(No):
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i

    return Fact 

def main():
    Ret = None

    Value = int(input("Enter Number : "))

    start_time = time.time()

    Ret = Factorial(Value)

    end_time = time.time()

    print("Factorial of",Value ," is :",Ret,"\n")

    print("Total execution time is :",end_time - start_time)

    print((Ret))

    

if __name__ == "__main__":
    main()