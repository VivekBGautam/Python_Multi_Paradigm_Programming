# Assignment_20 - Python Multithreading Assignment

## Assignment Title
Python Multithreading Using `threading` Module

---

## Assignment Description
This assignment demonstrates the use of **multithreading in Python**.   
Multiple threads are created to perform different tasks such as number processing, list operations, string analysis, and thread synchronization.

Each program focuses on:
- Creating threads
- Running threads concurrently
- Passing arguments to threads
- Synchronizing threads using `join()`

---

## File Structure
```
Assignment_20/
│
├── program20_1.py → Even & Odd Threads
├── program20_2.py → EvenFactor & OddFactor Threads
├── program20_3.py → EvenList & OddList Threads
├── program20_4.py → Small, Capital & Digits Threads
├── program20_5.py → Thread Synchronization
└── README.md
```

---

## 🧵 Programs Included

---

### **Program 20_1 : Even and Odd Threads**
- Creates two threads named **Even** and **Odd**
- Even thread displays first 10 even numbers
- Odd thread displays first 10 odd numbers
- Both threads execute independently using the `threading` module

---

### **Program 20_2 : EvenFactor and OddFactor Threads**
- Accepts one integer number as input
- **EvenFactor thread**
  - Identifies all even factors of the number
  - Calculates and displays the sum of even factors
- **OddFactor thread**
  - Identifies all odd factors of the number
  - Calculates and displays the sum of odd factors
- After completion of both threads, main thread displays  
  **"Exit from main"**

---

### **Program 20_3 : EvenList and OddList Threads**
- Accepts a list of integers
- **EvenList thread**
  - Extracts all even elements
  - Calculates and displays their sum
- **OddList thread**
  - Extracts all odd elements
  - Calculates and displays their sum
- Both threads run concurrently

---

### **Program 20_4 : Small, Capital and Digits Threads**
- Accepts a string as input
- **Small thread**
  - Counts lowercase characters
- **Capital thread**
  - Counts uppercase characters
- **Digits thread**
  - Counts numeric digits
- Each thread displays:
  - Thread ID
  - Thread Name

---

### **Program 20_5 : Thread Synchronization**
- Creates two threads named **Thread1** and **Thread2**
- **Thread1**
  - Displays numbers from 1 to 50
- **Thread2**
  - Displays numbers from 50 to 1 in reverse order
- Thread2 starts execution **only after Thread1 completes**
- Demonstrates thread synchronization using `join()`

---

## Technologies Used
- Python 3.x
- `threading` module

---

## Conclusion
This assignment helps in understanding:
- Multithreading concepts in Python
- Concurrent execution of threads
- Passing data to threads
- Thread synchronization techniques

These programs provide a strong foundation for real-world multithreaded applications.

---

## Author Information
- **Name:** Vivek Bhauraj Gautam  
- **Email:** vivekbgautam@gmail.com  
- **GitHub:** https://github.com/vivekbgautam  

---

