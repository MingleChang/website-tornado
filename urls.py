#!/usr/bin/env python
# -*- coding: utf-8 -*-
from handlers.base import BaseHandler
from handlers.index import IndexHandler

from handlers.api import APIHandler

from handlers.test import TestHandler

url_patterns = [
	(r'/', IndexHandler),

	(r'/test',TestHandler),

	(r'/api/.*', APIHandler),
	(r'.*',BaseHandler),
]