from sqlite3 import connect
from json import load

with open("data.json", "r") as file:
	data = load(file)

open("test.db", "w").close()
with open("test-schema.sql", "r") as file:
	connect("test.db").executescript(file.read())
	