# Write a program which contais one function named as Display().
# Which display 5 times Marvellous on display

def  Display(No):
    for i in range(No+1):
        print("Marvellous")
    
def main():
    Value1 = 0

    Value = int(input("Enter the first number : "))

    Display(Value)

if __name__ == "__main__":
    main()