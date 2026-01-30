"""
# program17_6

# Write one program which accept one number from user and Display below pattern
# input : 5
# Output    :   *   *   *   *   *
                *   *   *   *   
                *   *   *   
                *   *  
                *   

"""
def Pattern(No):
    for i in range(No):
        for j in range(No + 1):
            if i < j:
                print("*",end = "   ")
        print()

def main():
    Value = int(input("Enter the number : "))

    Pattern(Value)

if __name__ == "__main__":
    main()