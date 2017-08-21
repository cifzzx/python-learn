#!/usr/bin/python
# -*- coding: utf-8 -*-

import pickle

d = dict(name='ljm', age='23', addrdess="北京昌平")
pickle.dumps(d)

f = open('/Users/jiangmingli/myfile/python-learn/io/dumps.txt', 'wb')
pickle.dump(d, f)

f = open('/Users/jiangmingli/myfile/python-learn/io/dumps.txt', 'rb')
d = pickle.load(f)
print(d)
f.close()
