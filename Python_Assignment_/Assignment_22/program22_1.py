# 1: Write a Python program to implement a class named Demo with the following
# specifications:

#     . The class should contain two instance variables: no1 and no2.

#     . The class should contain one class variable named Value.

#     . Define a constructor (

#     · Implement two instance methods:

#         o Fun () - displays the values of instance variables no1 and no2.

#         o Gun () - displays the values of instance variables no1 and no2.

# Create two objects of the Demo class as follows:

# Obj1 = Demo(11, 21)

# Obj2 = Demo(51, 101)

# Call the instance methods in the given sequence:

# Obj1.Fun()

# Obj2.Fun()
# Obj1.Gun()
# Obj2.Gun()

# init ) that accepts two parameters and initializes the instance variables.

class Demo:
    Value = 0
    def __init__(self,A,B):
        self.no1 = A
        self.no2 = B
    def Fun(self):
        print(self.no1,self.no2)
    def Gun(self):
        print(self.no1,self.no2)

obj1 = Demo(11,21)
obj2 = Demo(51,101)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()

