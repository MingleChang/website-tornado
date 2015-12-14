CREATE TABLE IF NOT EXISTS user (
	id varchar(100) NOT NULL PRIMARY KEY,
	username varchar(100),
	password varchar(100),
	image varchar(500),
	telephone varchar(100),
	email varchar(100),
	nickname varchar(100),
	realname varchar(100),
	sex integer,
	birthday date,
	admin tinyint(1) NOT NULL DEFAULT 0);
CREATE TABLE IF NOT EXISTS blog (
	id varchar(100) NOT NULL PRIMARY KEY,
	userid varchar(100) NOT NULL REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE,
	title varchar(100),
	description varchar(100),
	detail text,
	ctime timestamp NULL DEFAULT CURRENT_TIMESTAMP,
	utime timestamp NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP);