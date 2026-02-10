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
# Descripton    : It is a entry point of our check word is present or not
# Author        : Vivek Bhauraj Gautam
# Date          : 10-02-2026 
# 
#=======================================================================
def main():
    Count1 = 0
    Ret = False

    print("Enter the file name :")
    FileName = input()

    print("Enter the word that you want to find :")
    WordToFind = input()

    Ret = os.path.exists(FileName)        # Function which are user to check file is exists or not
    if Ret != True:
        print("There is no suc file :")
        return  

    try:
        Sourceobj = open(FileName,'r')
        File_Data = Sourceobj.read()
        Sourceobj.close()

        if WordToFind in File_Data:
            print(f"{WordToFind} is Present in file")
        else:
            print(f"{WordToFind} is Not Present in file")

    except Exception as e:
        print("Unexpected error occures as : ",e)

if __name__ == "__main__":
    main()