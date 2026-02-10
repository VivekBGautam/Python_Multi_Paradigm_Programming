# Write A program which ecept the filename from user 
# And count the frequency of word in that file

#=======================================================================
#
# Required Module 
# 
#=======================================================================
import os    


# Program to display file content line by line in Python
#=======================================================================
#
# Function Name : Display_file_line_by_line
# Descripton    : It is used to display containts of file line by line
# Author        : Vivek Bhauraj Gautam
# Date          : 10-02-2026 
# 
#=======================================================================

def Display_file_line_by_line(file_path):
    try:
        # Open file in read mode with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            # Read and print each line without extra newlines
            for line_number, line in enumerate(file, start=1):
                print(f"{line_number} : {line.strip()}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to read '{file_path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

#=======================================================================
#
# Function Name : Main
# Descripton    : It is a emtry point of our program and check file is exist
# Author        : Vivek Bhauraj Gautam
# Date          : 10-02-2026 
# 
#=======================================================================
def main():
    path = input("Enter the file path: ").strip()
    Display_file_line_by_line(path)
    
if __name__ == "__main__":
    main()