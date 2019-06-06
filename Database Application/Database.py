import sqlite3


class Database:
    con = None
    cur = None

    def __init__(self, db_name):
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY AUTOINCREMENT, \
                                              title text, author text, year integer, isbn integer)")
        self.con.commit()

    def __del__(self):
        self.con.close()

    def fetchall(self) -> list:
        self.cur.execute("SELECT * from book")
        res = self.cur.fetchall()
        return res

    def insert(self, title, author, year, isbn) -> None:
        self.cur.execute("INSERT into book (title, author, year, isbn) values (?,?,?,?)", (title, author, year, isbn))
        self.con.commit()

    def update(self, item, title, author, year, isbn) -> None:
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",
                         (title, author, year, isbn, item))
        self.con.commit()

    def delete(self, item) -> None:
        self.cur.execute("DELETE FROM book WHERE id=?", (item,))
        self.con.commit()

    def search(self, title="", author="", year="", isbn="") -> list:
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? or year=? or isbn=?",
                         (title, author, year, isbn))
        res = self.cur.fetchall()
        return res
