def create_tables(cursor):
    cursor.execute(
        """
    DROP TABLE IF EXISTS tasks;
    DROP TABLE IF EXISTS status;
    DROP TABLE IF EXISTS users;
                
    CREATE TABLE users (
        id SERIAL PRIMARY KEY ,
        fullname VARCHAR(100) NOT NULL,
        email VARCHAR(100) NOT NULL UNIQUE
                );
    CREATE TABLE status (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50) NOT NULL UNIQUE
                );
    CREATE TABLE tasks (
        id SERIAL PRIMARY KEY,
        title VARCHAR(200) NOT NULL,
        description TEXT,
        status_id INTEGER REFERENCES status(id),
        user_id INTEGER REFERENCES users(id) ON DELETE CASCADE
        );     
    """
    )
    print("Tables created successfully.\n")
