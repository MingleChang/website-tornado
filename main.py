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

from settings import settings,mysql_param,SQLITE_PATH,SQLITE_SQL_PATH,MYSQL_SQL_PATH
from urls import url_patterns

from tornado.options import define, options

define("port", default=8000, help="run on the given port", type=int)

class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(url_patterns, **settings)
        #MySQL数据库初始化 PS:使用sqlite时请使用%s作为sql语句占位符
        self.db = mysql.connector.connect(**mysql_param)
        # self.createMySQLTable()
        
        #Sqlite数据库初始化 PS:使用sqlite时请使用？作为sql语句占位符
        # self.db = sqlite3.connect(SQLITE_PATH)

    def createMySQLTable(self):
        cursor = self.db.cursor()
        allSql=self.readMySQL()
        for sql in allSql.split(';',1):
            cursor.execute(sql)
        cursor.close()
        self.db.commit()

    def readMySQL(self):
        file_object = open(MYSQL_SQL_PATH)
        try:
            all_the_text = file_object.read()
        finally:
            file_object.close()
        return all_the_text
  
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
