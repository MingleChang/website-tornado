#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import uuid

from models.models import User
from handlers.base import BaseHandler

class LoginHandler(BaseHandler):
	def get(self):
		username=self.current_user
		if username==None:
			self.render('login.html')
		else:
			self.redirect('/')
			
	def post(self):
		username=self.get_argument('username')
		password=self.get_argument('password')
		users=self.db.query(User).filter(User.username==username).filter(User.password==password)
		if users.count()>0:
			self.set_secure_cookie("username", users[0].username,expires_days=None)
			self.redirect('/')
		else:
			self.redirect('/login')
		