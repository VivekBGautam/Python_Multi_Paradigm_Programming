# 2: Write a Python program to implement a class named Circle with the following
# requirements:

#     . The class should contain three instance variables: Radius, Area, and Circumference.

#     . The class should contain one class variable named PI, initialized to 3.14.

#     Define a constructor(__init__)that inicialize all instance variable to 0.0
#     Implement the following instance methods:

#         o Accept () - accepts the radius of the circle from the user.

#     CalculateArea ( ) - calculates the area of the circle and stores it in the Area variable.

#     . CalculateCircumference() - calculates the circumference of the circle and stores it in
#     the Circumference variable.

#     . Display ( ) - displays the values of Radius, Area, and Circumference.

#     . Create multiple objects of the Circle class and invoke all the instance methods for each object.

class Circle:
    PI = 3.14

    # Constructor
    def __inti__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumferance = 0.0
    
    # Instance method to calculate area
    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius
        

    # Instance method to calculate circumfarance
    def CalculateCircumference(self):
        self.Circumferance = 2 * Circle.PI * self.Radius

    # Instance method to accept radius from circle 
    def Accept(self):
        self.Radius = float(input("Enter the radius of circle : "))

    # Insttance method to display the values
    def Display(self):
        print("Radius of circle is : ",self.Radius)
        print("Area of circle is : ",self.Area)
        print("Circumfarance of circle is : ",self.Circumferance)

# creating multiple objects
Obj1 = Circle()
Obj2 = Circle()

# invoking methods for first object
Obj1.Accept()
Obj1.CalculateArea()
Obj1.CalculateCircumference() 
Obj1.Display()

# invoking methods for second object
Obj2.Accept()
Obj2.CalculateArea()
Obj2.CalculateCircumference()
Obj2.Display()






    

    

