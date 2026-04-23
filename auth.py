def login_or_register(cursor, conn, username, password):
    cursor.execute("SELECT * FROM users WHERE username=%s", (username,))
    user = cursor.fetchone()

    if user:
        if user['password'] == password:
            return True, "login"
        else:
            return False, "wrong_password"
    else:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (%s, %s)",
            (username, password)
        )
        conn.commit()
        return True, "registered"