from io import StringIO
from csv import writer
from argparse import Namespace
from sqlite3 import Row
from typing import List
from .stringify import stringify

def format_to_csv(rows: List[Row], opts: Namespace) -> str:
	if opts.headers:
		rows.insert(0, rows[0].keys())

	file = StringIO()
	w = writer(file)

	rows = [tuple(row) for row in rows]
	for row in rows:
		w.writerow(map(lambda v: stringify(v, opts), row))
	
	return "\n".join(file.getvalue().splitlines())
	