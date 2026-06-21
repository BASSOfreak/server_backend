import sqlite3
import sys
username = None
if len(sys.argv)> 1:
    username = sys.argv[1]
with sqlite3.connect("user_db/user_db.db") as connection:
    cur = connection.cursor()
    if not username:
        print("show all data")
        res = cur.execute("""
            SELECT * FROM users;
        """)
        print(res.fetchall())
        sys.exit()

    res = cur.execute("""
        SELECT username, password FROM users WHERE username = ?;
    """, [username])
    row = res.fetchone()
    if row is None:
        sys.exit()
    found_username, password_hashed = row
    print(f"requested user: {username}\n"
        +f"found user: {found_username}, hash:{password_hashed}")
