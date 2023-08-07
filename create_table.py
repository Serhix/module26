from conect import create_conection
from read_sql import sql_reader

DATABASE = 'database_m26.db'

create_sql = 'sql/create_table.sql'

def create_db():
    with create_conection(DATABASE) as conn:
        cur = conn.cursor()
        cur.executescript(sql_reader(create_sql))

if __name__ == '__main__':
    create_db()