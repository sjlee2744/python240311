# db1.py

import sqlite3

# con = sqlite3.connect(":memory:")

con = sqlite3.connect("c:\\work\\demo.db")

cur = con.cursor()

cur.execute("create table if not exists PhoneBook (name test, phoneNum text);")

cur.execute("insert into PhoneBook values ('홍길동', '010-222');")

# 입력 파라메터 처리
name = "박문수"
phoneNum = "010-123"

cur.execute("insert into PhoneBook values (?, ?);", (name, phoneNum))

# 여러건 입력
datalist = (("tom", "010-333"), ("dsp", "010-567"))
cur.executemany("insert into PhoneBook values (?, ?);", datalist)

cur.execute("select * from PhoneBook;")
for row in cur:
    print(row)


