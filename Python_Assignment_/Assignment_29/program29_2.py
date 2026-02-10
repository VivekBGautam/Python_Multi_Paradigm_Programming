# Write A program which ecept the filename from user 
# And open the file and read it andd print all containts of file on console

#=======================================================================
#
# Required Module 
# 
#=======================================================================
import os         

#=======================================================================
#
# Function Name : Main
# Descripton    : It is a emtry point of our program 
#                 It will oepn the file and read the file
#                 And print all containts of file on console
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
        fobj = open(FileName,'r')

        Data = fobj.read(1024)
        print(Data)

    else:
        print(FileName," : is not exists in current Directry ")

if __name__ == "__main__":
    main()