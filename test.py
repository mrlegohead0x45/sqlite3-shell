from sqlite3_shell.output import json_output
from sqlite3_shell.args import parser
from sqlite3 import connect, Row

args = parser.parse_args()

open("tests/test.db", "w").close()
with open("tests/test-schema.sql", "r") as file:
	connect("tests/test.db").executescript(file.read())

conn = connect("tests/test.db")
conn.row_factory = Row
cur = conn.cursor()

cur.execute("select * from test_data;")
res = cur.fetchall()
print(json_output.format_to_json(res, args))

