import sqlite3

conn = sqlite3.connect("data/database.db", isolation_level=None)

cursor = conn.cursor()

# 조회
sql = """select*
from user
"""
cursor.execute(sql)

# fetchone(), fetchmany(), fethcall()
# print("1", cursor.fetchone())  # select 결과로 나온 제일 첫번째 행

# print("3", cursor.fetchmany(size=3))

# print("3", cursor.fetchall())

# for row in cursor.fetchall():
#     print("rows", row)

# sql = """select*
# from user order by id desc
# """
# cursor.execute(sql)

# for row in cursor.fetchall():
#     print("rows", row)

# sql = """select*
# from user id = ?
# """
# cursor.execute(sql, (3,))

# for row in cursor.fetchall():
#     print("rows", row)

# sql = """select*
# from user where id = %s
# """

# param = 4
# cursor.execute(sql % param)

# for row in cursor.fetchall():
#     print("rows", row)

# sql = """select*
# from user where id = :id
# """

# cursor.execute(sql, {"id": 5})

# for row in cursor.fetchall():
#     print("rows", row)

sql = """select*
from user where id in (?,?)
"""

param = (3, 6)
cursor.execute(sql, param)

for row in cursor.fetchall():
    print("rows", row)
