#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.web
from handlers.base import BaseHandler

class IndexHandler(BaseHandler):
    def get(self):
    	username=self.current_user
    	if username==None:
    		username="World"
        self.render('index.html',username=username)