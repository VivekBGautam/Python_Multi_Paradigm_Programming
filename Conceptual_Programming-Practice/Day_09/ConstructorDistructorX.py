import gc

class Demo:
    def __init__(self):
        print("Inside Constructor :")
    def __del__(self):
        print("Inside Destrctor :")

# Alocate 
obj1 = Demo()
obj2 = Demo()

# Use

# Deallocate
del obj1             # is like delete in C++
del obj2

gc.collect()

print("End of applictaion")