#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import uuid
import json
from sqlalchemy.orm import class_mapper
from models.models import User
from handlers.api import APIHandler

class LoginAPIHandler(APIHandler):
	def get(self):
		username=self.get_argument('username','')
		password=self.get_argument('password','')
		users=self.db.query(User).filter(User.username==username).filter(User.password==password)
		if users.count()>0:
			user=users[0]
			columns = [c.key for c in class_mapper(user.__class__).columns]
	  		dic = dict((c, self.getAttrModel(user, c)) for c in columns)
	  		dic.pop('password')
	  		self.status=200
	  		jsonStr=self.getJsonResult(result=dic)
	  		self.write(jsonStr)
	  	else:
	  		self.status=201
	  		self.message=u'帐号或密码错误'
	  		jsonStr=self.getJsonResult()
	  		self.write(jsonStr)
	def post(self):
		username=self.get_argument('username','')
		password=self.get_argument('password','')
		users=self.db.query(User).filter(User.username==username).filter(User.password==password)
		if users.count()>0:
			user=users[0]
			columns = [c.key for c in class_mapper(user.__class__).columns]
	  		dic = dict((c, self.getAttrModel(user, c)) for c in columns)
	  		dic.pop('password')
	  		self.status=200
	  		jsonStr=self.getJsonResult(result=dic)
	  		self.write(jsonStr)
	  	else:
	  		self.status=201
	  		self.message=u'帐号或密码错误'
	  		jsonStr=self.getJsonResult()
	  		self.write(jsonStr)