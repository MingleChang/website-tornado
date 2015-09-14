#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import uuid
import tornado.httpclient
from sqlalchemy.orm import class_mapper
from models.models import Tag
from handlers.base import BaseHandler

class AddJokeFormHandler(BaseHandler):
	def get(self):
		tagArr=self.selectAllTag()
		self.render('admin/addjoke.html',tags=tagArr)

	def post(self):
		self.render('admin/addjoke.html')
	
	def selectAllTag(self):
		tags=self.db.query(Tag)
		tagArr=[]
		for tag in tags:
			columns = [c.key for c in class_mapper(tag.__class__).columns]
			dic = dict((c, self.getAttrModel(tag, c)) for c in columns)
			tagArr.append(dic)
		return tagArr
		