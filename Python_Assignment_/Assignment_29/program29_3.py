# Write A program which Accept the filename using command line
# Create a new file name as Demo.txt and copy all the conntaints in that file 

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
#                 It will oepn the file and read the file
#                 And copy file contain in another file 
# Author        : Vivek Bhauraj Gautam
# Date          : 10-02-2026 
# 
#=======================================================================
def main():

    FileName = sys.argv[1]
    DestFile = "Demo.txt"

    Ret = False 

    Ret = os.path.exists(FileName)        # Function which are user to check file is exists or not  

    if(Ret == True):
        fSourceobj = open(FileName,'r')
        Data = fSourceobj.read()
        fSourceobj.close()

        fDestobj = open(DestFile,'w')
        fDestobj.write(Data)
        fDestobj.close()

    
        print("File gets Sucessfully copied ")
     


    else:
        print(FileName," : is not exists in current Directry ")

if __name__ == "__main__":
    main()