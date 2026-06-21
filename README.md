# Student Cyber Security Management System

## 📌 Project Overview

The **Student Cyber Security Management System** is a menu-driven Python application that combines student record management with basic cyber security assessment tools.

This project was developed to demonstrate practical use of:

* Variables
* Input/Output Operations
* Conditional Statements
* Loops
* Functions
* Lists
* File Handling
* Problem Solving

The system stores student information, evaluates cyber security practices, generates reports, and provides useful cyber security utilities.

---

## 🎯 Objective

The objective of this project is to build a simple console-based application that can:

* Manage student records efficiently
* Assess basic cyber security practices
* Generate security reports
* Store data using text files
* Promote cyber security awareness

The project uses only Python's standard library and a text file (`students.txt`) for data storage.

---

## ✨ Features

### 👨‍🎓 Student Record Management

#### Add Student

Stores:

* Student Name
* Student ID
* Branch
* Email Address

Features:

* Unique Student ID validation
* Email format validation
* Empty field prevention

#### View Students

Displays all stored student records in a formatted layout.

#### Search Student

Search by:

* Student Name
* Student ID

Supports partial name matching.

#### Delete Student

* Delete student records safely
* Confirmation before deletion

---

### 🔐 Security Assessment

Evaluates:

* Multi-Factor Authentication (MFA)
* Password Length
* System Updates
* Antivirus Installation

Generates a Security Score out of 100.

#### Security Categories

| Score Range | Status    |
| ----------- | --------- |
| 90 - 100    | Excellent |
| 70 - 89     | Good      |
| 50 - 69     | Moderate  |
| Below 50    | Poor      |

---

### 📊 Report Generation

Displays:

* Total Students
* Students Assessed
* Average Security Score
* Individual Security Scores
* Students with Poor Security Ratings

---

### 🛡 Cyber Security Utilities

#### 1. Password Strength Checker

Evaluates passwords based on:

* Length
* Uppercase Letters
* Lowercase Letters
* Numbers
* Special Characters

Ratings:

* Very Weak
* Weak
* Moderate
* Strong
* Very Strong

---

#### 2. Username Generator

Generates secure username suggestions based on a user's name.

Features:

* Randomized usernames
* Multiple suggestions
* Easy customization

---

#### 3. Security Awareness Quiz

Interactive cyber security quiz covering:

* Phishing
* Password Security
* MFA
* Safe Browsing
* Security Best Practices

Provides a final awareness score.

---

## 💾 File Storage

Student data is stored in:

```text
students.txt
```

Record Format:

```text
StudentID|Name|Branch|Email|SecurityScore|SecurityStatus
```

Supported Operations:

* Create Records
* Read Records
* Update Records
* Delete Records

---

## 🖥 User Interface

The application features:

* Menu-Driven Navigation
* Clean Console Output
* Input Validation
* Error Handling
* User-Friendly Design

---

## 🔄 Program Flow

1. Program starts and checks for `students.txt`
2. Displays Main Menu
3. User selects an operation
4. Records are loaded from the file
5. Requested operation is performed
6. Data is updated and saved
7. Returns to Main Menu
8. Continues until Exit is selected

---

## ⚙ Technologies Used

### Programming Language

* Python 3

### Python Standard Library Modules

* `os`
* `re`
* `random`
* `string`

### Storage

* Plain Text File (`students.txt`)

### Platform

* Windows, Linux, or macOS
* Python 3.x

---

## 🧩 Challenges Faced

* Designing a reliable text-file storage format
* Implementing validation without external libraries
* Building a meaningful security scoring system
* Managing file updates safely
* Creating a user-friendly console interface

---

## 📚 Learning Outcomes

Through this project, I learned:

* Structured Python programming
* Function-based program design
* File handling techniques
* Input validation and error handling
* Cyber security fundamentals
* Menu-driven application development
* Data management using flat files

---
