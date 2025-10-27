def select(cursor, query: str):
    cursor.execute(query)
    return cursor.fetchall()
