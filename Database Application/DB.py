import sqlite3


class DB:

    dbName = "book"

    def __init__(self, dbName):
        self.dbName = dbName
        con = self.get_connection()
        cur = con.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY AUTOINCREMENT, title text, author text, year integer, isbn integer)")
        con.commit()
        con.close()

    def get_connection(self) -> sqlite3.Connection:
        return sqlite3.connect(self.dbName)

    def fetchall(self) -> list:
        con = self.get_connection()
        cur = con.cursor()
        cur.execute("SELECT * from book")
        rs = cur.fetchall()
        con.close()
        return rs

    def insert(self,title, author, year, isbn) -> None:
        con = self.get_connection()
        cur = con.cursor()
        cur.execute("INSERT into book (title, author, year, isbn) values (?,?,?,?)", (title, author, year, isbn))
        con.commit()
        con.close()

    def update(self,id,title,author,year,isbn) -> None:
        con = self.get_connection()
        cur = con.cursor()
        cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
        con.commit()
        con.close()

    def delete(self,id) -> None:
        con = self.get_connection()
        cur = con.cursor()
        cur.execute("DELETE FROM book WHERE id=?",(id,))
        con.commit()
        con.close()

    def search(self,title="", author="", year="", isbn="") -> list:
        con = self.get_connection()
        cur = con.cursor()
        cur.execute("SELECT * FROM book WHERE title=? OR author=? or year=? or isbn=?",(title, author,year,isbn))
        rs = cur.fetchall()
        con.close()
        return rs