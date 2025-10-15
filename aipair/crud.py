# CRUD operations for COURSES table in SQLite (college.db)
import sqlite3

DB_PATH = '../college.db'  # Adjust path if needed

def create_table():
    """
    Creates the COURSES table in the database if it does not already exist.

    The table includes the following columns:
        - id: INTEGER, primary key, auto-incremented
        - title: TEXT, not null
        - duration: TEXT, not null
        - fee: REAL, not null

    Uses the global DB_PATH for the database connection.
    """
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS COURSES (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                duration TEXT NOT NULL,
                fee REAL NOT NULL
            )
        ''')
        conn.commit()

def add_course(title, duration, fee):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('INSERT INTO COURSES (title, duration, fee) VALUES (?, ?, ?)', (title, duration, fee))
        conn.commit()
        return c.lastrowid

def get_course(course_id):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM COURSES WHERE id = ?', (course_id,))
        return c.fetchone()

def get_all_courses():
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM COURSES')
        return c.fetchall()

def update_course(course_id, title, duration, fee):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('UPDATE COURSES SET title = ?, duration = ?, fee = ? WHERE id = ?', (title, duration, fee, course_id))
        conn.commit()
        return c.rowcount

def delete_course(course_id):
    with sqlite3.connect(DB_PATH) as conn:
        c = conn.cursor()
        c.execute('DELETE FROM COURSES WHERE id = ?', (course_id,))
        conn.commit()
        return c.rowcount