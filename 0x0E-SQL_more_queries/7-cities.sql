-- creates the database hbtn_0d_usa and the table cities

CREATE DATABASE IF NOT EXISTS cities;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT FOREIGN KEY NOT NULL REFERENCES states(id);
	name VARCHAR(256));
