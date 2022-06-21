# db 연동
import sqlite3
from datetime import datetime

# print(sqlite3.version)
# print(sqlite3.sqlite_version)

# # 남짜 생성
now = datetime.now()
# print("now", now)
now_date_time = now.strftime("%Y-%m-%d %H:%M:%S")
# print("now_date_time", now_date_time)

conn = sqlite3.connect("data/database.db", isolation_level=None)

# 커서
cursor = conn.cursor()  # <class 'sqlite3.Cursor'>
print(type(cursor))

# 테이블 생성
cursor.execute(
    "CREATE TABLE IF NOT EXISTS user(id integer primary key,username text, phon text,website text,regdate text)"
)

# insert
# cursor.execute(
#     "INSERT INTO user VALUES(1,'KIM','010-1234-1234','kim.com',?)", (now_date_time,)
# )


# cursor.execute(
#     "INSERT INTO user VALUES(?,?,?,?,?)",
#     (
#         2,
#         "hong",
#         "010-1234-4567",
#         "hong.com",
#         now_date_time,
#     ),
# )

# 여러개 삽입
user_list = (
    (3, "park", "010-4567-1234", "park.com", now_date_time),
    (4, "choi", "010-9876-1234", "choi.com", now_date_time),
    (5, "yoo", "010-3687-1234", "yoo.com", now_date_time),
)

cursor.executemany("INSERT INTO user VALUES(?,?,?,?,?)", user_list)
