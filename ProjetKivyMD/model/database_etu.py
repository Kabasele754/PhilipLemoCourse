import sqlite3

class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS Student (id INTEGER PRIMARY KEY, name text, lastname text, firstname text, age text)")
        self.conn.commit()

    def fetch_all(self):
        self.cur.execute("SELECT * FROM Student")
        rows = self.cur.fetchall()
        return rows

    def get_record_by_id(self, id):
        self.cur.execute("SELECT * FROM Student WHERE id=?", (id,))
        row = self.cur.fetchone()
        return row

    def insert(self, name, lastname, firstname, age):
        self.cur.execute("INSERT INTO Student VALUES (NULL, ?, ?, ?, ?)", (name, lastname, firstname, age))
        self.conn.commit()

    def delete(self, id):
        self.cur.execute("DELETE FROM Student where id=?", (id,))
        self.conn.commit()

    def update(self, id, name, lastname, firstname, age):
        self.cur.execute("UPDATE Student SET matter=?, filename=?, description=?, location=? WHERE id=?", (name, lastname, firstname, age, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()