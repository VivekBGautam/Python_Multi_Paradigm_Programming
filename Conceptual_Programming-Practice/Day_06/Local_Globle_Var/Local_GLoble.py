No = 11   # Globle

def fun():
    No = 21      # Local

    print("Value of No from fun is :",No)       # 21 

print("Value of no is :", No)                   # 11

fun()