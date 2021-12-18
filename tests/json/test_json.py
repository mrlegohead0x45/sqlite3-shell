from sqlite3_shell.output.json_output import format_to_json
from sqlite3_shell.args import parser
from .. import res

def test_basic_json():
	with open("tests/json/basic.json", "r") as file:
		data = file.read()

	args = parser.parse_args(["-f", "json"])
	json = format_to_json(res, args)

	assert json == data

def test_blob_json():
	with open("tests/json/blob.json", "r") as file:
		data = file.read()

	args = parser.parse_args(["-f", "json", "-be", "base64", "-bf", "blob({})"])
	json = format_to_json(res, args)

	assert json == data

def test_pretty_headers_json():
	with open("tests/json/headers_pretty.json", "r") as file:
		data = file.read()

	args = parser.parse_args(["-f", "json", "--headers", "-p"])
	json = format_to_json(res, args)

	assert json == data

