from json import JSONEncoder
from sqlite3 import Row
from argparse import Namespace
from typing import List
from .blob_format import format_blob

class CustomJSONEncoder(JSONEncoder):
	def __init__(self, opts: Namespace) -> None:
		self.opts = opts
		super().__init__()

	def default(self, o):
		if isinstance(o, bytes):
			return format_blob(o, self.opts)

		elif isinstance(o, Row):
			return tuple(o)

		return super().default(o)
		
def format_to_json(rows: List[Row], opts:Namespace) -> str:
	if not rows:
		return ""

	encoder = CustomJSONEncoder(opts)

	if opts.headers:
		rows.insert(0, rows[0].keys())

	if opts.pretty:
		output = "[\n"

		for row in rows:
			output += "\t" + encoder.encode(row) + ",\n"

		output += "]"

		return output

	return encoder.encode(rows)
