def sql_reader(file: str) -> str:   
    with open(file, 'r') as f:
        sql = f.read()
    return sql