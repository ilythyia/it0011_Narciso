def show_student_info():
    """Reads student information from a file and displays it."""
    
    try:
        with open("students.txt", "r") as file:
            print("Reading Student Information: ")
            for line in file:
                l_name, f_name, age, co_number, course = [
                    x.strip() for x in line.strip().split(",")
                ]
            
            print("Last Name: ", l_name)
            print("First Name: ", f_name)
            print("Age: ", age)
            print("Contact Number: ", co_number)
            print("Course: ", course)
            print()
        
    except Exception as e: 
        print(f"An error occured:{e}")
        
show_student_info()