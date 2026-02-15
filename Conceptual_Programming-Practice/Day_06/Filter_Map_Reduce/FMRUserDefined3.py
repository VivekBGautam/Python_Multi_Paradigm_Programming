
CheckEven = lambda No : (No % 2 == 0)

Increment = lambda No : No +1

Add = lambda A , B : A + B         # A = prevSum    B = Value

def filterX(Task, Elements):       # Task = CheckEven   //  Elements = Data(list)
    Result = list()

    for No in Elements:
        Ret = Task(No)

        if(Ret == True):
            Result.append(No)

    return Result

def mapX(Task, Elements):
    Result = list()

    for No in Elements:
        Ret = Task(No)
        Result.append(Ret)
    
    return Result

# Add = lambda A , B : A + B 
def reduceX(Task, Elements):
    Sum = 0

#   [11, 21, 23, 31]
    for No in Elements:
        Sum = Task(Sum,No)
    
    return Sum

def main():

    Data = [11,10,15,20,22,27,30]
    print("Actual Data is :",Data)

    FData = list(filterX(CheckEven , Data))
    print("Data after filter is : ",FData)

    MData = list(mapX(Increment,FData))
    print("Data after Map is :",MData)

    RData = reduceX(Add,MData)
    print("Data after redduce is :",RData)

if __name__ == "__main__":
    main()