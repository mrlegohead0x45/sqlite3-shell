# sqlite3-shell
[![Run on Repl.it](https://repl.it/badge/github/mrlegohead0x45/sqlite3-shell)](https://repl.it/github/mrlegohead0x45/sqlite3-shell)

A SQLite3 shell written in Python

Depends on [sqlparse](github.com/andialbrecht/sqlparse).

## Planned features
* [ ] dot commands like sqlite3 has
* [x] different output formats

## Planned dot commands
* [x] `.exit`, `.quit` exit
* [ ] `.help` help message
* [ ] `.open FILE` open database file
* [ ] `.args ARGS` parse and apply formatting arguments as though from the command line
* [ ] `.cd DIR` change cwd to DIR
* [ ] `.shell CMD ARGS...` run CMD ARGS... in a system shell
* [ ] `.system` alias for `.shell`
* [ ] `.read FILE` run SQL in FILE 



```
~/sqlite3-shell$ python3 -m sqlite3_shell -h
usage: sqlite3_shell [-h] [--version] [-i file] [-f {csv,html,json}] [--headers]
                     [-s separator] [-p] [-be {base64,base85,hex,raw}] [-bf BLOB_FORMAT]
                     [-n NULL_VALUE]
                     [database]

Python SQLite3 shell

positional arguments:
  database              database file to connect to; by default a temporary in-memory one

optional arguments:
  -h, --help            show this help message and exit
  --version             show program's version number and exit
  -i file, --init file  file with SQL code to run before interactive input is opened

Formatting options:
  Options for formatting output

  -f {csv,html,json}, --format {csv,html,json}
                        format to output data in
  --headers             whether or not to include table headings in output
  -s separator, --sep separator
                        string to use to separate cells in default output mode; default '|'
  -p, --pretty          whether to prettify output
  -be {base64,base85,hex,raw}, --blob-encoding {base64,base85,hex,raw}
                        encoding to output blobs in
  -bf BLOB_FORMAT, --blob-format BLOB_FORMAT
                        format to output blobs in. .format will be called with the encoded
                        blob. default 'BLOB:{}'
  -n NULL_VALUE, --null-value NULL_VALUE
                        string representation of NULL, default 'NULL'
```
