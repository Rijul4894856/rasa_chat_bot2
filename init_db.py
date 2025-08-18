import sqlite3
import bcrypt

# Connect to or create the database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL,
    token TEXT,
    last_access TEXT
)
''')

# Hash the password securely with bcrypt
password = "secure_password123"
hashed_pw = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

# Insert the user
cursor.execute('''
INSERT OR IGNORE INTO users (username, password_hash)
VALUES (?, ?)
''', ("rijul_user", hashed_pw))

conn.commit()
conn.close()

print("✅ Secure user inserted with bcrypt hashing.")
