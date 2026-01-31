# Assignment_19 : List Programs in Python

## Aim

To understand and implement Python programs using **List**, user input, and basic list operations such as addition, maximum, minimum, frequency count, and prime number processing with user-defined modules.

---

## Assignment Description

This assignment contains programs that accept **N numbers from the user**, store them into a **List**, and perform different operations on that list.

---

## Programs Included

### Program 1: Addition of All Elements

**Description:**
Accept N numbers from the user, store them into a list, and return the addition (sum) of all elements from that list.

**File Name:** `python19_1.py`

---

### Program 2: Maximum Number from List

**Description:**
Accept N numbers from the user, store them into a list, and return the maximum number from that list.

**File Name:** `python19_2.py`

---

### Program 3: Minimum Number from List

**Description:**
Accept N numbers from the user, store them into a list, and return the minimum number from that list.

**File Name:** `python19_3.py`

---

### Program 4: Frequency of a Number

**Description:**
Accept N numbers from the user, store them into a list. Accept one additional number from the user and return the frequency of that number from the list.

**File Name:** `python19_4.py`

---

### Program 5: Addition of All Prime Numbers

**Description:**
Accept N numbers from the user and store them into a list. Return the addition of all prime numbers from that list.

* Main Python file accepts N numbers from the user.
* Each number is passed to the `ChkPrime()` function.
* `ChkPrime()` function is part of a user-defined module named **MarvellousNum**.
* Function called from main file should be named **ListPrime()**.

**File Names:**

* Main File: `python19_5.py`
* Module File: `MarvellousNum.py`

---

## File Structure

```
Assignment_19/
│── python19_1.py      -> Adds all elements from the list
│── python19_2.py      -> Finds maximum number from the list
│── python19_3.py      -> Finds minimum number from the list
│── python19_4.py      -> Counts frequency of a given number
│── python19_5.py      -> Calculates addition of prime numbers from the list
│── MarvellousNum.py   -> Contains ChkPrime() function
│── README.md          -> Assignment documentation
```

---

## Concepts Used

* List data structure
* User input handling
* Functions
* Modular programming
* Prime number logic

---

## How to Run

1. Open terminal or command prompt.
2. Navigate to the assignment directory.
3. Run the required program using:

   ```bash
   python programX.py
   ```

   (Replace `X` with program number)

---

## Author

**Name:** Vivek Bhauraj Gautam
**Email:** [vivekbgautam@gmail.com](mailto:vivekbgautam@gmail.com)
**GitHub:** [https://github.com/vivekbgautam](https://github.com/vivekbgautam)

---

## Conclusion

This assignment helps in strengthening the understanding of Python lists, user-defined functions, and modular programming using practical examples.


## Questions

1. Write a program which accept N numbers from user and store it into List. Return addition of all
elements from that List.

2. Write a program which accept N numbers from user and store it into List. Return Maximum
number from that List.

3. Write a program which accept N numbers from user and store it into List. Return Minimum number from that List.

4. Write a program which accept N numbers from user and store it into List. Accept one another
number from user and return frequency of that number from List.

5. Write a program which accept N numbers from user and store it into List. Return addition of all
prime numbers from that List. Main python file accepts N numbers from user and pass each
number to ChkPrime() function which is part of our user defined module named as
MarvellousNum. Name of the function from main python file should be ListPrime().
