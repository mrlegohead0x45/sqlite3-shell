__version__ = "0.1.0"

try:
	import sqlparse
	SQLPARSE = True
except ModuleNotFoundError:
	SQLPARSE = False
