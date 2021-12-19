import sqlite3
from argparse import Namespace

class Shell:
	def __init__(self, opts: Namespace) -> None:
		self.opts = opts

		self.conn = sqlite3.connect(self.opts.database)
		self.conn.row_factory = sqlite3.Row
		self.conn.isolation_level = None # allow user to do their own transactions

		self.buffer = ""

	# 	if self.opts.init is not None:
	# 		with open(self.opts.init, "r") as file:
	# 			self.buffer = file.read()
	# 			self.run_sql()

	# def run_sql() -> None:
	# 	pass

	# def handle_dot_command(self, command: str) -> None:
	# 	pass

	# def run() -> None:
	# 	pass

