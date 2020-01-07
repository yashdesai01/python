import mysql.connector
class Mconnection:
    def __init__(self):pass
    def getCursor(self):
        self.conn=mysql.connector.connect(host='localhost',database='world',user='root',password='')
        self.cursor=self.conn.cursor()
        return self.cursor
    def close(self):
        self.conn.close()
        self.cursor.close()
    def rollback(self):
        self.conn.rollback()
    def commit(self):
        self.conn.commit()
