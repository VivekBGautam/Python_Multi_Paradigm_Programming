# Write A program which ecept the filename from user 
# And check weather the file is exists in current dirctory or not 

#=======================================================================
#
# Required Module 
# 
#=======================================================================
import os         

#=======================================================================
#
# Function Name : Main
# Descripton    : It is a emtry point of our program and check file is exist
# Author        : Vivek Bhauraj Gautam
# Date          : 10-02-2026 
# 
#=======================================================================
def main():
    print("Enter the file name :")
    FileName = input()

    Ret = False 

    Ret = os.path.exists(FileName)        # Function which are user to check file is exists or not  

    if(Ret == True):
        print(FileName," : is exists in current directry ")
    else:
        print(FileName," : is not exists in current Directry ")

if __name__ == "__main__":
    main()