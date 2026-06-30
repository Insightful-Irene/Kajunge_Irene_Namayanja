"""
Student Record Management System
Stores core student data in a CSV file and extra details in a JSON file.
Logs all actions and errors to a log file.
"""

import csv
import json
import os
import logging
import re

CSV_FILE = "students.csv"
JSON_FILE = "students.json"
LOG_FILE = "student_system.log"

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


class StudentNotFoundError(Exception):
    """Raised when a student record cannot be found in the system."""
    pass


class DuplicateRegistrationError(Exception):
    """Raised when trying to add a student with an existing reg number."""
    pass


def initialize_files():
    """Create CSV and JSON files with headers/defaults if they don't exist."""
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["reg_no", "name", "age", "course"])
        logging.info("Created new students.csv file.")

    if not os.path.exists(JSON_FILE):
        with open(JSON_FILE, "w") as f:
            json.dump({}, f, indent=4)
        logging.info("Created new students.json file.")


def load_students():
    students = []
    try:
        with open(CSV_FILE, "r", newline="") as f:
            reader = csv.DictReader(f)
            students = list(reader)
    except FileNotFoundError:
        logging.error("students.csv not found during load.")
    return students


def save_students(students):
    try:
        with open(CSV_FILE, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["reg_no", "name", "age", "course"])
            writer.writeheader()
            writer.writerows(students)
    except Exception as e:
        logging.error(f"Error saving CSV: {e}")
        raise


