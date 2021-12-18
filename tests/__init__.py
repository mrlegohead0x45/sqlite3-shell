from sqlite3 import connect, Row

open("tests/test.db", "w").close()
with open("tests/test-schema.sql", "r") as file:
	connect("tests/test.db").executescript(file.read())
	
conn = connect("tests/test.db")
conn.row_factory = Row
res = conn.execute("SELECT * FROM test_data;").fetchall()
conn.close()