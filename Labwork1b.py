def input_students():
    student_list = []
    n = int(input("Enter number of students: "))
    for i in range(n):
        print("\n--- Student " + str(i + 1) + " ---")
        stuID = input("Enter student ID: ")
        name = input("Enter student name: ")
        DoB = input("Enter date of birth: ")
        
        student = {"id": stuID, "name": name, "dob": DoB}
        student_list.append(student)
        
    return student_list


def input_courses():
    course_list = []
    n = int(input("Enter number of courses: "))
    for i in range(n):
        print("\n--- Course " + str(i + 1) + " ---")
        c_id = input("Enter course ID: ")
        c_name = input("Enter course name: ")
        
        # Lưu vào Dictionary
        course = {"id": c_id, "name": c_name}
        course_list.append(course)
        
    return course_list


def input_marks(students, courses):
    marks = {}
    for course in courses:
        c_id = course["id"]
        print("\n--- Enter marks for course: " + str(course["name"]) + " (ID: " + str(c_id) + ") ---")
        
        marks[c_id] = {}
        for student in students:
            s_id = student["id"]
            mark = float(input("Enter mark for " + str(student["name"]) + " (ID: " + str(s_id) + "): "))
            marks[c_id][s_id] = mark
            
    return marks


def list_students(students):
    print("\n===== STUDENTS =====")
    for student in students:
        print("ID: " + str(student["id"]) + " | Name: " + str(student["name"]) + " | DoB: " + str(student["dob"]))


def list_courses(courses):
    print("\n===== COURSES =====")
    for course in courses:
        print("ID: " + str(course["id"]) + " | Name: " + str(course["name"]))


def show_marks_for_course(students, courses, marks):
    course_id = input("\nEnter course ID to show marks: ")
    if course_id not in marks:
        print("Course ID not found!")
        return

    print("\n===== STUDENT MARKS FOR " + str(course_id) + " =====")
    for student in students:
        s_id = student["id"]
        if s_id in marks[course_id]:
            print(str(student["id"]) + " - " + str(student["name"]) + " : " + str(marks[course_id][s_id]))


students = input_students()
courses = input_courses()
marks = input_marks(students, courses)

list_students(students)
list_courses(courses)
show_marks_for_course(students, courses, marks)