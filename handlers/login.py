#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from handlers.base import BaseHandler

class LoginHandler(BaseHandler):
	def get(self):
		self.render('login.html')

	def post(self):
		self.render('login.html')
