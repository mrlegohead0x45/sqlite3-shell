from argparse import ArgumentParser
from . import __version__

parser = ArgumentParser(
	prog="sqlite3_shell",
	description="Pure Python SQLite3 shell"
)

parser.add_argument(
	"--version", action="version", version=f"sqlite3-shell {__version__}"
)

parser.add_argument(
	"database", default=":memory:", nargs="?",
	help="database file to connect to; by default a temporary in-memory one"
)

formatGroup = parser.add_argument_group(
	"Formatting options",
	description="Options for formatting output"
)

formatGroup.add_argument(
	"-f", "--format",
	choices=["csv", "html", "json", "py"],
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
	"-be", "--blob-encoding",
	choices=["base64", "base85", "hex", "raw"],
	help="encoding to output blobs in"
)
