import sqlite3 as sql
db = sql.connect("DB\IK.sqlite")
cur = db.cursor()
cur.execute("SELECT  count(DISTINCT departman_id)  FROM personeller")
print(cur.fetchall())

