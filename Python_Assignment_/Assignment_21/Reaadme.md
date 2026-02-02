# Assignment_21 – Python Multithreading

## Assignment Title
Python Multithreading Using `threading` Module

---

## Assignment Description

This assignment focuses on **multithreading in Python** using the built-in `threading` module.  
Multiple threads are created to perform different operations on lists and shared data.

The programs demonstrate:
- Creating and naming threads
- Running threads concurrently
- Sharing data between threads
- Using `Lock` to avoid race conditions
- Returning results from threads to the main thread

---

## File Structure
```
Assignment_21/
│
├── program21_1.py # Prime and Non-Prime numbers using threads
├── program21_2.py # Maximum and Minimum element using threads
├── program21_3.py # Thread-safe shared counter using Lock
├── program21_4.py # Sum and Product of list using threads
└── README.md

```
---

## Programs Included

### Program 21_1 – Prime and Non-Prime Numbers
- Creates two threads named **Prime** and **NonPrime**
- Both threads accept the same list of integers
- Prime thread displays all prime numbers
- NonPrime thread displays all non-prime numbers

---

### Program 21_2 – Maximum and Minimum Element
- Creates two threads
- One thread finds the **maximum** element
- Another thread finds the **minimum** element
- List is accepted from the user

---

### Program 21_3 – Thread-Safe Counter
- Multiple threads update a shared counter
- Uses `Lock` to prevent race conditions
- Each thread increments the counter multiple times
- Displays the final counter value after execution

---

### Program 21_4 – Sum and Product of List
- Creates two threads
- One thread calculates the **sum** of list elements
- Another thread calculates the **product** of list elements
- Results are returned to the main thread and displayed


---

## Author Information

**Name:** Vivek Gautam  
**Email:** vivekbgautam@gmail.com  
**GitHub:** https://github.com/vivekbgautam
