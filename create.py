import sqlite3

conn = sqlite3.connect('demo2.db')
cursor = conn.cursor()

# 创建一个表
cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
                    Name TEXT PRIMARY KEY,
                    ImageUrl TEXT,
                     Position TEXT,
                      Birthday TEXT,
                      URL TEXT
                 )''')



cursor.execute(f"INSERT INTO Employees VALUES ('测试名字', 'image/测试图片.png', '[测试员, 超级测试员]',  '2023-11-25', '{zifu_json}')")

conn.commit()

cursor.close()

# cursor.execute(f'''SELECT Name, ImageUrl FROM Employees WHERE Name = '测试名字' ;''')
# print(cursor.fetchone())
# # cursor.execute(f'''SELECT Name, ImageUrl FROM Employees WHERE NAME = ;''')
# cursor.execute("""SELECT * FROM Employees""")
# print(cursor.fetchone())
