#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

# print(os.name)

# print(os.environ)

print([x for x in os.listdir('/Users/jiangmingli/myfile/python-learn/io') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])