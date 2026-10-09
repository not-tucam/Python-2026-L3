import math
from domains import Student, Course

def input_students():
    students = []
    n = int(input("Enter number of students: "))
    for i in range(n):
        print(f"\n--- Student {i + 1} ---")
        s_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        dob = input("Enter date of birth: ")
        students.append(Student(s_id, name, dob))
    return students

def input_courses():
    courses = []
    n = int(input("Enter number of courses: "))
    for i in range(n):
        print(f"\n--- Course {i + 1} ---")
        c_id = input("Enter course ID: ")
        c_name = input("Enter course name: ")
        credits = int(input("Enter number of credits: "))
        courses.append(Course(c_id, c_name, credits))
    return courses

def input_marks(students, courses):
    marks = {}
    for c in courses:
        print(f"\n--- Entering Marks for Course: {c.name} (ID: {c.id}) ---")
        marks[c.id] = {}
        for s in students:
            raw_mark = float(input(f"Enter mark for {s.name} (ID: {s.id}): "))
            # Round down to 1 decimal place using math.floor
            rounded_mark = math.floor(raw_mark * 10) / 10.0
            marks[c.id][s.id] = rounded_mark
    return marks