# 1.Write a program which contains one lambda function which accepts one parameter and return
#power of two.

#Input : 4          16
#Input : 6          64

#--------------------------------------------------------------------------------------------

Power = lambda A : A * A 

def main():
    Value = 0
    Value = int(input("Enter the number : "))
    Ret = Power(Value)
    print("Power of ",Value,"is :->",Ret)

if __name__ == "__main__":
    main()