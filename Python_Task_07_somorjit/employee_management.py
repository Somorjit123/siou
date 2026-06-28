"""
Employee Management System
Python Programming Task 07: Object-Oriented Programming (OOP)

A menu-driven console application demonstrating OOP concepts
(classes, objects, encapsulation) to manage employee records.
"""

import csv
import os


# -------------------------------------------------------------------
# Part A: Employee Class
# -------------------------------------------------------------------
class Employee:
    """Represents a single employee record."""

    def __init__(self, emp_id, name, department, designation, salary):
        self.emp_id = emp_id
        self.name = name
        self.department = department
        self.designation = designation
        self.salary = salary

    def to_dict(self):
        """Convert employee object to a dictionary (used for CSV export)."""
        return {
            "ID": self.emp_id,
            "Name": self.name,
            "Department": self.department,
            "Designation": self.designation,
            "Salary": self.salary,
        }

    def __str__(self):
        return (f"{self.emp_id:<6}{self.name:<15}{self.department:<15}"
                f"{self.designation:<15}{self.salary:<10}")


# -------------------------------------------------------------------
# Employee Management System Class
# -------------------------------------------------------------------
class EmployeeManagementSystem:
    """Manages a collection of Employee objects and all operations."""

    def __init__(self):
        self.employees = []  # list of Employee objects

    # ---------------- Part B: Add Employee ----------------
    def add_employee(self):
        print("\n--- Add New Employee ---")
        emp_id = input("Enter Employee ID: ").strip()

        # Prevent duplicate IDs
        if self.find_by_id(emp_id):
            print(f"Employee ID '{emp_id}' already exists. Use a unique ID.")
            return

        name = input("Enter Employee Name: ").strip()
        department = input("Enter Department: ").strip()
        designation = input("Enter Designation: ").strip()

        salary = self._get_valid_salary()
        if salary is None:
            print("Add Employee cancelled due to invalid salary input.")
            return

        new_employee = Employee(emp_id, name, department, designation, salary)
        self.employees.append(new_employee)
        print(f"Employee '{name}' added successfully!")

    @staticmethod
    def _get_valid_salary():
        """Helper to safely read a numeric salary from the user."""
        salary_input = input("Enter Salary: ").strip()
        try:
            return float(salary_input)
        except ValueError:
            print("Invalid salary. Please enter a numeric value.")
            return None

    # ---------------- Part C: View Employees ----------------
    def view_employees(self):
        print("\n--- Employee Records ---")
        if not self.employees:
            print("No employee records found.")
            return

        print("-" * 70)
        print(f"{'ID':<6}{'Name':<15}{'Department':<15}{'Designation':<15}{'Salary':<10}")
        print("-" * 70)
        for emp in self.employees:
            print(emp)
        print("-" * 70)

    # ---------------- Part D: Search Employee ----------------
    def search_employee(self):
        print("\n--- Search Employee ---")
        print("1. Search by ID")
        print("2. Search by Name")
        choice = input("Enter choice (1/2): ").strip()

        if choice == "1":
            emp_id = input("Enter Employee ID: ").strip()
            emp = self.find_by_id(emp_id)
            self._display_search_result(emp)
        elif choice == "2":
            name = input("Enter Employee Name: ").strip()
            matches = self.find_by_name(name)
            if matches:
                print("\n--- Matching Records ---")
                print("-" * 70)
                print(f"{'ID':<6}{'Name':<15}{'Department':<15}{'Designation':<15}{'Salary':<10}")
                print("-" * 70)
                for emp in matches:
                    print(emp)
                print("-" * 70)
            else:
                print("Employee Not Found")
        else:
            print("Invalid choice.")

    @staticmethod
    def _display_search_result(emp):
        if emp:
            print("\n--- Employee Found ---")
            print(f"ID         : {emp.emp_id}")
            print(f"Name       : {emp.name}")
            print(f"Department : {emp.department}")
            print(f"Designation: {emp.designation}")
            print(f"Salary     : {emp.salary}")
        else:
            print("Employee Not Found")

    def find_by_id(self, emp_id):
        for emp in self.employees:
            if emp.emp_id == emp_id:
                return emp
        return None

    def find_by_name(self, name):
        return [emp for emp in self.employees if emp.name.lower() == name.lower()]

    # ---------------- Part E: Update Employee ----------------
    def update_employee(self):
        print("\n--- Update Employee ---")
        emp_id = input("Enter Employee ID to update: ").strip()
        emp = self.find_by_id(emp_id)

        if not emp:
            print("Employee Not Found")
            return

        print(f"Updating record for {emp.name} (leave blank to keep current value)")

        new_department = input(f"Enter new Department [{emp.department}]: ").strip()
        new_designation = input(f"Enter new Designation [{emp.designation}]: ").strip()
        new_salary = input(f"Enter new Salary [{emp.salary}]: ").strip()

        if new_department:
            emp.department = new_department
        if new_designation:
            emp.designation = new_designation
        if new_salary:
            try:
                emp.salary = float(new_salary)
            except ValueError:
                print("Invalid salary entered. Salary not updated.")

        print("Employee record updated successfully!")

    # ---------------- Part F: Delete Employee ----------------
    def delete_employee(self):
        print("\n--- Delete Employee ---")
        emp_id = input("Enter Employee ID to delete: ").strip()
        emp = self.find_by_id(emp_id)

        if not emp:
            print("Employee Not Found")
            return

        confirm = input(f"Are you sure you want to delete {emp.name} (ID: {emp.emp_id})? (y/n): ").strip().lower()
        if confirm == "y":
            self.employees.remove(emp)
            print("Employee Deleted Successfully")
        else:
            print("Deletion cancelled.")

    # ---------------- Part G: Salary Statistics ----------------
    def salary_statistics(self):
        print("\n--- Salary Statistics ---")
        if not self.employees:
            print("No employee records found.")
            return

        salaries = [emp.salary for emp in self.employees]
        highest = max(salaries)
        lowest = min(salaries)
        average = sum(salaries) / len(salaries)

        highest_emp = next(emp for emp in self.employees if emp.salary == highest)
        lowest_emp = next(emp for emp in self.employees if emp.salary == lowest)

        print(f"Total Employees : {len(self.employees)}")
        print(f"Highest Salary  : {highest} (Employee: {highest_emp.name}, ID: {highest_emp.emp_id})")
        print(f"Lowest Salary   : {lowest} (Employee: {lowest_emp.name}, ID: {lowest_emp.emp_id})")
        print(f"Average Salary  : {average:.2f}")

    # ---------------- Part H: Export Data ----------------
    def export_to_csv(self, filename="employees.csv"):
        print("\n--- Export Data ---")
        if not self.employees:
            print("No employee records found to export.")
            return

        fieldnames = ["ID", "Name", "Department", "Designation", "Salary"]
        try:
            with open(filename, mode="w", newline="", encoding="utf-8") as f:
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                for emp in self.employees:
                    writer.writerow(emp.to_dict())
            print(f"Employee data exported successfully to '{filename}'.")
        except IOError as e:
            print(f"Error writing file: {e}")
            return

        self.read_from_csv(filename)

    @staticmethod
    def read_from_csv(filename="employees.csv"):
        print(f"\n--- Reading Records Back from '{filename}' ---")
        if not os.path.exists(filename):
            print(f"File '{filename}' not found.")
            return

        try:
            with open(filename, mode="r", newline="", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                rows = list(reader)

            if not rows:
                print("The file is empty.")
                return

            print("-" * 70)
            print(f"{'ID':<6}{'Name':<15}{'Department':<15}{'Designation':<15}{'Salary':<10}")
            print("-" * 70)
            for row in rows:
                print(f"{row['ID']:<6}{row['Name']:<15}{row['Department']:<15}"
                      f"{row['Designation']:<15}{row['Salary']:<10}")
            print("-" * 70)
        except IOError as e:
            print(f"Error reading file: {e}")


# -------------------------------------------------------------------
# Menu-Driven Program
# -------------------------------------------------------------------
def main():
    system = EmployeeManagementSystem()

    menu = """
========================================
      EMPLOYEE MANAGEMENT SYSTEM
========================================
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Salary Statistics
7. Export Data (CSV) & Read Back
8. Exit
========================================
"""

    while True:
        print(menu)
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            system.add_employee()
        elif choice == "2":
            system.view_employees()
        elif choice == "3":
            system.search_employee()
        elif choice == "4":
            system.update_employee()
        elif choice == "5":
            system.delete_employee()
        elif choice == "6":
            system.salary_statistics()
        elif choice == "7":
            system.export_to_csv()
        elif choice == "8":
            print("Exiting Employee Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
