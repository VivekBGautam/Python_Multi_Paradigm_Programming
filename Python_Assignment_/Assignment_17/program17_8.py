"""
# program17_7

# Write one program which accept one number from user and Display below pattern
# input : 5
# Output    :   1  
                1   2    
                1   2   3    
                1   2   3   4 
                1   2   3   4   5   

"""
def Pattern(No):
    for i in range(No+1):
        for j in range(1,No + 1):
            if i > j or i == j: 
                print(j,end = "   ")
        print()

def main():
    Value = int(input("Enter the number : "))

    Pattern(Value)

if __name__ == "__main__":
    main()