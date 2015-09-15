#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import uuid
import tornado.httpclient
from sqlalchemy.orm import class_mapper
from models.models import Tag,User
from handlers.base import BaseHandler

class AddJokeFormHandler(BaseHandler):
	def get(self):

		tagArr=self.selectAllTag()
		userArr=self.selectAllUser()
		self.render('admin/addjoke.html',tags=tagArr,users=userArr)

	def post(self):
		pass
	
	def  selectAllUser(self):
		users=self.db.query(User.userid,User.username)
		userArr=[]
		for user in users:
			dic={}
			dic['userid']=user.userid
			dic['username']=user.username
			userArr.append(dic)
		return userArr

	def selectAllTag(self):
		tags=self.db.query(Tag)
		tagArr=[]
		for tag in tags:
			columns = [c.key for c in class_mapper(tag.__class__).columns]
			dic = dict((c, self.getAttrModel(tag, c)) for c in columns)
			tagArr.append(dic)
		return tagArr
		