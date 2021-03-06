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
	admin tinyint(1) NOT NULL DEFAULT 0
)engine=innodb default charset=utf8;
CREATE TABLE IF NOT EXISTS blog (
	id varchar(100) NOT NULL PRIMARY KEY,
	userid varchar(100) NOT NULL REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE,
	title varchar(100),
	description varchar(100),
	detail text,
	ctime timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
	utime timestamp NOT NULL DEFAULT now() ON UPDATE now()
)engine=innodb default charset=utf8;