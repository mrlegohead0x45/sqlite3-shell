from argparse import ArgumentParser
from . import __version__

parser = ArgumentParser(
	prog="sqlite3_shell",
	description="Python SQLite3 shell"
)

parser.add_argument(
	"--version", action="version", version=f"sqlite3-shell {__version__}"
)

parser.add_argument(
	"database", default=":memory:", nargs="?",
	help="database file to connect to; by default a temporary in-memory one"
)

parser.add_argument(
	"-i", "--init", metavar="file",
	help="file with SQL code to run before interactive input is opened"
)

formatGroup = parser.add_argument_group(
	"Formatting options",
	description="Options for formatting output"
)

formatGroup.add_argument(
	"-f", "--format",
	choices=["csv", "html", "json"],
	help="format to output data in"
)

formatGroup.add_argument(
	"--headers", action="store_true",
	help="whether or not to include table headings in output"
)

formatGroup.add_argument(
	"-s", "--sep", default="|", metavar="separator",
	help="string to use to separate cells in default output mode; default '|'"
)

formatGroup.add_argument(
	"-p", "--pretty", action="store_true",
	help="whether to prettify output"
)

formatGroup.add_argument(
	"-be", "--blob-encoding", default="hex",
	choices=["base64", "base85", "hex", "raw"],
	help="encoding to output blobs in"
)

formatGroup.add_argument(
	"-bf", "--blob-format", default="BLOB:{}",
	help="format to output blobs in. .format will be called with the encoded blob. " \
		"default 'BLOB:{}'"
)

formatGroup.add_argument(
	"-n", "--null-value", default="NULL",
	help="string representation of NULL, default 'NULL'"
)
