--creates the table unique_id on your MySQL server.

CREATE TABLE IF NOT EXISTS unique_id(
	id INT,
	name VARCHAR(256));
INSERT INTO first_table (id) IF NOT EXISTS VALUES (1);