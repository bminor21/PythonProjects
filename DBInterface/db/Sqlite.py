import sqlite3

from .DbBase import DbBase

class Sqlite(DbBase):

    dbName = "lite.db"
    
    def __init__(self):
        print("Created sqlite db object")

    def executeStatement(self, statement):
        conn = sqlite3.connect(self.dbName)
        cursor = conn.cursor()
        cursor.execute(statement)
        conn.commit()
        conn.close()
