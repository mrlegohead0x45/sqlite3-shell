from json import JSONEncoder
from sqlite3 import Row
from argparse import Namespace
from .blob_format import formatBlob

class CustomJSONEncoder(JSONEncoder):
	def __init__(self, opts: Namespace) -> None:
		self.opts = opts
		super().__init__()

	def default(self, o):
		if isinstance(o, bytes):
			return formatBlob(o, self.opts)

		elif isinstance(o, Row):
			return tuple(o)

		return super().default(o)
		