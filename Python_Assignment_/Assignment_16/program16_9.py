# Write a program which contais one function named as PrinEven().
# Which print first 10 even number on display

def  PrinEven():
    for i in range(1,11):
        print(2 * i,end= "   ")    # end = "   " is for tab or space between number 
    
    
def main():
    PrinEven()

if __name__ == "__main__":
    main()