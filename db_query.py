import sqlite3

db_locale='students.db'
connie = sqlite3.connect(db_locale)

c = connie.cursor()
c.execute("""
SELECT * FROM attendance_report
""")

students_info = c.fetchall()
for students in students_info:
    print(students)

connie.commit()
connie.close()
