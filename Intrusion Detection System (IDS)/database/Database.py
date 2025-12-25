import sqlite3
import os
print("Current Working Directory:", os.getcwd())


def createDabase():
    global conn, cursor
    cwd = os.getcwd()
    database_path = os.path.join(cwd, 'database', 'db.db')
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        username TEXT,
        email TEXT,
        password TEXT,
        mobile TEXT
    )''')
    conn.commit()
    conn.close()
    print("Database Created")

def InsertData(name, email, password, mobile):
    cwd = os.getcwd()
    database_path = os.path.join(cwd, 'database', 'db.db')
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (username, email, password, mobile) VALUES (?, ?, ?, ?)",
                   (name, email, password, mobile))
    conn.commit()
    conn.close()
    print("Inserted Data")

def read_cred(email, password):
    cwd = os.getcwd()
    database_path = os.path.join(cwd, 'database', 'db.db')
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()
    cursor.execute("SELECT username, email, password, mobile FROM users WHERE email=? AND password=?",
                   (email, password))
    fetch = cursor.fetchone()
    conn.close()
    print(fetch)
    return fetch
