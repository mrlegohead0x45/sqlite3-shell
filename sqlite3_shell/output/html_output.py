from html import escape
from argparse import Namespace
from sqlite3 import Row
from typing import List

_HTML_TAGS = {
	"regular":{
		"table_start": "<table>",
		"row_start": "<tr>",
		"header_start": "<th>",
		"header_end": "</th>",
		"data_start": "<td>",
		"data_end": "</td>",
		"row_end": "</tr>",
		"table_end": "</table>"
	},
	"pretty":{
		"table_start": "<table>\n",
		"row_start": "\t<tr>\n",
		"header_start": "\t\t<th>",
		"header_end": "</th>\n",
		"data_start": "\t\t<td>",
		"data_end": "</td>\n",
		"row_end": "\t</tr>\n",
		"table_end": "</table>"
	}
}

def formatToHtml(rows: List[Row], opts: Namespace) -> str:
	if not rows:
		return ""

	key = "regular"

	if opts.pretty:
		key = "pretty"

	HTML_TAGS = _HTML_TAGS[key]

	output = HTML_TAGS["table_start"]

	if opts.headers:
		output += HTML_TAGS["row_start"]
		for header in rows[0].keys():
			output += HTML_TAGS["header_start"]
			output += escape(header)
			output += HTML_TAGS["header_end"]
	
		output += HTML_TAGS["row_end"]




	
