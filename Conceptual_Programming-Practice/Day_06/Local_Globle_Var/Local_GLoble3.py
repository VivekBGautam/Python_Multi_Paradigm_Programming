No = 11   # Globle

def fun():
    No = 21
    print("Value of No from fun is :",No)       # 21 
    No = No + 1
    print("Value of No from fun is :",No)       # 22      

print("Value of no is :", No)                   # 11
fun()
print("Value of no is :", No)                   # 11