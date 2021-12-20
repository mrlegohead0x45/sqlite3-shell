DROP TABLE IF EXISTS test_data;
CREATE TABLE test_data (
	i integer,
	f real,
	b blob,
	t text
);
INSERT INTO test_data (i, f, b, t) VALUES (
	1, 2.0, x'fffe62006c006f0062005f007400650073007400', 'text data;'
);
INSERT INTO test_data (i, b) VALUES (
	5, x'cea0'
);
