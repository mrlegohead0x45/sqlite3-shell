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
	"database", default=":memory:", metavar="FILE",
	help="database file to connect to; by default a temporary in-memory one"
)