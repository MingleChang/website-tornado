#!/usr/bin/env python
# -*- coding: utf-8 -*-
from handlers.base import BaseHandler
from handlers.index import IndexHandler
from handlers.login import LoginHandler
from handlers.register import RegisterHandler
from handlers.logout import LogoutHandler
from handlers.api import APIHandler
from handlers.loginAPI import LoginAPIHandler
from handlers.registerAPI import RegisterAPIHandler

from handlers.jokeInsertAPI import AddJokeAPIHandler
from handlers.jokeSelectAPI import GetJokeAPIHandler

from handlers.tagInsertAPI import AddTagAPIHandler
from handlers.tagSelectAPI import GetTagAPIHandler

from handlers.commentInsertAPI import AddCommentAPIHandler
from handlers.commentSelectAPI import GetCommentAPIHandler

url_patterns = [
	(r'/', IndexHandler),
	(r'/login', LoginHandler),
	(r'/register', RegisterHandler),
	(r'/logout', LogoutHandler),

	(r'/api/login', LoginAPIHandler),
	(r'/api/register', RegisterAPIHandler),
	
	(r'/api/addjoke', AddJokeAPIHandler),
	(r'/api/getjoke', GetJokeAPIHandler),

	(r'/api/addtag', AddTagAPIHandler),
	(r'/api/gettag', GetTagAPIHandler),

	(r'/api/addcomment', AddCommentAPIHandler),
	(r'/api/getcomment', GetCommentAPIHandler),

	(r'/api/.*', APIHandler),
	(r'.*',BaseHandler),
]