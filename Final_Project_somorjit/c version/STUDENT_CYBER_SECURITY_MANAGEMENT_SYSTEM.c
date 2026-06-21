"""
=====================================================
 STUDENT CYBER SECURITY MANAGEMENT SYSTEM
=====================================================
A menu-driven console application to manage student
records and basic cyber security information.

Data is persisted in a plain text file: students.txt
=====================================================
"""

import os
import re
import random
import string

# ---------------------------------------------------
# CONSTANTS
# ---------------------------------------------------
FILE_NAME = "students.txt"
FIELD_SEP = "|"   # separator used inside each line of students.txt


# =====================================================
#  FILE STORAGE HELPERS  (Module 7: File Storage)
# =====================================================

def ensure_file_exists():
    """Create students.txt if it does not already exist."""
    if not os.path.exists(FILE_NAME):
        open(FILE_NAME, "w").close()


def load_students():
    """
    Read all records from students.txt and return them as a
    list of dictionaries. Each line in the file is stored as:

    id|name|branch|email|mfa|pwd_length|updated|antivirus|score|status
    """
    ensure_file_exists()
    students = []
    with open(FILE_NAME, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(FIELD_SEP)
            # Skip malformed lines instead of crashing the program
            if len(parts) != 10:
                continue
            student = {
                "id": parts[0],
                "name": parts[1],
                "branch": parts[2],
                "email": parts[3],
                "mfa": parts[4],
                "pwd_length": parts[5],
                "updated": parts[6],
                "antivirus": parts[7],
                "score": parts[8],
                "status": parts[9],
            }
            students.append(student)
    return students


def save_all_students(students):
    """Overwrite students.txt with the full given list of student dicts."""
    with open(FILE_NAME, "w") as f:
        for s in students:
            line = FIELD_SEP.join([
                s.get("id", ""),
                s.get("name", ""),
                s.get("branch", ""),
                s.get("email", ""),
                s.get("mfa", "Not Assessed"),
                s.get("pwd_length", "0"),
                s.get("updated", "Not Assessed"),
                s.get("antivirus", "Not Assessed"),
                s.get("score", "0"),
                s.get("status", "Not Assessed"),
            ])
            f.write(line + "\n")


def append_student(student):
    """Append a single new student record to students.txt."""
    with open(FILE_NAME, "a") as f:
        line = FIELD_SEP.join([
            student["id"],
            student["name"],
            student["branch"],
            student["email"],
            student.get("mfa", "Not Assessed"),
            student.get("pwd_length", "0"),
            student.get("updated", "Not Assessed"),
            student.get("antivirus", "Not Assessed"),
            student.get("score", "0"),
            student.get("status", "Not Assessed"),
        ])
        f.write(line + "\n")


# =====================================================
#  UTILITY / UI HELPERS
# =====================================================

def print_header(title):
    width = 50
    print("\n" + "=" * width)
    print(title.center(width))
    print("=" * width)


def pause():
    input("\nPress Enter to return to the main menu...")


def get_non_empty_input(prompt):
    """Keeps asking until the user types something other than blank spaces."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  [Error] This field cannot be empty. Please try again.")


def get_yes_no(prompt):
    """Asks a yes/no question and returns True/False. Handles bad input."""
    while True:
        value = input(prompt + " (yes/no): ").strip().lower()
        if value in ("yes", "y"):
            return True
        elif value in ("no", "n"):
            return False
        print("  [Error] Please answer with 'yes' or 'no'.")


def get_valid_email(prompt):
    """Basic email format validation."""
    pattern = r"^[^@\s]+@[^@\s]+\.[a-zA-Z]+$"
    while True:
        value = input(prompt).strip()
        if re.match(pattern, value):
            return value
        print("  [Error] Invalid email format. Example: name@example.com")


def get_unique_student_id(existing_students):
    """Ensures the entered student ID is numeric and not already used."""
    existing_ids = {s["id"] for s in existing_students}
    while True:
        value = input("Enter Student ID: ").strip()
        if not value.isdigit():
            print("  [Error] Student ID must be numeric.")
            continue
        if value in existing_ids:
            print("  [Error] A student with this ID already exists.")
            continue
        return value


def get_positive_int(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit() and int(value) > 0:
            return int(value)
        print("  [Error] Please enter a positive whole number.")


# =====================================================
#  MODULE 1: ADD STUDENT
# =====================================================

def add_student():
    print_header("ADD NEW STUDENT")
    students = load_students()

    student_id = get_unique_student_id(students)
    name = get_non_empty_input("Enter Student Name: ")
    branch = get_non_empty_input("Enter Branch: ")
    email = get_valid_email("Enter Email Address: ")

    new_student = {
        "id": student_id,
        "name": name,
        "branch": branch,
        "email": email,
        "mfa": "Not Assessed",
        "pwd_length": "0",
        "updated": "Not Assessed",
        "antivirus": "Not Assessed",
        "score": "0",
        "status": "Not Assessed",
    }

    append_student(new_student)
    print(f"\n[Success] Student '{name}' (ID: {student_id}) has been added and saved.")
    pause()


# =====================================================
#  MODULE 2: VIEW STUDENTS
# =====================================================

def display_student(s):
    print("-" * 50)
    print(f" ID            : {s['id']}")
    print(f" Name          : {s['name']}")
    print(f" Branch        : {s['branch']}")
    print(f" Email         : {s['email']}")
    print(f" Security Score: {s['score']}/100")
    print(f" Status        : {s['status']}")
    print("-" * 50)


def view_students():
    print_header("ALL STUDENT RECORDS")
    students = load_students()

    if not students:
        print("No student records found. Please add a student first.")
    else:
        for s in students:
            display_student(s)
        print(f"\nTotal Students: {len(students)}")

    pause()


# =====================================================
#  MODULE 3: SEARCH STUDENT
# =====================================================

def search_student():
    print_header("SEARCH STUDENT")
    students = load_students()

    if not students:
        print("No student records found. Please add a student first.")
        pause()
        return

    print("Search by:")
    print("  1. Name")
    print("  2. Student ID")
    choice = input("Enter your choice (1-2): ").strip()

    results = []
    if choice == "1":
        keyword = get_non_empty_input("Enter Name (or part of it) to search: ").lower()
        results = [s for s in students if keyword in s["name"].lower()]
    elif choice == "2":
        keyword = get_non_empty_input("Enter Student ID to search: ").strip()
        results = [s for s in students if s["id"] == keyword]
    else:
        print("  [Error] Invalid choice.")
        pause()
        return

    if results:
        print(f"\n{len(results)} matching record(s) found:\n")
        for s in results:
            display_student(s)
    else:
        print("\nNo matching student record found.")

    pause()


# =====================================================
#  MODULE 4: DELETE STUDENT
# =====================================================

def delete_student():
    print_header("DELETE STUDENT")
    students = load_students()

    if not students:
        print("No student records found. Please add a student first.")
        pause()
        return

    student_id = get_non_empty_input("Enter Student ID to delete: ").strip()
    matched = [s for s in students if s["id"] == student_id]

    if not matched:
        print(f"\n[Error] No student found with ID {student_id}.")
        pause()
        return

    student = matched[0]
    print("\nRecord to be deleted:")
    display_student(student)

    confirm = get_yes_no("Are you sure you want to delete this record?")
    if confirm:
        remaining = [s for s in students if s["id"] != student_id]
        save_all_students(remaining)
        print(f"\n[Success] Student ID {student_id} ({student['name']}) has been deleted.")
    else:
        print("\n[Cancelled] Deletion was cancelled. No changes were made.")

    pause()


# =====================================================
#  MODULE 5: SECURITY ASSESSMENT
# =====================================================

def calculate_security_score(mfa_enabled, pwd_length, system_updated, antivirus_installed):
    """
    Simple weighted scoring model out of 100:
      MFA Enabled        -> 30 points
      Password Length     -> up to 30 points (scales with length, capped)
      System Updated      -> 20 points
      Antivirus Installed -> 20 points
    """
    score = 0

    if mfa_enabled:
        score += 30

    if pwd_length >= 12:
        score += 30
    elif pwd_length >= 8:
        score += 20
    elif pwd_length >= 6:
        score += 10
    # below 6 characters -> 0 points for this category

    if system_updated:
        score += 20

    if antivirus_installed:
        score += 20

    return score


def get_security_status(score):
    if score >= 90:
        return "Excellent"
    elif score >= 70:
        return "Good"
    elif score >= 50:
        return "Moderate"
    else:
        return "Poor"


def security_assessment():
    print_header("SECURITY ASSESSMENT")
    students = load_students()

    if not students:
        print("No student records found. Please add a student first.")
        pause()
        return

    student_id = get_non_empty_input("Enter Student ID for assessment: ").strip()
    matched = [s for s in students if s["id"] == student_id]

    if not matched:
        print(f"\n[Error] No student found with ID {student_id}.")
        pause()
        return

    student = matched[0]
    print(f"\nRunning security assessment for: {student['name']} (ID: {student['id']})\n")

    mfa_enabled = get_yes_no("Is MFA (Multi-Factor Authentication) Enabled?")
    pwd_length = get_positive_int("Enter Password Length: ")
    system_updated = get_yes_no("Is the System Updated (latest OS/software updates)?")
    antivirus_installed = get_yes_no("Is Antivirus Installed?")

    score = calculate_security_score(mfa_enabled, pwd_length, system_updated, antivirus_installed)
    status = get_security_status(score)

    # Update the student record in place
    student["mfa"] = "Yes" if mfa_enabled else "No"
    student["pwd_length"] = str(pwd_length)
    student["updated"] = "Yes" if system_updated else "No"
    student["antivirus"] = "Yes" if antivirus_installed else "No"
    student["score"] = str(score)
    student["status"] = status

    save_all_students(students)

    print("\n" + "-" * 50)
    print(f" Security Score: {score}/100")
    print(f" Status        : {status} Security Practices")
    print("-" * 50)
    print("\n[Saved] Assessment results have been saved to the student record.")

    pause()


# =====================================================
#  MODULE 6: GENERATE REPORT
# =====================================================

def generate_report():
    print_header("SECURITY SUMMARY REPORT")
    students = load_students()

    if not students:
        print("No student records found. Please add a student first.")
        pause()
        return

    total_students = len(students)

    assessed = [s for s in students if s["status"] != "Not Assessed"]
    scores = [int(s["score"]) for s in assessed]

    avg_score = round(sum(scores) / len(scores), 2) if scores else 0
    poor_students = [s for s in assessed if s["status"] == "Poor"]

    print(f" Total Students             : {total_students}")
    print(f" Students Assessed          : {len(assessed)}")
    print(f" Average Security Score     : {avg_score}/100")
    print(f" Students with Poor Rating  : {len(poor_students)}")

    print("\n Individual Security Scores:")
    print("-" * 50)
    if assessed:
        for s in assessed:
            print(f" {s['id']:<6} {s['name']:<20} Score: {s['score']:>3}/100  [{s['status']}]")
    else:
        print(" No students have completed a security assessment yet.")

    if poor_students:
        print("\n Students Needing Attention (Poor Security Rating):")
        print("-" * 50)
        for s in poor_students:
            print(f" {s['id']:<6} {s['name']:<20} Score: {s['score']}/100")

    pause()


# =====================================================
#  CYBER SECURITY FEATURE 1: PASSWORD STRENGTH CHECKER
# =====================================================

def password_strength_checker():
    print_header("PASSWORD STRENGTH CHECKER")
    password = input("Enter a password to check its strength: ")

    if not password:
        print("[Error] No password entered.")
        pause()
        return

    length_ok = len(password) >= 8
    has_upper = bool(re.search(r"[A-Z]", password))
    has_lower = bool(re.search(r"[a-z]", password))
    has_digit = bool(re.search(r"[0-9]", password))
    has_symbol = bool(re.search(r"[!@#$%^&*(),.?\":{}|<>_\-+=]", password))

    criteria_met = sum([length_ok, has_upper, has_lower, has_digit, has_symbol])

    print("\nPassword Criteria Check:")
    print(f"  [{'OK' if length_ok else 'X '}] Minimum 8 characters")
    print(f"  [{'OK' if has_upper else 'X '}] Contains uppercase letter")
    print(f"  [{'OK' if has_lower else 'X '}] Contains lowercase letter")
    print(f"  [{'OK' if has_digit else 'X '}] Contains a number")
    print(f"  [{'OK' if has_symbol else 'X '}] Contains a special character")

    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    print(f"\nOverall Password Strength: {strength} ({criteria_met}/5 criteria met)")
    pause()


# =====================================================
#  CYBER SECURITY FEATURE 2: USERNAME GENERATOR
# =====================================================

def username_generator():
    print_header("SECURE USERNAME GENERATOR")
    name = get_non_empty_input("Enter your name: ")
    add_numbers = get_yes_no("Add random numbers to make it more unique?")

    base = re.sub(r"[^a-zA-Z]", "", name).lower()
    if not base:
        base = "user"

    suggestions = []
    for _ in range(5):
        username = base
        if add_numbers:
            username += str(random.randint(100, 9999))
        else:
            username += random.choice(string.ascii_lowercase) + random.choice(string.ascii_lowercase)
        suggestions.append(username)

    print("\nGenerated Username Suggestions:")
    for i, u in enumerate(suggestions, start=1):
        print(f"  {i}. {u}")

    pause()


# =====================================================
#  CYBER SECURITY FEATURE 3: SECURITY AWARENESS QUIZ
# =====================================================

QUIZ_QUESTIONS = [
    {
        "question": "What should you do if you receive an email asking for your password?",
        "options": ["A. Reply with your password", "B. Delete it / Report it as phishing", "C. Forward it to friends"],
        "answer": "B",
    },
    {
        "question": "Which of these is the strongest password?",
        "options": ["A. 123456", "B. password", "C. Tr@il_M1xer!92"],
        "answer": "C",
    },
    {
        "question": "What does MFA stand for?",
        "options": ["A. Multi-Factor Authentication", "B. Mobile File Access", "C. Main Firewall Application"],
        "answer": "A",
    },
    {
        "question": "Is it safe to use the same password on multiple websites?",
        "options": ["A. Yes, it's convenient", "B. No, it increases risk if one site is breached", "C. Only for unimportant sites"],
        "answer": "B",
    },
    {
        "question": "What should you do before clicking a link in an unexpected message?",
        "options": ["A. Click it immediately", "B. Verify the sender and hover/check the link first", "C. Share it with others first"],
        "answer": "B",
    },
]


def security_awareness_quiz():
    print_header("SECURITY AWARENESS QUIZ")
    print("Answer each question by typing A, B, or C.\n")

    score = 0
    total = len(QUIZ_QUESTIONS)

    for i, q in enumerate(QUIZ_QUESTIONS, start=1):
        print(f"Q{i}. {q['question']}")
        for option in q["options"]:
            print(f"     {option}")

        while True:
            answer = input("  Your answer: ").strip().upper()
            if answer in ("A", "B", "C"):
                break
            print("  [Error] Please answer with A, B, or C.")

        if answer == q["answer"]:
            print("  Correct!\n")
            score += 1
        else:
            print(f"  Incorrect. The correct answer was {q['answer']}.\n")

    percentage = round((score / total) * 100, 2)
    print("-" * 50)
    print(f" Quiz Complete! You scored {score}/{total} ({percentage}%)")

    if percentage >= 80:
        print(" Awareness Level: Excellent")
    elif percentage >= 60:
        print(" Awareness Level: Good")
    elif percentage >= 40:
        print(" Awareness Level: Moderate")
    else:
        print(" Awareness Level: Needs Improvement")

    pause()


# =====================================================
#  CYBER SECURITY TOOLS SUB-MENU
# =====================================================

def cyber_tools_menu():
    while True:
        print_header("CYBER SECURITY TOOLS")
        print("1. Password Strength Checker")
        print("2. Username Generator")
        print("3. Security Awareness Quiz")
        print("4. Back to Main Menu")

        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == "1":
            password_strength_checker()
        elif choice == "2":
            username_generator()
        elif choice == "3":
            security_awareness_quiz()
        elif choice == "4":
            break
        else:
            print("  [Error] Invalid choice. Please select between 1 and 4.")
            pause()


# =====================================================
#  MAIN MENU
# =====================================================

def main_menu():
    ensure_file_exists()

    while True:
        print("\n==========================================")
        print("       Student Cyber Security Manager")
        print("==========================================")
        print(" 1. Add Student")
        print(" 2. View Students")
        print(" 3. Search Student")
        print(" 4. Delete Student")
        print(" 5. Security Assessment")
        print(" 6. Generate Report")
        print(" 7. Cyber Security Tools")
        print(" 8. Exit")
        print("==========================================")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            security_assessment()
        elif choice == "6":
            generate_report()
        elif choice == "7":
            cyber_tools_menu()
        elif choice == "8":
            print("\nThank you for using the Student Cyber Security Manager. Goodbye!")
            break
        else:
            print("  [Error] Invalid choice. Please select a number between 1 and 8.")
            pause()


if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user. Exiting safely...")