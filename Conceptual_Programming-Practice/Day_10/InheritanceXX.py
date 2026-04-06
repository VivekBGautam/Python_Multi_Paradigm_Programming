class Parrent:
    def __init__(self): 
        print("Inside parent constructor")
    
    def Fun(self):
        print("Inside fun method of parrent")

class Child(Parrent):
    def __init__(self):
        super().__init__()
        print("Inside child constructor")

    def Fun(self):
        super().Fun()
        print("Inside Fun method of child",)

cobj = Child()

cobj.Fun()
