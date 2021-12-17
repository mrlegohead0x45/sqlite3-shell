from argparse import Namespace
import base64

BLOB_ENCODINGS = {
	"base64": lambda b: base64.b64encode(b).decode(),
	"base85": lambda b: base64.b85encode(b).decode(),
	"hex": lambda b: b.hex(),
	"raw": lambda b: b.decode(errors="ignore")
}

def format_blob(blob: bytes, opts: Namespace) -> str:
	encoded = BLOB_ENCODINGS[opts.blob_encoding](blob)

	return opts.blob_format.format(encoded)
