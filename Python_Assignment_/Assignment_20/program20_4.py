# 4. : Design a Python application that creates three threads named Small, Capital, and
# Digits.

# All threads should accept a string as input.
# The Small thread should count and display the number of lowercase characters.
# The Capital thread should count and display the number of uppercase characters.
# The Digits thread should count and display the number of numeric digits.
# Each thread must also display:

# Thread ID
# Thread Name

import threading

def Count_Small(Text):
    Count = 0
    for i in range(len(Text)):
        if Text[i] >='a' and Text[i] <='z':
            Count = Count + 1

    print("Count of small charector in text is : ",Count)
    print("process id of Count_Small is : ",threading.get_ident())
    print("Thread Name of Count_Small is : ",threading.current_thread().name)

def Count_Capital(Text):
    Count = 0
    for i in range(len(Text)):
        if Text[i] >='A' and Text[i] <='Z':
            Count = Count + 1

    print("Count of Capital charector in text is : ",Count)
    print("process id of Count_Capital is : ",threading.get_ident())
    print("Thread Name of Count_Capital is : ",threading.current_thread().name)

def Count_Digit(Text):
    Count = 0
    for i in range(len(Text)):
        if Text[i] >='0' and Text[i] <='9':
            Count = Count + 1

    print("Count of Digits in text is : ",Count)
    print("process id of Count_Digit is : ",threading.get_ident())
    print("Thread Name of Count_Digit is : ",threading.current_thread().name)

def main():
    Text = "MarvellousInfoSystem12345"

    t1 = threading.Thread(target = Count_Small, args = (Text,))
    t2 = threading.Thread(target = Count_Capital, args = (Text,))
    t3 = threading.Thread(target = Count_Digit, args = (Text,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()