#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import datetime
import mysql.connector
import sqlite3

from settings import settings,DB_USERNAME,DB_PASSWORD,DB_DATEBASE,LISTEN_PORT,SQLITE_PATH
from urls import url_patterns

from tornado.options import define, options

class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(url_patterns, **settings)
        # self.db = mysql.connector.connect(user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATEBASE)
        self.db = sqlite3.connect(SQLITE_PATH)
        cursor = self.db.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS user (id varchar(100) NOT NULL PRIMARY KEY,name varchar(100),password varchar(100))')
        cursor.execute('CREATE TABLE IF NOT EXISTS blog (id varchar(100) NOT NULL PRIMARY KEY,userid varchar(100) NOT NULL REFERENCES user (id) ON DELETE CASCADE ON UPDATE CASCADE,title varchar(100),description varchar(100),detail text)')
        cursor.close()
        self.db.commit()
  
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(LISTEN_PORT)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
