#!/usr/bin/env python
# -*- coding: utf-8 -*-
from handlers.base import BaseHandler
from handlers.index import IndexHandler
from handlers.blog import BlogHandler
from handlers.login import LoginHandler
from handlers.register import RegisterHandler
from handlers.addBlog import AddBlogHandler
from handlers.blogDetail import BlogDetailHandler

from handlers.api import APIHandler

url_patterns = [
	(r'/', IndexHandler),
	(r'/blog',BlogHandler),
	(r'/login',LoginHandler),
	(r'/register',RegisterHandler),
	(r'/addblog',AddBlogHandler),
	(r'/blog/(\w+)',BlogDetailHandler),

	(r'/api/.*', APIHandler),
	(r'.*',BaseHandler),
]