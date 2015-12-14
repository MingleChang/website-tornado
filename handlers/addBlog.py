#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from handlers.base import BaseHandler
import uuid

class AddBlogHandler(BaseHandler):
	@tornado.web.authenticated
	def get(self):
		self.render('addBlog.html')

	@tornado.web.authenticated
	def post(self):
		title=self.get_argument('title','')
		description=self.get_argument('description','')
		detail=self.get_argument('detail','')
		username=self.get_secure_cookie("username")
		userid=self.selectedUserId(username)
		self.insertBlog(userid,title,description,detail)
		self.redirect('/')

	def  selectedUserId(self,username):
		cursor = self.db.cursor()
		cursor.execute('select * from user where name=?',(username,))
		values = cursor.fetchall()
		cursor.close()
		return values[0][0]

	def insertBlog(self,userid,title,description,detail):
		cursor = self.db.cursor()
		cursor.execute('insert into blog (id,userid, title,description,detail) values (%s, %s,%s, %s,%s)',(uuid.uuid1().hex,userid,title,description,detail))
		cursor.close()
		self.db.commit()
