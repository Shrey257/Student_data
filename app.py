import sqlite3

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    student_data = query_attendance_report()
    return render_template('home.html', student_data=student_data)

def query_attendance_report():
    connie=sqlite3.connect('students.db')
    c=connie.cursor()
    c.execute('''SELECT * FROM attendance_report''')
    student_data=c.fetchall()
    return student_data

if __name__ == '__main__':
    app.run()
