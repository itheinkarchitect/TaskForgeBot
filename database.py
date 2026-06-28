
import sqlite3





def add_task(user_id, task):
    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO tasks(user_id, task) VALUES(?, ?)",
        (user_id, task)
    )

    conn.commit()
    conn.close()

def create_table():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        task TEXT NOT NULL
)
""")


    conn.commit()
    conn.close()

    print("TABLE CREATED")

def get_tasks(user_id):

    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        "SELECT task FROM tasks WHERE user_id = ?",
        (user_id,)
    )

    tasks = cursor.fetchall()

    conn.close()

    return tasks

def delete_task(id, user_id):
    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM tasks
        WHERE id = ? AND user_id = ?
        """,
        (id, user_id)
    )

    conn.commit()
    conn.close()

def complete_task(id, user_id):
    conn = sqlite3.connect("database.db")

    cursor = conn.cursor()

    cursor.execute(
         """
        DELETE FROM tasks
        WHERE id = ? AND user_id = ?
        """,
        (id, user_id)
   )

    conn.commit()
    conn.close()