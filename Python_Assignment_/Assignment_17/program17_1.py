# create one module named as Arithmetic which contains 4 function as 
# Add for Adddition ,sub for Substrcation, mult() for multiplication, Div() for division 
# All function accept two parameter as number and return the operation. 
# write on python programe which call all function from Arithmatic module by accepting the parameters from user

import Arithematic

def main():
    Value1 = 0
    Value2 = 0

    Value1 = int(input("Enter the first Number : "))
    Value2 = int(input("Enter the Second Number : "))

    Ret = Arithematic.Add(Value1,Value2)
    print("Addition is :",Ret)

    Ret = Arithematic.Sub(Value1,Value2)
    print("Substraction is :",Ret)

    Ret = Arithematic.Mult(Value1,Value2)
    print("Multiplication is :",Ret)

    Ret = Arithematic.Div(Value1,Value2)
    print("Division is :",Ret)


main()