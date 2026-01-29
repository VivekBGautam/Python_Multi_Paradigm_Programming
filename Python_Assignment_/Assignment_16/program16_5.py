# Write a program which contais one function named as Display().
# Which display 10 to 1 on display

def  Display(No):
    for i in range(No+1, 1 -1):
        print(i)
    
def main():
    Value1 = 0

    Value = int(input("Enter the first number : "))

    Display(Value)

if __name__ == "__main__":
    main()