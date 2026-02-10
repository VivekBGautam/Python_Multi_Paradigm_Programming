# Write A program which ecept the filename from user 
# And count the frequency of lines in that file

#=======================================================================
#
# Required Module 
# 
#=======================================================================
import os         

#=======================================================================
#
# Function Name : Main
# Descripton    : It is a entry point of our program and check file is exist
# Author        : Vivek Bhauraj Gautam
# Date          : 10-02-2026 
# 
#=======================================================================
def main():
    Count1 = 0
    Ret = False

    print("Enter the file name :")
    FileName = input()

    Ret = os.path.exists(FileName)        # Function which are user to check file is exists or not  

    if(Ret == True):
        Sourceobj = open(FileName,'r')
        Data = Sourceobj.read()

        Count1 = Data.count('\n')
    else:
        print(FileName," : is not exists in current Directry ")

    print("Count of lines is ->", Count1)

if __name__ == "__main__":
    main()