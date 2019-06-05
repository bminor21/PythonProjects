import sqlite3


class DB:

    @staticmethod
    def get_connection() -> sqlite3.Connection:
        return sqlite3.connect("books")

    def __init__(self) -> None:
        con = DB.get_connection()
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INT PRIMARY KEY, title text, author text, year integer, isbn integer)")
        con.commit()
        con.close()

    def fetchall(self) -> list:
        con = DB.get_connection()
        cur = con.cursor()
        cur.execute("SELECT * from book")
        rs = cur.fetchall()
        con.close()
        return rs

    def insert(self, title, author, year, isbn) -> None:
        con = DB.get_connection()
        cur = con.cursor()
        cur.execute("INSERT into book values(NULL,?,?,?,?)", (title, author, year, isbn))
        con.commit()
        con.close()

    def update(self, id,title,author,year,isbn) -> None:
        con = DB.get_connection()
        cur = con.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        con.commit()
        con.close()

    def delete(self,id) -> None:
        con = DB.get_connection()
        cur = con.cursor()
        cur.execute("DELETE FROM book WHERE id=?",(id,))
        con.commit()
        con.close()

    def search(self, title="", author="", year="", isbn="") -> list:
        con = DB.get_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? or year=? or isbn=?",(title, author,year,isbn))
        rs = cur.fetchall()
        con.close()
        return rs