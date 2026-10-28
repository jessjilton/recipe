import sqlite3
from auth_utils import hash_password, verify_password

DB_PATH = "recipes.db"  # change this if your DB file has a different name

def main():
    # 1) Connect to the database
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()

    username = "test_user"
    email = "test_user@example.com"
    plain_password = "test123"

    # 2) Hash the password
    pw_hash = hash_password(plain_password)
    print("Generated hash for storage:", pw_hash)

    # 3) Insert or replace the test user
    cur.execute(
        """
        INSERT INTO users (username, email, password_hash)
        VALUES (?, ?, ?)
        ON CONFLICT(username) DO UPDATE SET
            email = excluded.email,
            password_hash = excluded.password_hash
        """,
        (username, email, pw_hash),
    )
    conn.commit()

    # 4) Read the stored hash back
    cur.execute("SELECT password_hash FROM users WHERE username = ?", (username,))
    row = cur.fetchone()
    stored_hash = row[0]
    print("Stored hash from DB:", stored_hash)

    # 5) Verify correct and incorrect passwords
    print("Correct password check:", verify_password(stored_hash, "test123"))
    print("Wrong password check:", verify_password(stored_hash, "wrongpass"))

    conn.close()


if __name__ == "__main__":
    main()