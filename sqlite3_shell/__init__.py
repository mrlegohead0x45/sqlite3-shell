__version__ = "0.1.0"
__all__ = [
	"output",
	"args"
]

try:
	import sqlparse
	SQLPARSE = True
except ModuleNotFoundError:
	SQLPARSE = False
