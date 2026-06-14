def display_student_info(name, roll, branch, semester):
    print("\nStudent Information")
    print("Name:", name)
    print("Roll No:", roll)
    print("Branch:", branch)
    print("Semester:", semester)

name = input("Enter Name: ")
roll = input("Enter Roll Number: ")
branch = input("Enter Branch: ")
semester = input("Enter Semester: ")

display_student_info(name, roll, branch, semester)