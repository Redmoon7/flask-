import pathlib
import sqlite3

""" 数据库类 """


class Data:

    def __init__(self):
        path = pathlib.Path(r'data\demo2.db').absolute()
        self.conn = sqlite3.connect(path)
        # 连接到数据库（如果不存在则创建）
        self.cursor = self.conn.cursor()
        # 创建一个游标对象

    def ADD(self, Name, ImageUrl, Position, Birthday, URL):
        self.cursor.execute(
            f"INSERT INTO Employees VALUES ('{Name}', '{ImageUrl}', '{Position}',  '{Birthday}', '{URL}')")

        self.conn.commit()

        self.cursor.close()

    def CheckImage(self, Name):
        self.cursor.execute(f'''SELECT Name, ImageUrl FROM Employees WHERE Name = '{Name}' ;''')

        return self.cursor.fetchone()

    def CheckAll(self, Name):
        self.cursor.execute(f'''SELECT * FROM Employees WHERE Name = '{Name}' ;''')

        return self.cursor.fetchone()


#
# print(pathlib.Path)
#
# print(pathlib.Path(r'data\data.db').absolute())

print(Data().CheckAll(Name='测试名字'))
