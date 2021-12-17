from argparse import Namespace
from typing import Union
from .blob_format import format_blob

Value = Union[
	str,
	bytes,
	int,
	float,
	None
]

def stringify(value: Value, opts: Namespace) -> str:
	if isinstance(value, bytes):
		return format_blob(value)

	elif value is None:
		return opts.null_value

	return str(value)
	