from sqlite3_shell.output.json_output import CustomJSONEncoder
from sqlite3_shell.args import parser
from sqlite3 import connect, Row
from . import data

data = data["json"]

conn = connect("test.db")
conn.row_factory = Row

res = conn.execute("SELECT * FROM test_data;").fetchall()

def test_basicJson():
	args = parser.parse_args(["-f", "json"])
	json = CustomJSONEncoder(args).encode(res)

	assert data["basic"] == json

def test_blobJson():
	args = parser.parse_args(["-f", "json", "-be", "base64", "-bf", "blob({})"])
	json = CustomJSONEncoder(args).encode(res)
	
	assert json == data["blob"]
	