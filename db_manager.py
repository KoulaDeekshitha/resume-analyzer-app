import sqlite3

def create_db():
    conn = sqlite3.connect('database/resumes.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS resumes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            text TEXT,
            keywords TEXT
        )
    ''')
    conn.commit()
    conn.close()

def insert_resume(name, text, keywords):
    conn = sqlite3.connect('database/resumes.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO resumes (name, text, keywords) VALUES (?, ?, ?)
    ''', (name, text, ",".join(keywords)))
    conn.commit()
    conn.close()
