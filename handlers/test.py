#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.gen
import tornado.options
import tornado.httpclient

import urllib
import uuid
import json

from handlers.api import APIHandler
from tornado.options import define, options

class TestHandler(APIHandler):
	@tornado.web.asynchronous
	@tornado.gen.engine
	def get(self):
		client = tornado.httpclient.AsyncHTTPClient()
		# client.fetch("http://www.baidu.com",callback=self.on_response)
		response = yield tornado.gen.Task(client.fetch,"http://www.baidu.com")
		self.write(response.body)
		self.finish()
		
	def post(self):
		pass

	def on_response(self, response):
		self.write(response.body)
		self.finish()

