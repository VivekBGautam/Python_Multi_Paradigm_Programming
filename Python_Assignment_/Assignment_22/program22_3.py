# 3: Write a Python program to implement a class named Arithmetic with the following
# characteristics:

#     The class should contain two instance variables: Value1 and Value2.

#     Define a constructor(__init__)that initializes all instance variables to 0.
#     Implement the following instance methods:

#         1. Accept ( ) - accepts values for Value1 and Value2 from the user.
#         2, Addition ( ) - returns the addition of Value1 and Value2.
#         3. Subtraction () - returns the subtraction of Value1 and Value2.
#         4. Multiplication ( ) -returns the multiplication of Value1 and Value2.
#         5. Division () - returns the division of Value1 and Value2 (handle division by zero
#         properly).

#     Create multiple objects of the Arithmetic class and invoke all the instance methods.init
     
class Arithmetic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter the first value : "))
        self.Value2 = int(input("Enter the second value : "))

    # instance method for addition
    def Addition(self):
        return self.Value1 + self.Value2

    # instance method for subtraction
    def Subtraction(self):
        return self.Value1 - self.Value2

    # instance method for multiplication
    def Multiplication(self):
        return self.Value1 * self.Value2

    # instance method for division
    def Division(self):
        if self.Value2 == 0:
            return "Division by zero not allowed"
        return self.Value1 / self.Value2


# creating multiple objects
Obj1 = Arithmetic()
Obj2 = Arithmetic()

# first object operations
Obj1.Accept()
print("Addition:", Obj1.Addition())
print("Subtraction:", Obj1.Subtraction())
print("Multiplication:", Obj1.Multiplication())
print("Division:", Obj1.Division())
print("--------------------------")

# second object operations
Obj2.Accept()
print("Addition:", Obj2.Addition())
print("Subtraction:", Obj2.Subtraction())
print("Multiplication:", Obj2.Multiplication())
print("Division:", Obj2.Division())