# PID concept
import os

def main():
    print("PID of running process is : ", os.getpid())
    print("PID of parrnt process is : ",os.getppid())

if __name__ == "__main__":
    main()