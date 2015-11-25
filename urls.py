#!/usr/bin/env python
# -*- coding: utf-8 -*-
from handlers.base import BaseHandler
from handlers.index import IndexHandler

from handlers.api import APIHandler

url_patterns = [
	(r'/', IndexHandler),

	(r'/api/.*', APIHandler),
	(r'.*',BaseHandler),
]