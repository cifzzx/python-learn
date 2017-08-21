#!/usr/bin/python
# -*- coding: utf-8 -*-

import simplejson as json

d = dict(name='ljm',age='23',addrdess="北京昌平")
print(json.dumps(d))

f = open('/Users/jiangmingli/myfile/python-learn/io/file/ljm.json','wb')
json.dump(d,f)

f = open('/Users/jiangmingli/myfile/python-learn/io/file/ljm.json','rb')

d = json.load(f)
print(d)
