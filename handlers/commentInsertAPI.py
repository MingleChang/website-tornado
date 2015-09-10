#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import uuid
import json
from sqlalchemy.orm import class_mapper
from models.models import Comment,Joke,User
from handlers.api import APIHandler

class AddCommentAPIHandler(APIHandler):
	def get(self):
		jokeid=self.get_argument('jokeid','')
		userid=self.get_argument('userid','')
		content=self.get_argument('content','')
		self.insertComment()
		
	def post(self):
		jokeid=self.get_argument('jokeid','')
		userid=self.get_argument('userid','')
		content=self.get_argument('content','')
		self.insertComment()

	def checkJoke(self,jokeid):
		count=self.db.query(Joke).filter(Joke.jokeid==jokeid).count()
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

	def insertComment(self,jokeid,userid,content):
		if jokeid=='':
			pass
		elif userid=='':
			pass
		elif not self.checkUser(userid):
			pass
		elif not self.checkJoke(jokeid):
			pass
		else:
			commentid=uuid.uuid1().hex;
			newcomment=Comment()
			newcomment.commentid=commentid
			newcomment.userid=userid
			newcomment.jokeid=jokeid
			newcomment.content=content

			self.db.add(newjoke)
			self.db.commit()
			self.db.close()
			
			self.status=200
			jsonStr=self.getJsonResult()

			self.write(jsonStr)
		
