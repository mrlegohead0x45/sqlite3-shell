import sqlite3
import sqlparse
from argparse import Namespace
from typing import List, Optional
from os import chdir
from subprocess import getoutput
from sys import exit
from .args import parser
from .output import OUTPUT_FORMAT_MAP, stringify

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
				

	def handle_dot_command(self, cmd: str) -> sqlite3.Connection:
		cmd = cmd.strip()

		if cmd.startswith((".exit", ".quit")):
			self.conn.close()
			exit()

		elif cmd.startswith(".open"):
			# remove '.open ' and trailing ;
			file = cmd[6:-1]
			self.conn.close()
			self.conn = sqlite3.connect(file)
			self.conn.row_factory = sqlite3.Row
			self.conn.isolation_level = None # allow user to do their own transactions

		elif cmd.startswith(".cd"):
			dir = cmd[4:-1] # remove '.cd ' and trailing ;
			chdir(dir)

		elif cmd.startswith(".read"):
			file = cmd[6:-1] # remove '.read ' and trailing ;
			with open(file, "r") as f:
				self.run_sql(f.read())
				
		return self.conn

	def output(self, rows: Rows) -> None:
		func = OUTPUT_FORMAT_MAP.get(self.opts.format, None)
		
		if func is None:
			if self.opts.headers:
				rows.insert(0, rows[0].keys())

			for row in rows:
				out = map(lambda v: stringify.stringify(v, self.opts), row)
				print(self.opts.sep.join(out))

		else:
			print(func(rows, self.opts))

	# run a single statement and return it's results if any
	def run_stmt(self, stmt: str) -> Optional[Rows]:
		stmt = stmt.strip() # remove leading & trailing whitespace

		if stmt.startswith("."):
			try:
				self.conn = self.handle_dot_command(stmt)

			except (FileNotFoundError, ) as e:
				print(f"Error: {e}")
			
			finally:
				return None

		if stmt.upper().startswith("SELECT"):
			select = True

		try:
			cur = self.conn.execute(stmt)
		
		except sqlite3.Error as e:
			print(f"Error: {e}")
			return None

		if select:
			res = cur.fetchall()

		else:
			res = None

		cur.close()
		return res

	# run statements and output results
	def run_sql(self, sql: str) -> None:
		stmts = sqlparse.split(sql)
		
		for stmt in stmts:
			res = self.run_stmt(stmt)

			if res is not None:
				self.output(res)

	# the main method as it were
	def run(self) -> None:
		buffer = ""
		prompt = "sqlite3> "
		# main loop
		while True:
			buffer += input(prompt)

			if sqlite3.complete_statement(buffer):
				self.run_sql(buffer)
				buffer = ""
				prompt = "sqlite3> "
			
			else:
				prompt = "    ...> "
		
