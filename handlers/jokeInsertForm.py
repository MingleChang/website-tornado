#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
import uuid
import tornado.httpclient
from models.models import Tag
from handlers.base import BaseHandler

class AddJokeFormHandler(BaseHandler):
	def get(self):
		self.render('admin/addjoke.html')

	def post(self):
		self.render('admin/addjoke.html')
		