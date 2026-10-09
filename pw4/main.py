import curses
import numpy as np

from domains import Student, Course
import input as in_mod
import output as out_mod

def calculate_gpa(students, courses, marks):
    for s in students:
        s_marks = []
        c_credits = []
        for c in courses:
            if c.id in marks and s.id in marks[c.id]:
                s_marks.append(marks[c.id][s.id])
                c_credits.append(c.credits)
        
        if s_marks:
            np_marks = np.array(s_marks)
            np_credits = np.array(c_credits)
            weighted_sum = np.sum(np_marks * np_credits)
            total_credits = np.sum(np_credits)
            s.gpa = weighted_sum / total_credits if total_credits > 0 else 0.0

def sort_students_by_gpa(students):
    gpas = np.array([s.gpa for s in students])
    sorted_indices = np.argsort(-gpas)
    return [students[i] for i in sorted_indices]

def main(stdscr):
    # Command-line data entry
    curses.endwin()
    
    print("=== STUDENT & COURSE MANAGEMENT SYSTEM ===")
    students = in_mod.input_students()
    courses = in_mod.input_courses()
    marks = in_mod.input_marks(students, courses)
    
    # Calculate GPAs and sort
    calculate_gpa(students, courses, marks)
    sorted_students = sort_students_by_gpa(students)
    
    # Display output using Curses screen interface
    stdscr.clear()
    out_mod.display_students(stdscr, sorted_students)
    out_mod.display_courses(stdscr, courses)
    
    for course in courses:
        out_mod.display_marks(stdscr, course, marks)

if __name__ == "__main__":
    curses.wrapper(main)