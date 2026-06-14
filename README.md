# Python and C Programming – Task 03

## 📌 Task 03: Loops, Patterns & Basic Automation

### 🎯 Objective

The purpose of this task is to strengthen understanding of loops, iteration, problem-solving, and basic automation concepts. All programs were implemented in both **Python** and **C Programming**.

---

## 📂 Folder Structure

```text
Programming_Task_03_YourName/
│
├── Python Files
│   ├── multiplication_table.py
│   ├── number_analysis.py
│   ├── patterns.py
│   ├── password_attempt.py
│   └── username_generator.py
│
├── C Files
│   ├── multiplication_table.c
│   ├── number_analysis.c
│   ├── patterns.c
│   ├── password_attempt.c
│   └── username_generator.c
│
├── Screenshots
│   ├── multiplication_table_output.png
│   ├── number_analysis_output.png
│   ├── patterns_output.png
│   ├── password_attempt_output.png
│   └── username_generator_output.png
│
└── README.md
```

---

## 🔹 Part A: Multiplication Table Generator

### Description

This program accepts a number from the user and displays its multiplication table up to 10 using a loop.

### Example

**Input**

```text
7
```

**Output**

```text
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
```

### Logic Used

* Accept a number from the user.
* Use a `for` loop from 1 to 10.
* Multiply the number by the loop variable.
* Display the result.

---

## 🔹 Part B: Number Analysis Tool

### Description

This program accepts a number N and calculates:

* Sum of numbers from 1 to N
* Count of even numbers
* Count of odd numbers

### Example

**Input**

```text
10
```

**Output**

```text
Sum = 55
Even Numbers = 5
Odd Numbers = 5
```

### Logic Used

* Use a loop from 1 to N.
* Add each number to a running sum.
* Check whether the number is even or odd.
* Increment the corresponding counter.

---

## 🔹 Part C: Pattern Printing Challenge

### Pattern 1

```text
*
**
***
****
*****
```

### Pattern 2

```text
*****
****
***
**
*
```

### Pattern 3

```text
1
12
123
1234
12345
```

### Logic Used

* Use nested loops.
* Outer loop controls rows.
* Inner loop controls symbols or numbers printed in each row.

---

## 🔹 Part D: Password Attempt Simulator

### Description

This program simulates a basic authentication system.

### Features

* Stores a predefined password.
* Allows a maximum of 3 attempts.
* Displays:

  * Access Granted
  * Account Locked

### Logic Used

* Store the correct password.
* Use a loop for three attempts.
* Compare user input with the stored password.
* Grant access if matched.
* Lock account after three failed attempts.

---

## 🔹 Part E: Username Generator

### Description

This utility generates multiple username suggestions based on:

* First Name
* Last Name
* Birth Year

### Example

**Input**

```text
First Name: Soham
Last Name: Patel
Birth Year: 2004
```

**Output**

```text
sohampatel2004
s.patel04
patel_soham
soham_2004
patel2004
```

### Logic Used

* Accept user details.
* Perform string manipulation.
* Combine names and birth year in different formats.
* Display at least five username suggestions.

---

## ⭐ Bonus Challenge: Number Guessing Game

### Description

A simple game where the user guesses a secret number between 1 and 50.

### Features

* Random number generation.
* Unlimited attempts until correct guess.
* Displays total attempts taken.

### Logic Used

* Generate a random number.
* Use a loop until the correct number is guessed.
* Count and display attempts.

---

## 🛠 Concepts Practiced

### Python

* for Loops
* while Loops
* range()
* String Manipulation
* Random Module

### C Programming

* for Loop
* while Loop
* do-while Loop
* Nested Loops
* String Functions

### Common Concepts

* Loop Control
* Iteration
* Pattern Printing
* Algorithm Design
* Basic Authentication Logic

---

## 📸 Screenshots

Execution screenshots for all programs are included in the Screenshots folder.

---

## 🚀 Conclusion

This task improved understanding of loops, nested loops, conditional statements, string manipulation, pattern printing, authentication logic, and basic automation concepts in both Python and C Programming.
