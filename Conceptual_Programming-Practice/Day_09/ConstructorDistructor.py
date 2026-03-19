import gc

class Demo:
    def __init__(self):
        print("Inside Constructor :")
    def __del__(self):
        print("Inside Destrctor :")

# Alocate 
obj = Demo()

# Use

# Deallocate
del obj             # is like delete in C++

gc.collect()

print("End of applictaion")