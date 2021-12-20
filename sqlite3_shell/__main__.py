from .args import parser
from .shell import Shell

def main():
	args = parser.parse_args()
	shell = Shell(args)
	shell.run()

main()
