#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from handlers.base import BaseHandler

class BlogHandler(BaseHandler):
	def get(self):
		values=self.selectedAllBlog()
		self.render('blog.html',values=values)

	def post(self):
		self.selectedAllBlog()
		self.render('blog.html',values=values)

	def selectedAllBlog(self):
		cursor = self.db.cursor()
		cursor.execute('select id,title,description from blog')
		values = cursor.fetchall()
		cursor.close()
		return values
