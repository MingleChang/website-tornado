#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from handlers.base import BaseHandler

class LoginHandler(BaseHandler):
	def get(self):
		if self.get_current_user():
			self.redirect('/')
			return
		self.render('login.html')

	def post(self):
		username=self.get_argument('username','')
		password=self.get_argument('password','')
		hint = self.checkUserNameAndPassword(username,password)
		if hint=='':
			self.set_secure_cookie('username', username)
			self.redirect('/')
		else:
			self.redirect('login')

	def  checkUserNameAndPassword(self,username,password):
		cursor = self.db.cursor()
		cursor.execute('select * from user where name=? and password=?',(username,password))
		values = cursor.fetchall()
		cursor.close()
		if len(values)==0:
			return '帐号或密码错误'
		else:
			return ''	
