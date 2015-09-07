#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import uuid
import json
from sqlalchemy.orm import class_mapper
from models.models import Joke,User
from handlers.api import APIHandler

class GetJokeAPIHandler(APIHandler):
	def get(self):
		jokes=self.db.query(Joke)
		array=[]
		for joke in jokes:
			columns = [c.key for c in class_mapper(joke.__class__).columns]
			dic = dict((c, self.getAttrModel(joke, c)) for c in columns)
			array.append(dic)

		self.status=200
		jsonStr=self.getJsonResult(result=array,count=len(array))
		self.write(jsonStr)

	def post(self):
		pass

	
		