student_records = []
current_file = None

def calculate_grade(class_standing, major_exam):
    return (class_standing * 0.6) + (major_exam * 0.4)

def load_file(filename):
    global student_records, current_file
    try:
        with open(filename, 'r') as file:
            student_records = eval(file.read())
        current_file = filename
        print("File loaded successfully.")
    except FileNotFoundError:
        print("File not found.")

def save_file():
    if current_file:
        with open(current_file, 'w') as file:
            file.write(str(student_records))
        print("File saved successfully.")
    else:
        print("No file opened. Use 'Save As' to specify a file name.")

def save_as_file(filename):
    global current_file
    with open(filename, 'w') as file:
        file.write(str(student_records))
    current_file = filename
    print("File saved as:", filename)

def show_all_records():
    for record in student_records:
        print(record)

def order_by_last_name():
    sorted_records = sorted(student_records, key=lambda x: x[1][1])
    for record in sorted_records:
        print(record)

def order_by_grade():
    sorted_records = sorted(student_records, key=lambda x: calculate_grade(x[2], x[3]), reverse=True)
    for record in sorted_records:
        print(record)

def show_student_record(student_id):
    for record in student_records:
        if record[0] == student_id:
            print(record)
            return
    print("Student not found.")

def add_record(student_id, first_name, last_name, class_standing, major_exam):
    student_records.append((student_id, (first_name, last_name), class_standing, major_exam))
    print("Record added successfully.")

def edit_record(student_id, first_name=None, last_name=None, class_standing=None, major_exam=None):
    for i, record in enumerate(student_records):
        if record[0] == student_id:
            new_first_name = first_name if first_name else record[1][0]
            new_last_name = last_name if last_name else record[1][1]
            new_class_standing = class_standing if class_standing is not None else record[2]
            new_major_exam = major_exam if major_exam is not None else record[3]
            student_records[i] = (student_id, (new_first_name, new_last_name), new_class_standing, new_major_exam)
            print("Record updated successfully.")
            return
    print("Student not found.")

def delete_record(student_id):
    global student_records
    student_records = [record for record in student_records if record[0] != student_id]
    print("Record deleted successfully.")

def main():
    while True:
        print("\nStudent Record Management System")
        print("1. Open File")
        print("2. Save File")
        print("3. Save As File")
        print("4. Show All Students Record")
        print("5. Order by Last Name")
        print("6. Order by Grade")
        print("7. Show Student Record")
        print("8. Add Record")
        print("9. Edit Record")
        print("10. Delete Record")
        print("11. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            filename = input("Enter file name: ")
            load_file(filename)
        elif choice == "2":
            save_file()
        elif choice == "3":
            filename = input("Enter new file name: ")
            save_as_file(filename)
        elif choice == "4":
            show_all_records()
        elif choice == "5":
            order_by_last_name()
        elif choice == "6":
            order_by_grade()
        elif choice == "7":
            student_id = input("Enter student ID: ")
            show_student_record(student_id)
        elif choice == "8":
            student_id = input("Enter Student ID (6 digits): ")
            first_name = input("Enter First Name: ")
            last_name = input("Enter Last Name: ")
            class_standing = float(input("Enter Class Standing Grade: "))
            major_exam = float(input("Enter Major Exam Grade: "))
            add_record(student_id, first_name, last_name, class_standing, major_exam)
        elif choice == "9":
            student_id = input("Enter Student ID to edit: ")
            first_name = input("Enter new First Name (press Enter to keep current): ") or None
            last_name = input("Enter new Last Name (press Enter to keep current): ") or None
            class_standing = input("Enter new Class Standing Grade (press Enter to keep current): ")
            major_exam = input("Enter new Major Exam Grade (press Enter to keep current): ")
            class_standing = float(class_standing) if class_standing else None
            major_exam = float(major_exam) if major_exam else None
            edit_record(student_id, first_name, last_name, class_standing, major_exam)
        elif choice == "10":
            student_id = input("Enter Student ID to delete: ")
            delete_record(student_id)
        elif choice == "11":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
