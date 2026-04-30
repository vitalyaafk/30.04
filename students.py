import sqlite3

connection = sqlite3.connect("something.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL,age INTEGER,major TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS courses (course_id INTEGER PRIMARY KEY AUTOINCREMENT,course_name TEXT NOT NULL,instructor TEXT)""")
cursor.execute("""CREATE TABLE IF NOT EXISTS student_courses (student_id INTEGER,course_id INTEGER,FOREIGN KEY (student_id) REFERENCES students(id),FOREIGN KEY (course_id) REFERENCES courses(course_id))""")
connection.commit()


def add_student():
    name = input("Введи ім'я студента: ")
    age = input("Введи вік студента: ")
    major = input("Введи спеціальність студента: ")
    cursor.execute("INSERT INTO students (name, age, major) VALUES (?, ?, ?)",(name, age, major),)
    connection.commit()
    print(f"Студент {name} доданий успішно")
def add_course():
    course_name = input("Введи назву курсу: ")
    instructor = input("Введи ім'я викладача: ")
    cursor.execute("INSERT INTO courses (course_name, instructor) VALUES (?, ?)",(course_name, instructor),)
    connection.commit()
    print(f"Курс {course_name} від {instructor} доданий успішно")
def enroll_student():
    student_id = input("Введи ID студента: ")
    course_id = input("Введи ID курсу: ")
    cursor.execute("INSERT INTO student_courses (student_id, course_id) VALUES (?, ?)",(student_id, course_id),)
    connection.commit()
    print(f"Студент {student_id} записаний на курс {course_id} успішно")
def get_students():
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()
def get_courses():
    cursor.execute("SELECT * FROM courses")
    return cursor.fetchall()
def update_student():
    student_id = input("Введи ID студента для зміни: ")
    name = input("Нове ім'я: ")
    age = input("Новий вік: ")
    major = input("Нова спеціальність: ")
    cursor.execute("UPDATE students SET name = ?, age = ?, major = ? WHERE id = ?",(name, age, major, student_id),)
    connection.commit()
def update_course():
    course_id = input("Введи ID курсу для зміни: ")
    course_name = input("Нова назва курсу: ")
    instructor = input("Нове ім'я викладача: ")
    cursor.execute("UPDATE courses SET course_name = ?, instructor = ? WHERE course_id = ?",(course_name, instructor, course_id),)
    connection.commit()
    print(f"Курс {course_name} від {instructor} змінений успішно")
def delete_student():
    student_id = input("Введи ID студента для видалення: ")
    cursor.execute("DELETE FROM students WHERE id = ?",(student_id),)
    connection.commit()
    print(f"Студент {student_id} видалений успішно")
def delete_course():
    course_id = input("Введи ID курсу для видалення: ")
    cursor.execute("DELETE FROM courses WHERE course_id = ?",(course_id),)
    connection.commit()
    print(f"Курс {course_id} видалений успішно")