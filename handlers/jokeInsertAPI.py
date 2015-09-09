#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import uuid
import json
from sqlalchemy.orm import class_mapper
from models.models import Joke,Tag,User
from handlers.api import APIHandler

class AddJokeAPIHandler(APIHandler):
	def get(self):
		userid=self.get_argument('userid','')
		title=self.get_argument('title','')
		content=self.get_argument('content','')
		tagid=self.get_argument('tagid','')
		self.addJoke(userid,title,content,tagid)
		
	def post(self):
		userid=self.get_argument('userid','')
		title=self.get_argument('title','')
		content=self.get_argument('content','')
		tagid=self.get_argument('tagid','')
		self.addJoke(userid,title,content,tagid)

	def checkTag(self,tagid):
		count=self.db.query(Tag).filter(Tag.tagid==tagid).count()
		if count>0:
			return True
		else:
			return False

	def checkUser(self,userid):
		count=self.db.query(User).filter(User.userid==userid).count()
		if count>0:
			return True
		else:
			return False

	def addJoke(self,userid,title,content,tagid):
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
		