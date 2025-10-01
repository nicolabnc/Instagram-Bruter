class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = self.connect()

    def connect(self):
        import sqlite3
        connection = sqlite3.connect(self.db_path)
        return connection

    def create_table(self):
        with self.connection:
            self.connection.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    username TEXT NOT NULL,
                    password TEXT NOT NULL
                )
            ''')

    def insert_user(self, username, password):
        with self.connection:
            self.connection.execute('''
                INSERT INTO users (username, password) VALUES (?, ?)
            ''', (username, password))

    def fetch_users(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM users')
        return cursor.fetchall()

    def close(self):
        self.connection.close()