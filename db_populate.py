import sqlite3

db_locale='students.db'
connie = sqlite3.connect(db_locale)

c = connie.cursor()
c.execute("""
INSERT INTO attendance_report(month,student_name,present,absent) VALUES 
('Jan','Raj Modi',20,2),
('Jan','Arnav Khanna',22,0)
""")

connie.commit()
connie.close()
