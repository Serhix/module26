import sqlite3
from contextlib import contextmanager

@contextmanager
def create_conection(db_file: str):
    '''create a database conection to a SQLite'''
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        yield conn
        conn.rollback()
    except sqlite3.DatabaseError as err:
        print(err)
    finally:
        if conn  is not None:
            conn.close()

class CreateConnection:

    def __init__(self, file: str) -> None:
        self.file = file

    def __enter__(self):
        self.connect = sqlite3.connect(self.file)
        return self.connect
    
    def __exit__(self, exc_type, ext_val, exc_tb):
        self.connect.commit()
        self.connect.close()

