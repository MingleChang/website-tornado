CREATE TABLE IF NOT EXISTS user (
	id varchar(100) NOT NULL PRIMARY KEY,
	username varchar(100),
	password varchar(100),
	telephone varchar(100),
	email varchar(100),
	nickname varchar(100),
	realname varchar(100),
	sex integer,
	birthday date,
	admin boolean NOT NULL DEFAULT 0);
CREATE TABLE IF NOT EXISTS blog (
	id varchar(100) NOT NULL PRIMARY KEY,
	userid varchar(100) NOT NULL REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE,
	title varchar(100),
	description varchar(100),
	detail text,
	ctime datetime NOT NULL DEFAULT (datetime(CURRENT_TIMESTAMP,'localtime')),
	utime datetime NOT NULL DEFAULT (datetime(CURRENT_TIMESTAMP,'localtime')));