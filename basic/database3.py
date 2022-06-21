import sqlite3

conn = sqlite3.connect("data/database.db")
cursor = conn.cursor()

# 수정
# id가 2번인 user 이름을 cho로 변경

# sql = """update user
# set username = ? where id = ?
# """
# cursor.execute(sql, ("cho", 2))
# conn.commit()

# sql = """update user
# set username = :username where id = :id
# """
# cursor.execute(sql, {"username": "hong", "id": 2})
# conn.commit()

# sql = """update user
# set username = '%s' where id= '%s'
# """
# cursor.execute(sql % ("cho", 2))
# conn.commit()

# delete
cursor.execute("delete from user where id=?", (2,))
cursor.execute("delete from user where id=:id", {"id": 3})
cursor.execute("delete from user where id=%d" % 4)

conn.commit()
