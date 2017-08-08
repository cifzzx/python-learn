#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

now = datetime.now()
print(now)

dt = datetime.strptime('1993-08-25 11:11:11', '%Y-%m-%d %H:%M:%S')
print(dt)

dtm = datetime.now()
str_time = dtm.strftime('%Y-%m-%d %H:%M:%S')
print(str_time)
