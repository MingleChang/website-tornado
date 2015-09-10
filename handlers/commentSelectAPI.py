#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import uuid
import json
from sqlalchemy.orm import class_mapper
from models.models import Comment
from handlers.api import APIHandler

class GetCommentAPIHandler(APIHandler):
	def get(self):
		pass
		
	def post(self):
		pass

	
		