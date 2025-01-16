import sqlite3

db_locale='students.db'
connie = sqlite3.connect(db_locale)

c = connie.cursor()
c.execute("""
CREATE TABLE attendance_report (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    month TEXT,
    student_name TEXT ,
    present integer ,
    absent integer 
)
""")

connie.commit()
connie.close()
