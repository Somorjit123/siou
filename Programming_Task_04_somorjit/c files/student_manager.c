name = input("Enter Name: ")
roll = input("Enter Roll Number: ")
branch = input("Enter Branch: ")
marks = input("Enter Marks: ")

with open("student_data.txt", "w") as file:
    file.write(f"Name: {name}\n")
    file.write(f"Roll No: {roll}\n")
    file.write(f"Branch: {branch}\n")
    file.write(f"Marks: {marks}\n")

print("Student Record Saved Successfully")

print("\nReading File...\n")

with open("student_data.txt", "r") as file:
    print(file.read())