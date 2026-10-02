def students():
    student = []
    n = int(input("Enter number of students: "))
    for i in range(n):
        print("\n Student ", i + 1)
        s_ID = input("Enter student ID: ")
        name = input("Enter student name: ")
        DoB = input("Enter date of birth: ")
        student.append({"id": s_ID, "name": name, "dob": DoB})
    return student

def courses():
    course = []
    n = int(input("Enter number of courses: "))
    for i in range(n):
        print("\nCourse ", i + 1)
        c_id = input("Enter course ID: ")
        c_name = input("Enter course name: ")
        course.append({"id": c_id, "name": c_name})
    return course

def input_marks(students, courses):
    marks = {}
    for course in courses:
        c_id = course["id"]
        print("\nEnter marks for course " + course["name"] + " (ID: " + course["id"] + "): ")
        
        marks[c_id] = {}
        for student in students:
            s_id = student["id"]
            mark = float(input("Enter mark for " + student["name"] + " (ID: " + student["id"] + ")"))
            marks[c_id][s_id] = mark
    return marks

def list_students(students):
    print("\nSTUDENTS")
    for student in students:
        print("ID: " + student["id"] + " | Name: " + student["name"] + " | DoB: " + student["dob"])

def list_courses(courses):
    print("\nCOURSES")
    for course in courses:
        print("ID: " + course["id"] + " | Name: " + course["name"])

def show_marks_for_course(students, courses, marks):
    c_id = input("\nEnter course ID to show marks: ")
    if c_id not in marks:
        print("Course ID not found!")
        return

    print("\n STUDENT MARKS FOR " + courses["id"])
    for student in students:
        s_id = student["id"]
        if s_id in marks[c_id]:
            print(student["id"] + " - " + student["name"] + " : " + marks[c_id][s_id])

students = students()
courses = courses()
marks = input_marks(students, courses)

list_students(students)
list_courses(courses)
show_marks_for_course(students, courses, marks)