# 2. Write a program which contains one lambda function which accepts two parameters and return
# its multiplication.

#Input : 4  3          12
#Input : 6  3          24

#--------------------------------------------------------------------------------------------

Power = lambda A ,B : A * B 

def main():
    Value1 = 0
    Value1 = int(input("Enter the first number : "))
    Value2 = 0
    Value2 = int(input("Enter the second number : "))

    Ret = Power(Value1,Value2)
    print("Multiplication is :->",Ret)

if __name__ == "__main__":
    main()