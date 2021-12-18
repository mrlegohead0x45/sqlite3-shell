from sqlite3_shell.output.html_output import format_to_html
from sqlite3_shell.args import parser
from .. import res

def test_basic_html():
	with open("tests/html/basic.html", "r") as file:
		data = file.read()

	args = parser.parse_args(["-f", "html"])
	html = format_to_html(res, args)

	assert html == data

def test_blob_html():
	with open("tests/html/blob.html", "r") as file:
		data = file.read()

	args = parser.parse_args(["-f", "html", "-bf", "{}", "-be", "base85"])
	html = format_to_html(res, args)

	assert html == data

def test_headers_pretty_html():
	with open("tests/html/headers_pretty.html", "r") as file:
		data = file.read()

	args = parser.parse_args(["-f", "html", "--headers", "-p"])
	html = format_to_html(res, args)

	assert html == data
	