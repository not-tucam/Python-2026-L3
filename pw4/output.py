import curses

def display_students(stdscr, students):
    stdscr.clear()
    stdscr.addstr(0, 0, "=== STUDENT LIST (Decreasing GPA) ===", curses.A_BOLD)
    stdscr.addstr(2, 0, f"{'ID':<10} | {'Name':<20} | {'DoB':<12} | {'GPA':<5}")
    stdscr.addstr(3, 0, "-" * 55)
    
    for idx, s in enumerate(students, start=4):
        stdscr.addstr(idx, 0, f"{s.id:<10} | {s.name:<20} | {s.dob:<12} | {s.gpa:.2f}")
    
    stdscr.addstr(len(students) + 6, 0, "Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()

def display_courses(stdscr, courses):
    stdscr.clear()
    stdscr.addstr(0, 0, "=== COURSE LIST ===", curses.A_BOLD)
    stdscr.addstr(2, 0, f"{'ID':<10} | {'Course Name':<25} | {'Credits':<8}")
    stdscr.addstr(3, 0, "-" * 50)
    
    for idx, c in enumerate(courses, start=4):
        stdscr.addstr(idx, 0, f"{c.id:<10} | {c.name:<25} | {c.credits:<8}")
    
    stdscr.addstr(len(courses) + 6, 0, "Press any key to continue...")
    stdscr.refresh()
    stdscr.getch()

def display_marks(stdscr, course, marks):
    stdscr.clear()
    c_id = course.id
    stdscr.addstr(0, 0, f"=== MARK TABLE FOR COURSE: {course.name} ({c_id}) ===", curses.A_BOLD)
    stdscr.addstr(2, 0, f"{'Student ID':<15} | {'Mark':<8}")
    stdscr.addstr(3, 0, "-" * 30)
    
    if c_id in marks:
        row = 4
        for s_id, mark in marks[c_id].items():
            stdscr.addstr(row, 0, f"{s_id:<15} | {mark:<8.1f}")
            row += 1
        stdscr.addstr(row + 2, 0, "Press any key to continue...")
    else:
        stdscr.addstr(4, 0, "No marks recorded for this course.")
        stdscr.addstr(6, 0, "Press any key to continue...")
        
    stdscr.refresh()
    stdscr.getch()