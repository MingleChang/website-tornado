#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from handlers.base import BaseHandler
import markdown2

class BlogDetailHandler(BaseHandler):
	def get(self,input):
		blogid=input
		print blogid
		value=self.selectedBlogById(blogid)
		self.render('blogDetail.html',content=value)

	def post(self,input):
		blogid=input
		value=self.selectedBlogById(blogid)
		self.render('blogDetail.html',content=value)

	def selectedBlogById(self,blogid):
		cursor = self.db.cursor()
		cursor.execute('select detail from blog where id=%s',(blogid,))
		values = cursor.fetchall()
		cursor.close()
		md=values[0][0]
		value=markdown2.markdown(md, extras=["footnotes"])
		return value