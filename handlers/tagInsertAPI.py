#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import uuid
import json
from sqlalchemy.orm import class_mapper
from models.models import Tag
from handlers.api import APIHandler

class AddTagAPIHandler(APIHandler):
	def get(self):
		content=self.get_argument('content','')
		self.insertTag(content)
		
	def post(self):
		content=self.get_argument('content','')
		self.insertTag(content)

	def checkTag(self,content):
		tags=self.db.query(Tag).filter(Tag.content==content)
		if tags.count()==0:
			return False
		else:
			return True

	def insertTag(self,content):
		if content=='':
			jsonStr=self.getJsonResult()
			self.write(jsonStr)
		elif self.checkTag(content):
			self.status=201
			jsonStr=self.getJsonResult()
			self.write(jsonStr)
		else:
			tag=Tag()
			tag.content=content
			tag.tagid=uuid.uuid1().hex
			self.db.add(tag)
			self.db.commit()
			self.db.close()

			self.status=200
			jsonStr=self.getJsonResult()
			self.write(jsonStr)
		