# Write A program which ecept two filename from user 
# And copy the containints of one file into another file

#=======================================================================
#
# Required Module 
# 
#=======================================================================
import os         

#=======================================================================
#
# Function Name : Main
# Descripton    : It is a entry point of our program
# Author        : Vivek Bhauraj Gautam
# Date          : 10-02-2026 
# 
#=======================================================================
def main():
    Count1 = 0
    Ret = False

    print("Enter the Source file name :")
    SourceFile = input()

    print("Enter the Dest file name :")
    DestFile = input()

    try:
        Sourceobj = open(SourceFile,'r')
        Data = Sourceobj.read()
        Sourceobj.close()

        Destobj = open(DestFile,'w')
        Destobj.write(Data)
        Sourceobj.close()

        print("file get sucessfully copied into the another file")

    except Exception as e:
        print("Unexpected Error occures :",e)

if __name__ == "__main__":
    main()