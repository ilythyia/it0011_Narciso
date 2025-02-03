def file_student_info():
    """Collects student information and saves it to a file."""
    
    f_name = input("Enter your first name: ")
    l_name = input("Enter your last name: ")
    age = input("Enter your age : ")
    co_number = input("Enter contact number: ")
    course = input("Enter course: ")

    student_info = f"{l_name}, {f_name}, {age}, {co_number}, {course}\n"

    try:
        with open("students.txt", "a") as file:
            file.write(student_info)
        print("Student information has been saved to 'student.txt'. ")
        
    except Exception as e: 
        print(f"An error occured:{e}")
        
file_student_info()