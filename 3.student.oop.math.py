import math
import numpy as np

class Student:
    def __init__(self, s_id, name, DoB):
        self.id = s_id
        self.name = name
        self.dob = DoB
        self.gpa = 0.0

class Course:
    def __init__(self, c_id, c_name, credits):
        self.id = c_id
        self.name = c_name
        self.credits = credits

def input_students():
    student = []
    n = int(input("Enter number of students: "))
    for i in range(n):
        print("\n Student ", i + 1)
        s_id = input("Enter student ID: ")
        name = input("Enter student name: ")
        DoB = input("Enter date of birth: ")
        student.append(Student(s_id, name, DoB))
    return student

def input_courses():
    course = []
    n = int(input("Enter number of courses: "))
    for i in range(n):
        print("\n Course ", i + 1)
        c_id = input("Enter course ID: ")
        c_name = input("Enter course name: ")
        credits = int(input("Enter number of credits: "))
        course.append(Course(c_id,c_name, credits))
    return course

def input_marks(student, course):
    marks = {}  
    for c in course:
        print("\nEnter course mark for " + course["name"] + "(ID: " + course["id"] + ")")
        marks[course.id] = {}
        for s in students:
            raw_mark = float(input("Enter mark for " + student.name + "(ID: " + student.id + ")"))
        
            rounded_mark = math.floor(raw_mark * 10) / 10.0
            marks[course.id][student.id] = rounded_mark
    return marks

def calculate_gpa(student, course, marks):
    for student in students:
        student_marks = []
        credits_list = []

        for course in courses:
            if course.id in marks and student.id in marks[course.id]:
                student_marks.append(marks[course.id][student.id])
                credits_list.append(course.credits)

        if student_marks:
            np_marks = np.array(student_marks)
            np_credits = np.array(credits_list)

            weighted_sum = np.sum(np_marks * np_credits)
            total_credits = np.sum(np_credits)
            student.gpa = weighted_sum / total_credits

def sort_students_by_gpa(students):
    gpas = np.array([student.gpa for student in students])
    sorted_indices = np.argsort(-gpas)
    return [students[i] for i in sorted_indices]

def list_students(student):
    print("\nStudent list (Decreasing GPA)")
    for student in students:
        print(f"ID: {student.id:<8} | Name: {student.name:<18} | DoB: {student.dob:<10} | GPA: {student.gpa:.2f}")

def list_courses(course):
    print("\nCourse list")
    for course in courses:
        print(f"ID: {course.id:<8} | Name: {course.name:<20} | Credits: {course.credits}")


def show_marks_for_course(course, marks):
    c_id = input("\nEnter course ID: ")
    if c_id not in marks:
        print("Course ID not found!")
        return

    print(f"\nCourse mark table {c_id}")
    for s_id, mark in marks[c_id].items():
        print(f"Student ID: {s_id} | Mark: {mark}")

def main():
    student = input_students()
    course = input_courses()
    marks = input_marks(student, course)

    calculate_gpa(student, course, marks)
    sorted_students = sort_students_by_gpa(student)

    list_students(sorted_students)
    list_courses(course)
    show_marks_for_course(course, marks)
    
main()
