class Parrent:
    def __init__(self):
        print("Inside parent constructor")
        self.No1 = 10
        self.No2 = 20
    
    def Fun(self):
        print("Inside fun method of parrent")

class Child(Parrent):
    def __init__(self):
        super().__init__()
        print("Inside child constructor")
        self.A = 11
        self.B = 21

    def Sun(self):
        print("Inside Sun method of child")

cobj = Child()

cobj.Fun()
cobj.Sun()

print(cobj.No1)