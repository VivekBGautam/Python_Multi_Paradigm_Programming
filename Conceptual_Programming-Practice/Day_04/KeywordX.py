
def EmployeeInfo(Name,Age,Salery,City):
    print("Name : ",Name)
    print("Age : ",Age)
    print("Salery : ", Salery)
    print("City : ",City)

def main():
    # Positional
    # EmployeeInfo("Rahul",26,2000.50,"Pune")  # Correct
    # EmployeeInfo(26,"Rahul","Pune",2000.50)  # Wrong

    # Keyword Argument
    EmployeeInfo(Age = 26, Name = "Rahul",City = "Pune",Salery = 2000.50)   # Keypord
    
    # if we dont no any value 
    EmployeeInfo(Age = 26, Name = "Rahul",City = "Pune",Salery = None)   # Keypord



if __name__ == "__main__":
    main()