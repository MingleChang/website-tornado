CREATE TABLE IF NOT EXISTS user (
	id varchar(100) NOT NULL PRIMARY KEY,
	name varchar(100),
	password varchar(100));
CREATE TABLE IF NOT EXISTS blog (
	id varchar(100) NOT NULL PRIMARY KEY,
	userid varchar(100) NOT NULL REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE,
	title varchar(100),
	description varchar(100),
	detail text);