#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import datetime
import mysql.connector

from settings import settings,DB_USERNAME,DB_PASSWORD,DB_DATEBASE,LISTEN_PORT
from urls import url_patterns

from tornado.options import define, options

class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(url_patterns, **settings)
        self.db = mysql.connector.connect(user=DB_USERNAME, password=DB_PASSWORD, database=DB_DATEBASE)
  
def main():
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(LISTEN_PORT)
    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
