"""
----Student Records Management System----
1. Add Student record
2. Modify Student record
3. Delete Student record
4. Display Student record
"""

# Import required libraries
import sys

# Global variables

# Function definitions
def display(students_records):
    if students_records:
        print("Student Records:")
        for student in students_records:
            print(student)
    else:
        print("No student records found!!!")

def menu():
    print("Menu")
    print("1. Add Student Record")
    print("2. Modify Student Record")
    print("3. Delete Student Record")
    print("4. Display Student Records")

    return input("Enter your choice (1-4) or 'exit' to quit: ")

def addStudentRecord():
    global students_records
    global student_id

    # Get student information from user
    student_name = input("Enter Student Name: ")
    student_address = input("Enter Student Address: ")
    student_age = input("Enter Student Age: ")
    student_id = student_id + 1

    # Create a student record
    student = {
        'id': student_id,
        'name': student_name,
        'address': student_address,
        'age': student_age
    }

    # Add student record to the list
    students_records.append(student)

def modifyStudentRecord(students_records): 

    if students_records:
        display(students_records)
        mod_id = int(input("Enter the Student ID to modify: "))
        for student in students_records:
            if student['id'] == mod_id:
                student_name = input("Enter new name (leave blank to keep current): ")
                student_address = input("Enter new address (leave blank to keep current): ")
                student_age = input("Enter new age (leave blank to keep current): ")

                if student_name:
                    student['name'] = student_name
                if student_address:
                    student['address'] = student_address
                if student_age:
                    student['age'] = student_age

                print(f"Student with ID {mod_id} has been updated.")
                break
    else:
        print("No student records to modify.")

# Entry point function
def main():
    global students_records
    global student_id
    students_records = []   # List to hold student records
    student_id = 0          # Initial student ID
    student = {}            # Dictionary to hold individual student details    

    choice = None
    while choice != "exit":
        
        choice = menu()

        if choice == '1':
            addStudentRecord()
        elif choice == '2':
            modifyStudentRecord(students_records)                
        elif choice == '3':
            if students_records:
                display(students_records)
                del_id = int(input("Enter the Student ID to delete: "))
                
                for student in students_records:
                    if student['id'] == del_id:
                        students_records.remove(student)
                        print(f"Student with ID {del_id} has been deleted.")
                        break
        elif choice == '4':
            display(students_records)
        elif choice == "exit":
            print("Exiting the program.")   
        else:
            print("Invalid choice. Please try again.")
    sys.exit(0)

# Function call
main()