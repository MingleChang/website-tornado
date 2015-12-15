#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os.path

#文件路径
#项目的根路径
BASH_PATH = os.path.dirname(__file__)
#项目模板文件路径
TEMPLATES_PATH = os.path.join(BASH_PATH, "templates")
#项目静态文件路径
STATIC_PATH = os.path.join(BASH_PATH, "static")

#Sqlite的初始化sql语句
SQLITE_SQL_PATH=BASH_PATH+'/sqlite.sql'
#MySQL的初始化sql语句
MYSQL_SQL_PATH=BASH_PATH+'/mysql.sql'

#Sqlite数据库文件路径
SQLITE_PATH=BASH_PATH+'/test.db'

#MySQL数据的连接参数
mysql_param=dict(
	host='128.199.173.244',
	port='3306',
	user='mingle',
	password='mingle0805',
	database='website'
)

#项目基本设置
settings=dict(
	template_path=TEMPLATES_PATH,
	static_path=STATIC_PATH,
	cookie_secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    xsrf_cookies=True,
    login_url="/login",
	debug=True
)