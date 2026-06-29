# 📂 Smart File Organizer

> **Python Programming Task 08: File Organizer & Data Management System**

A real-world Python automation application that automatically organizes files into categorized folders based on their file extensions. This project demonstrates file handling, directory management, object-oriented programming, exception handling, and automation concepts.

---

# 🎯 Objective

The purpose of this task is to build a real-world automation application using Python.

Students will learn how to work with:

* 📁 Files
* 📂 Directories
* 🏗️ Object-Oriented Programming (OOP)
* ⚠️ Exception Handling
* 🤖 Automation

while developing a utility that can be used in everyday life.

---

# 📌 Project Title

## 📂 Smart File Organizer

Build a Python application that automatically organizes files into different folders based on their file extensions.

---

# 📝 Problem Statement

Imagine you have a **Downloads** folder containing hundreds of files.

The application automatically organizes them into separate folders such as:

* 🖼️ Images
* 📄 Documents
* 🎥 Videos
* 🎵 Audio
* 📦 Archives
* 💻 Programs
* 📁 Others

This helps keep your folders clean, organized, and easy to navigate.

---

# 🚀 Modules

## 📁 Module 1: Directory Selection

Allow the user to enter a folder path.

### Features

* 📂 Enter Folder Path
* ✅ Verify whether the directory exists
* ⚠️ Handle invalid paths gracefully

### Example

```text
Enter Folder Path:
C:\Users\Somorjit\Downloads
```

---

## 🔍 Module 2: File Scanning

Scan all files inside the selected directory.

### Display

* 📄 Total Files
* 📃 File Names
* 🏷️ File Extensions

### Example

```text
Found 52 Files

photo.jpg
resume.pdf
movie.mp4
notes.docx
```

---

## 📂 Module 3: Automatic File Organization

Automatically create folders:

* 🖼️ Images
* 📄 Documents
* 🎥 Videos
* 🎵 Audio
* 📦 Archives
* 💻 Programs
* 📁 Others

Move files according to their file extensions.

### Example

```text
photo.jpg
     ↓
Images/

resume.pdf
     ↓
Documents/
```

---

## 📊 Module 4: File Statistics

Generate statistics such as:

* 📄 Total Files
* 🖼️ Images
* 📄 Documents
* 🎥 Videos
* 🎵 Audio Files
* ❓ Unknown Files

Display the statistics in a formatted table.

---

## 🔎 Module 5: Search Functionality

Allow the user to:

* 🔍 Search by File Name
* 🔍 Search by Extension
* 📋 Display Matching Results

---

## 📑 Module 6: Duplicate File Detection

Identify duplicate file names inside the directory.

### Example

```text
Duplicate Files Found

photo.jpg
resume.pdf
```

If no duplicates exist:

```text
No Duplicate Files Found
```

---

## 📝 Module 7: Generate Report

Generate a report named:

```text
file_report.txt
```

The report includes:

* 📅 Date
* 📂 Folder Name
* 📄 Total Files
* 📊 Category-wise Count
* 📑 Duplicate Files
* 📁 Organized Folder Structure

---

## ⚠️ Module 8: Exception Handling

Handle errors such as:

* ❌ Invalid Folder
* 🔒 Permission Denied
* 📄 File Already Exists
* 📂 Missing Folder

The application should never crash unexpectedly.

---
