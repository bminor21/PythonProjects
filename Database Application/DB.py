import sqlite3


def get_connection() -> sqlite3.Connection:
    return sqlite3.connect("books")


def connect() -> None:
    con = get_connection()
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS book (id INT PRIMARY KEY, title text, author text, year integer, isbn integer)")
    con.commit()
    con.close()


def fetchall() -> list:
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * from book")
    rs = cur.fetchall()
    con.close()
    return rs


def insert(title, author, year, isbn) -> None:
    con = get_connection()
    cur = con.cursor()
    cur.execute("INSERT into book values(NULL,?,?,?,?)", (title, author, year, isbn))
    con.commit()
    con.close()


def update(id,title,author,year,isbn) -> None:
    con = get_connection()
    cur = con.cursor()
    cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?",(title,author,year,isbn,id))
    con.commit()
    con.close()


def delete(id) -> None:
    con = get_connection()
    cur = con.cursor()
    cur.execute("DELETE FROM book WHERE id=?",(id,))
    con.commit()
    con.close()


def search(title="", author="", year="", isbn="") -> list:
    con = get_connection()
    cur = con.cursor()
    cur.execute("SELECT * FROM book WHERE title=? OR author=? or year=? or isbn=?",(title, author,year,isbn))
    rs = cur.fetchall()
    con.close()
    return rs

connect()