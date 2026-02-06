# 🎓 Student Data Organizer – Python Console Project

A **menu-driven Python console application** that helps manage student records using basic data structures and control flow.  
This project is created to strengthen **Python logic, CRUD operations, and problem-solving skills** and is suitable for **college, GitHub, and internship submissions**.

---

## 📌 Project Description

The **Student Data Organizer** allows users to store and manage student information such as:
- Student ID
- Name
- Age
- Grade
- Date of Birth
- Subjects

The program runs continuously using a menu system until the user chooses to exit.

---

## 🎯 Objectives
- Practice Python programming fundamentals
- Use lists, dictionaries, and sets effectively
- Implement CRUD operations
- Build a menu-driven console application
- Improve logical thinking and control flow

---

## 🛠️ Features

### ➕ Add Student
- Takes student details from user input
- Stores data using a dictionary inside a list
- Subjects are entered as comma-separated values

### 📋 Display All Students
- Displays all stored student records
- Shows ID, name, age, grade, and subjects
- Handles empty records safely

### ✏️ Update Student Information
- Updates student details using **Student ID**
- Allows modification of:
  - Name
  - Age
  - Grade
  - Date of Birth
  - Subjects

### ❌ Delete Student
- Deletes a student record using Student ID
- Ensures correct record removal

### 📚 Display Subjects Offered
- Displays all **unique subjects**
- Uses `set` to remove duplicates

### 🚪 Exit Program
- Gracefully terminates the program

---

## 🧩 Concepts Used
- `while` loop for continuous execution
- `for` loop for traversing records
- `match-case` statement (Python 3.10+)
- Lists, dictionaries, and sets
- Input validation
- `break` statement
- Menu-driven programming

---

## 🧪 Sample Output

```text
Welcome to the Student Data Organizer!

1. Add Student
2. Display All Students
3. Update Student Information
4. Delete Student
5. Display Subjects Offered
6. Exit

Enter your choice: 1
Student added successfully!

--- Display All Students ---
Student ID: 101
Name: Rahul
Age: 20
Grade: A
Subjects: Math, Physics, Python
