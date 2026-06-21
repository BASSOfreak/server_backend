import sys
import sqlite3
print(sys.argv)
username = sys.argv[1]
with sqlite3.connect("user_db/user_db.db") as connection:
    cur = connection.cursor()
    cur.execute(f"""
        DELETE FROM users 
        WHERE username = ?;
    """, [username])
    connection.commit()