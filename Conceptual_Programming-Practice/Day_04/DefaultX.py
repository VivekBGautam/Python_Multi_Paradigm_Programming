
def EmployeeInfo(Name,Age,Salery,City = "Mumbai"):
    print("Name : ",Name)
    print("Age : ",Age)
    print("Salery : ", Salery)
    print("City : ",City)

def main():
    EmployeeInfo("Rahul",26,2000.50)
    print()
    EmployeeInfo("Rahul",26,2000.50,"Pune")

if __name__ == "__main__":
    main()