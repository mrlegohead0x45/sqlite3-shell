import sqlite3
from argparse import Namespace
from . import SQLPARSE

class Shell:
	def __init__(self, opts: Namespace) -> None:
		self.opts = opts
		self.conn = sqlite3.connect(self.opts.database)
		self.conn.row_factory = sqlite3.Row
		self.conn.isolation_level = None # allow user to do their own transactions


