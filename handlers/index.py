#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from handlers.base import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
        # self.render('index.html')
        self.redirect('/blog')

    def post(self):
    	# self.render('index.html')
    	self.redirect('/blog')