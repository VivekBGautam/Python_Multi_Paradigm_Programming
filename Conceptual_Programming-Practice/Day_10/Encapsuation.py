class Arithmatic:
    def __init__(self,A,B):     # magic method / Dundal method
        self.No1 = A
        self.No2 = B
        print("Object gets created succesfully")

    def Addition(self):         # instance method
        Ans = 0
        Ans = self.No1 + self.No2
        return Ans
    
    def Substraction(self):         # instance method
        Ans = 0
        Ans = self.No1 - self.No2
        return Ans
    
obj1 = Arithmatic(11,10)
obj2 = Arithmatic(21,20)

Ret = obj1.Addition()
print(Ret)              # 21
Ret = obj1.Substraction()

Ret = obj2.Addition()
Ret = obj2.Substraction()
print(Ret)              # 1
