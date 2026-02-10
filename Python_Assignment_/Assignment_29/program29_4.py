# Write A program which Accept the filename using command line
# And compair the containts of both file two file

#=======================================================================
#
# Required Module 
# 
#=======================================================================
import os 
import sys        

#=======================================================================
#
# Function Name : Main
# Descripton    : It is a emtry point of our program 
#                 Acccept two file name from command line argumnets
#                 And It will open both the file and read the file
#                 And compair both the files
# Author        : Vivek Bhauraj Gautam
# Date          : 10-02-2026 
# 
#=======================================================================
def main():

    FileName1 = sys.argv[1]
    FileName2 = sys.argv[2]

    Ret = False 

    # if(sys.argv != 2):
    #     print("please gives proper command")
    #     return

    Ret = os.path.exists(FileName1 and FileName2)        # Function which are user to check file is exists or not  

    if(Ret == True):
        fSourceobj = open(FileName1,'r')
        SourceData = fSourceobj.read()
        fSourceobj.close()

        fDestobj = open(FileName2,'r')
        DestData = fDestobj.read()
        fDestobj.close()

        if(SourceData == DestData):
            print("Both files containst are same :")
        else:
            print("Both files are different")
    else:
        print(FileName1 ,"Or",FileName2," : is not exists in current Directry ")

if __name__ == "__main__":
    main()