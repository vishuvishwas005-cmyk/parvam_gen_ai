from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'student-crud-secret-key'

def get_db_connection():
    conn = sqlite3.connect('students.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS students (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        age INTEGER,
                        grade TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    students = conn.execute('SELECT * FROM students ORDER BY name').fetchall()
    conn.close()
    return render_template('index.html', students=students)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        grade = request.form['grade']

        if not name or not email:
            flash('Name and email are required!')
            return redirect(url_for('add'))

        try:
            conn = get_db_connection()
            conn.execute('INSERT INTO students (name, email, age, grade) VALUES (?, ?, ?, ?)',
                        (name, email, age, grade))
            conn.commit()
            conn.close()
            flash('Student added successfully!')
            return redirect(url_for('index'))
        except sqlite3.IntegrityError:
            flash('Email already exists!')
            return redirect(url_for('add'))

    return render_template('form.html', action='Add', student=None)

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    student = conn.execute('SELECT * FROM students WHERE id = ?', (id,)).fetchone()
    conn.close()

    if student is None:
        flash('Student not found!')
        return redirect(url_for('index'))

    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        age = request.form['age']
        grade = request.form['grade']

        if not name or not email:
            flash('Name and email are required!')
            return redirect(url_for('edit', id=id))

        try:
            conn = get_db_connection()
            conn.execute('UPDATE students SET name = ?, email = ?, age = ?, grade = ? WHERE id = ?',
                        (name, email, age, grade, id))
            conn.commit()
            conn.close()
            flash('Student updated successfully!')
            return redirect(url_for('index'))
        except sqlite3.IntegrityError:
            flash('Email already exists!')
            return redirect(url_for('edit', id=id))

    return render_template('form.html', action='Edit', student=student)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Student deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)