#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import md5
import uuid
from sqlalchemy.orm import class_mapper
from models.models import User
from handlers.api import APIHandler

class RegisterAPIHandler(APIHandler):
	def get(self):
		username=self.get_argument('username','')
		password=self.get_argument('password','')
		self.register(username,password)
	def post(self):
		username=self.get_argument('username','')
		password=self.get_argument('password','')

	def register(self,username,password):
		if self.checkUsername(username):
			jsonStr=self.getJsonResult()
			self.write(jsonStr)
		elif self.checkPassword(password):
			jsonStr=self.getJsonResult()
			self.write(jsonStr)
		elif self.checkUserExist(username):
			jsonStr=self.getJsonResult()
			self.write(jsonStr)
		else:
			userid=uuid.uuid1().hex
			m1 = md5.new()   
			m1.update(password)   
			newuser=User()
			newuser.userid=userid
			newuser.username=username
			newuser.password=m1.hexdigest()
			newuser.nickname=username
			self.db.add(newuser)
			self.db.commit()
			self.db.close()

			users=self.db.query(User).filter(User.userid==userid)
			user=users[0]
			columns = [c.key for c in class_mapper(user.__class__).columns]
	  		dic = dict((c, self.getAttrModel(user, c)) for c in columns)
	  		dic.pop('password')
	  		dic.pop('create')
	  		dic.pop('update')
	  		self.status=200
	  		jsonStr=self.getJsonResult(result=dic)
	  		self.write(jsonStr)


	def checkUsername(self,username):
		if username=='':
			self.status=201
			self.message='帐号不能为空'
			return True
		elif len(username)<6 or len(username)>20:
			self.status=201
			self.message='帐号长度必须是6-20位'
			return True
		else:
			return False

	def checkPassword(self,password):
		if password=='':
			self.status=201
			self.message='密码不能为空'
			return True
		elif len(password)<6 or len(password)>20:
			self.status=201
			self.message='密码长度必须是6-20位'
			return True
		else:
			return False

	def checkUserExist(self,username):
		count=self.db.query(User).filter(User.username==username).count()
		if count>0:
			self.status=201
			self.message='该账户已存在'
			return True
		else:
			return False