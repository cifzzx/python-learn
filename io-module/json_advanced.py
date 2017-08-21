#!/usr/bin/python
# -*- coding: utf-8 -*-

import simplejson as json


class Student(object):
    def __init__(self, age, name, score):
        self.age = age
        self.name = name
        self.score = score


# 先将student对象转成dict
def student_to_dict(student):
    return {
        "name": student.name,
        "age": student.age,
        "score": student.score
    }


stu = Student(23, 'ljm', 100)
print(json.dumps(stu, default=student_to_dict))