def load_json_details():
    try:
        with open(JSON_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        logging.warning("students.json missing or corrupt, resetting.")
        return {}


def save_json_details(data):
    try:
        with open(JSON_FILE, "w") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        logging.error(f"Error saving JSON: {e}")
        raise


def validate_reg_no(reg_no):
    if not re.match(r"^[A-Za-z0-9\-]+$", reg_no):
        raise ValueError("Registration number must be alphanumeric (dashes allowed).")
    return reg_no.strip()


def validate_age(age_str):
    if not age_str.isdigit() or not (5 <= int(age_str) <= 100):
        raise ValueError("Age must be a whole number between 5 and 100.")
    return age_str


def validate_non_empty(value, field_name):
    if not value.strip():
        raise ValueError(f"{field_name} cannot be empty.")
    return value.strip()


def add_student():
    """Add a new student to CSV and JSON."""
    try:
        reg_no = validate_reg_no(input("Enter Registration No: "))
        students = load_students()

        if any(s["reg_no"] == reg_no for s in students):
            raise DuplicateRegistrationError(f"Reg No {reg_no} already exists.")

        name = validate_non_empty(input("Enter Name: "), "Name")
        age = validate_age(input("Enter Age: "))
        course = validate_non_empty(input("Enter Course: "), "Course")

        address = input("Enter Address: ").strip()
        contact = input("Enter Contact Number: ").strip()
        program = input("Enter Program: ").strip()

        students.append({"reg_no": reg_no, "name": name, "age": age, "course": course})
        save_students(students)

        details = load_json_details()
        details[reg_no] = {"address": address, "contact": contact, "program": program}
        save_json_details(details)

        print(f"Student {name} added successfully.")
        logging.info(f"Added student {reg_no} - {name}")

    except DuplicateRegistrationError as e:
        print(f"Error: {e}")
        logging.error(str(e))
    except ValueError as e:
        print(f"Invalid input: {e}")
        logging.error(f"Validation error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        logging.error(f"Unexpected error in add_student: {e}")
    finally:
        print("Add student operation finished.")


def view_students():
    """Display all students with merged CSV and JSON details."""
    try:
        students = load_students()
        details = load_json_details()

        if not students:
            print("No student records found.")
            return

        for s in students:
            extra = details.get(s["reg_no"], {})
            print(f"Reg No: {s['reg_no']}")
            print(f"Name: {s['name']}")
            print(f"Age: {s['age']}")
            print(f"Course: {s['course']}")
            print(f"Program: {extra.get('program', '')}")
            print(f"Contact: {extra.get('contact', '')}")
            print(f"Address: {extra.get('address', '')}")
            print()

        logging.info("Viewed all student records.")

    except Exception as e:
        print(f"Error displaying records: {e}")
        logging.error(f"Error in view_students: {e}")


def search_student():
    """Search for a student by registration number."""
    try:
        reg_no = validate_reg_no(input("Enter Registration No to search: "))
        students = load_students()
        student = next((s for s in students if s["reg_no"] == reg_no), None)

        if student is None:
            raise StudentNotFoundError(f"No student found with Reg No {reg_no}.")

        details = load_json_details().get(reg_no, {})
        print(f"Reg No: {student['reg_no']}")
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Course: {student['course']}")
        print(f"Program: {details.get('program', 'N/A')}")
        print(f"Contact: {details.get('contact', 'N/A')}")
        print(f"Address: {details.get('address', 'N/A')}")
        logging.info(f"Searched for student {reg_no} - found.")

    except StudentNotFoundError as e:
        print(f"Error: {e}")
        logging.warning(str(e))
    except ValueError as e:
        print(f"Invalid input: {e}")
        logging.error(f"Validation error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        logging.error(f"Unexpected error in search_student: {e}")
    finally:
        print("Search operation finished.")


def update_student():
    """Update an existing student's details."""
    try:
        reg_no = validate_reg_no(input("Enter Registration No to update: "))
        students = load_students()
        student = next((s for s in students if s["reg_no"] == reg_no), None)

        if student is None:
            raise StudentNotFoundError(f"No student found with Reg No {reg_no}.")

        print("Leave field blank to keep current value.")
        name = input(f"Name ({student['name']}): ").strip()
        age = input(f"Age ({student['age']}): ").strip()
        course = input(f"Course ({student['course']}): ").strip()

        if name:
            student["name"] = validate_non_empty(name, "Name")
        if age:
            student["age"] = validate_age(age)
        if course:
            student["course"] = validate_non_empty(course, "Course")

        save_students(students)

        details = load_json_details()
        extra = details.get(reg_no, {})
        address = input(f"Address ({extra.get('address', '')}): ").strip()
        contact = input(f"Contact ({extra.get('contact', '')}): ").strip()
        program = input(f"Program ({extra.get('program', '')}): ").strip()

        if address:
            extra["address"] = address
        if contact:
            extra["contact"] = contact
        if program:
            extra["program"] = program
        details[reg_no] = extra
        save_json_details(details)

        print("Student record updated successfully.")
        logging.info(f"Updated student {reg_no}")

    except StudentNotFoundError as e:
        print(f"Error: {e}")
        logging.warning(str(e))
    except ValueError as e:
        print(f"Invalid input: {e}")
        logging.error(f"Validation error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        logging.error(f"Unexpected error in update_student: {e}")
    finally:
        print("Update operation finished.")


def delete_student():
    """Delete a student record from both CSV and JSON."""
    try:
        reg_no = validate_reg_no(input("Enter Registration No to delete: "))
        students = load_students()

        if not any(s["reg_no"] == reg_no for s in students):
            raise StudentNotFoundError(f"No student found with Reg No {reg_no}.")

        confirm = input(f"Are you sure you want to delete {reg_no}? (y/n): ").lower()
        if confirm != "y":
            print("Deletion cancelled.")
            return

        students = [s for s in students if s["reg_no"] != reg_no]
        save_students(students)

        details = load_json_details()
        details.pop(reg_no, None)
        save_json_details(details)

        print("Student record deleted successfully.")
        logging.info(f"Deleted student {reg_no}")

    except StudentNotFoundError as e:
        print(f"Error: {e}")
        logging.warning(str(e))
    except ValueError as e:
        print(f"Invalid input: {e}")
        logging.error(f"Validation error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        logging.error(f"Unexpected error in delete_student: {e}")
    finally:
        print("Delete operation finished.")


def main_menu():
    initialize_files()
    logging.info("Student Management System started")

    while True:
        print("Student Record Management System")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student by Reg No")
        print("4. Update Student Details")
        print("5. Delete Student Record")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ").strip()

        try:
            if choice == "1":
                add_student()
            elif choice == "2":
                view_students()
            elif choice == "3":
                search_student()
            elif choice == "4":
                update_student()
            elif choice == "5":
                delete_student()
            elif choice == "6":
                print("Exiting system. Goodbye.")
                logging.info("Student Management System closed")
                break
            else:
                print("Invalid choice. Please select a number from 1 to 6.")
        except Exception as e:
            print(f"A system error occurred: {e}")
            logging.error(f"Menu-level error: {e}")


if __name__ == "__main__":
    main_menu()