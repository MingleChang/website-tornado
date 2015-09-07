#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from handlers.base import BaseHandler

class LogoutHandler(BaseHandler):
	def get(self):
		self.clear_cookie("username")
		self.redirect('/login')