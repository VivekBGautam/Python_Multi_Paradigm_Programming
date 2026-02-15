No = 11   # Globle

def fun():
    global No
    print("Value of No from fun is :",No)       # 11 
    No = No + 1
    print("Value of No from fun is :",No)       # 12      

print("Value of no is :", No)                   # 11
fun()
print("Value of no is :", No)                   # 12