from sys import exit
from .args import parser
from .shell import Shell
from . import __version__
import logging

def main():
	args = parser.parse_args()

	if args.verbosity == "none":
		level = 100
	
	else:
		level = getattr(logging, args.verbosity.upper())

	logging.basicConfig(
		level=level
	)
	
	print("SQLite3-Shell", __version__)

	shell = Shell(args)
	
	if args.database == ":memory:":
		print("Connected to a temporary in-memory database")
		print("Use '.open FILE;' to open a database file")

	else:
		print(f"Connected to {args.database}")

	print("Use '.help;' for help on dot commands")

	try:
		shell.run()
	
	except (KeyboardInterrupt, EOFError):
		print()
		exit()

main()
