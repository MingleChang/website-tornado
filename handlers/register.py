#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from handlers.base import BaseHandler
import uuid

class RegisterHandler(BaseHandler):
	def get(self):
		hint=self.get_argument('hint','')
		self.render('register.html',hint=hint)

	def post(self):
		username=self.get_argument('username','')
		password=self.get_argument('password','')
		hint=self.checkUserNameAndPassword(username,password)
		if hint!='':
			self.redirect("/register?hint="+hint)
			return
		self.insertUser(username,password)
		self.redirect('/login')

	def  checkUserNameAndPassword(self,username,password):
		if username=='':
			return '用户名不能为空'
		elif password=='':
			return '密码不能为空'
		elif self.checkUserExist(username):
			return '该用户已存在'
		return ''

	def checkUserExist(self,username):
		cursor = self.db.cursor()
		cursor.execute('select * from user where name=?',(username,))
		values = cursor.fetchall()
		cursor.close()
		if len(values)==0:
			return False
		else:
			return True

	def insertUser(self,username,password):
		cursor = self.db.cursor()
		cursor.execute('insert into user (id, name,password) values (?, ?, ?)',(uuid.uuid1().hex,username,password))
		cursor.close()
		self.db.commit()
