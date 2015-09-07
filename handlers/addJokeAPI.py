#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import uuid
import json
from sqlalchemy.orm import class_mapper
from models.models import Joke
from handlers.api import APIHandler

class AddJokeAPIHandler(APIHandler):
	def get(self):
		userid=self.get_argument('userid',None)
		title=self.get_argument('title',None)
		content=self.get_argument('content',None)
		self.addJoke(userid,title,content)
		
	def post(self):
		userid=self.get_argument('userid',None)
		title=self.get_argument('title',None)
		content=self.get_argument('content',None)
		self.addJoke(userid,title,content)

	def addJoke(self,userid,title,content):
		if content==None or len(content)==0:
			jsonStr=self.getJsonResult()
			self.write(jsonStr)
		else:
			jokeid=uuid.uuid1().hex
			newjoke=Joke()
			newjoke.jokeid=jokeid
			newjoke.userid=userid
			newjoke.title=title
			newjoke.content=content
			columns = [c.key for c in class_mapper(newjoke.__class__).columns]
			dic = dict((c, self.getAttrModel(newjoke, c)) for c in columns)
			self.status=200
			jsonStr=self.getJsonResult(result=dic)
			
			self.db.add(newjoke)
			self.db.commit()
			self.db.close()

			self.write(jsonStr)
		