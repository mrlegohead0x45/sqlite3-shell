import sqlite3
from argparse import Namespace
import sqlparse
from typing import List, Optional
from sqlite3_shell.output import *

Rows = List[sqlite3.Row]

# this is what's doing all the hard work
class Shell:
	def __init__(self, opts: Namespace) -> None:
		self.opts = opts

		self.conn = sqlite3.connect(self.opts.database)
		self.conn.row_factory = sqlite3.Row
		self.conn.isolation_level = None # allow user to do their own transactions

		if self.opts.init is not None:
			with open(self.opts.init, "r") as file:
				self.run_sql(file.read())
				

	def handle_dot_command(self, command: str) -> Optional[sqlite3.Connection]:
		pass

	def output(self, rows: Rows) -> None:
		if self.opts.format == "json":
			print(json_output.format_to_json(rows))

	# run a single statement and return it's results if any
	def run_stmt(self, stmt: str) -> Optional[Rows]:
		stmt = stmt.strip() # remove leading & trailing whitespace

		if stmt.startswith("."):
			self.handle_dot_command(stmt)
			return None

		if stmt.upper().startswith("SELECT"):
			select = True

		cur = self.conn.execute(stmt)
		if select:
			res = cur.fetchall()

		else:
			res = None

		cur.close()
		return res

	# run statements from and output results
	def run_sql(self, sql: str) -> None:
		stmts = sqlparse.split(sql)
		
		for stmt in stmts:
			res = self.run_stmt(stmt)

			if res is not None:
				self.output(res)

	# the main method as it were
	def run(self) -> None:
		buffer = ""
		# main loop
		while True:
			buffer += input("sqlite3> ")

			if sqlite3.complete_statement(buffer):
				self.run_sql(buffer)
				buffer = ""
			
			else:
				buffer += input("    ...>")
		
