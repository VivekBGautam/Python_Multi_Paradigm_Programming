# Write a program which contais one function named as Pattern().
# Which accept one number from user and display that nnumber of * on console

def  Pattern(No):
    for i in range(No+1):
        print("*")
    
    
def main():
    Value1 = 0

    Value = int(input("Enter the first number : "))

    Pattern(Value)

if __name__ == "__main__":
    main()