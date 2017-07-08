#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
from io import BytesIO

b = BytesIO()
b.write('李江明')
print(b.getvalue())

bt = BytesIO('youhujia李江明')
print(bt.read())
