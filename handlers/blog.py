#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from handlers.base import BaseHandler

class BlogHandler(BaseHandler):
	def get(self):
		self.render('blog.html')

	def post(self):
		self.render('blog.html')
