# Write one program which contain one function Named as CheckVowel()
# which Accept one Charector and check weather it is Vowel Or Consonent


#################################################################
# Function Name : CheckVowel
# Description   : Accepts a number and check weather it is palindrome or not
# Input         : Charector
# Output        : Returns True if it is Vowel else return False 
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def CheckVowel(Char):

    if Char > 'A' or Char < 'Z':
        Char = Char.lower()
    
    if Char == 'a' or Char == 'e' or Char == 'i' or Char == 'o' or Char == 'u':
        return True
    else:
        return False


#################################################################
# Function Name : main
# Description   : This is the entry point of the program and calls Display()
# Input         : None
# Output        : Executes CheckVowel function
# Author        : Vivek Bhauraj Gautam
# Date          : 19 January 2026
#################################################################
def main():
    Valucharchare = None
    print("Enter the number :")
    Char = input()

    Ret = CheckVowel(Char)

    if Ret == True:
        print(Char ," is A Vowel")
    else:
        print(Char ," is not A Vowel")

if __name__ == "__main__":
    main()