# This will interact with the Database Object

from .Psql import Psql
from .Sqlite import Sqlite

class Dao():
    database = None

    def __init__(self, db_type):
        print("Init: " + db_type)
        if db_type == 'sqlite':
            self.database = Sqlite()
        else:
            self.database = Psql()

    def query(self,statement):
        if self.database is not None:
            self.database.executeStatement(statement)
