import mysql.connector


class MysqlRepository:

    def __init__(self):
        config = {
            'user': 'root',
            'password': 'root',
            'host': 'localhost',
            'port': '32000',
            'database': 'etymological'
        }
        self.connection = mysql.connector.connect(**config)
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def commit_changes(self):
        self.connection.commit()
