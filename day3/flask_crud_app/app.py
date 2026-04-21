from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS items (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        description TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items ORDER BY created_at DESC').fetchall()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        if not name:
            flash('Name is required!')
            return redirect(url_for('add'))

        conn = get_db_connection()
        conn.execute('INSERT INTO items (name, description) VALUES (?, ?)',
                    (name, description))
        conn.commit()
        conn.close()

        flash('Item added successfully!')
        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit(id):
    conn = get_db_connection()
    item = conn.execute('SELECT * FROM items WHERE id = ?', (id,)).fetchone()

    if item is None:
        conn.close()
        flash('Item not found!')
        return redirect(url_for('index'))

    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']

        if not name:
            flash('Name is required!')
            return redirect(url_for('edit', id=id))

        conn.execute('UPDATE items SET name = ?, description = ? WHERE id = ?',
                    (name, description, id))
        conn.commit()
        conn.close()

        flash('Item updated successfully!')
        return redirect(url_for('index'))

    conn.close()
    return render_template('edit.html', item=item)

@app.route('/delete/<int:id>', methods=['POST'])
def delete(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM items WHERE id = ?', (id,))
    conn.commit()
    conn.close()

    flash('Item deleted successfully!')
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)