#!/usr/bin/env python
# -*- coding: utf-8 -*-
from handlers.base import BaseHandler
from handlers.index import IndexHandler
from handlers.login import LoginHandler
from handlers.register import RegisterHandler
from handlers.logout import LogoutHandler
from handlers.api import APIHandler
from handlers.loginAPI import LoginAPIHandler
from handlers.addJokeAPI import AddJokeAPIHandler
from handlers.getJokeAPI import GetJokeAPIHandler

url_patterns = [
	(r'/', IndexHandler),
	(r'/login', LoginHandler),
	(r'/register', RegisterHandler),
	(r'/logout', LogoutHandler),

	(r'/api/login', LoginAPIHandler),
	(r'/api/addjoke', AddJokeAPIHandler),
	(r'/api/getjoke', GetJokeAPIHandler),
	(r'/api.*', APIHandler),
	(r'.*',BaseHandler),
]