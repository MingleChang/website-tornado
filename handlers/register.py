#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import uuid
from datetime import * 
from models.models import User
from handlers.base import BaseHandler

class RegisterHandler(BaseHandler):
	def get(self):
		username=self.get_argument('register','')
		self.render('register.html',username=username)
	def post(self):
		username=self.get_argument('username')
		password=self.get_argument('password')
		if self.checkUserExist(username):
			self.redirect('/register?register='+username)
		else:
			userid=uuid.uuid1().hex
			newuser=User(userid=userid,username=username,password=password)
			newuser.create=datetime.today()
			newuser.update=datetime.today()
			self.db.add(newuser)
			self.db.commit()
			self.db.close()
			self.redirect('/login')

	def checkUserExist(self,username):
		count=self.db.query(User).filter(User.username==username).count()
		if count>0:
			return True
		else:
			return False
			