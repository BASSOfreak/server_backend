import sys
import sqlite3
from pwdlib import PasswordHash
password_hash = PasswordHash.recommended()
print(sys.argv)
username = sys.argv[1]
password = sys.argv[2]
hashed_password = password_hash.hash(password)
with sqlite3.connect("user_db/user_db.db") as connection:
    cur = connection.cursor()
    cur.execute(
        """CREATE TABLE IF NOT EXISTS users (
            username TEXT PRIMARY KEY,
            password TEXT NOT NULL
        );
    """)
    cur.execute(f"""
        INSERT INTO users (username, password)
        VALUES ('{username}', '{hashed_password}');
    """)
    connection.commit()
