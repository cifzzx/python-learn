# 面向对象编程

## 类和实例

### __init__方法

```
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age =age
```

* __init__方法第一个参数，永远是self
* self表示实例本身
* 有了__init__方法，在创建实例时，就不能传入空的参数

### 类的方法

```
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def print_info(self):
        print('%s: %s' % (self.name,self.age))

```

* 定义一个方法，除了第一个参数是self，其他和普通函数一样
* 调用方法直接通过实例调用，除了self不传，其它参数正传入

### 属性访问权限

- 属性前加__表示私有属性

```
class Student(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age =age

```

- getter&setter方法

```
class Student(object):
    def __init__(self,name,age):
        self.__name = name
        self.__age =age

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name
```

### 继承和多态

```
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    pass

```
- 使用isinstance()判断变量是某种类型

```
isinstance(a,Animal)
```

### 静态语言和动态语言

- 对于静态语言来说，如果需要传入Animal类型，则传入的对象必须是Animal或者它的子类，否则，无法调用run方法。
- 对于python来说，则不一定要传入Animal类型，只需要保证传入的对象有一个run方法就行。

### 获取对象信息

- 使用type()函数

```
>>> type(123)
<class 'int'>
>>> type('123')
<class 'str'>
>>> type(None)
<type(None) 'NoneType'>

```
==如果一个变量指向函数或者类，也可以用type()判断==
```
>>> type(abs)
<class 'builtin_function_or_method'>
>>> type(a)
<class '__main__.Animal'>

```
判断一个对象是否是函数,可以使用types模块中定义的常量

```
>>> import types
>>> def fn():
...     pass
...
>>> type(fn)==types.FunctionType
True
>>> type(abs)==types.BuiltinFunctionType
True
>>> type(lambda x: x)==types.LambdaType
True
>>> type((x for x in range(10)))==types.GeneratorType
True
```
### 使用isinstance()

对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数

isinstance()还可以判断变量是否是某些类型中的一种：
```
>>> isinstance([1, 2, 3], (list, tuple))
True
>>> isinstance((1, 2, 3), (list, tuple))
True
```

### 使用dir()
如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法

```
>>> dir('ABC')
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

```

### 实例属性和类属性

实例绑定属性的方法是通过实例变量，或者通过self变量:
```
class Student(object):
    def __init__(self, name):
        self.name = name

s = Student('Bob')
s.score = 90

```

但是，如果Student类本身需要绑定一个属性呢？可以直接在class中定义属性，这种属性是类属性，归Student类所有：

```
class Student(object):
    name = 'Student'

```

当我们定义了一个类属性后，这个属性虽然归类所有，但类的所有实例都可以访问到。来测试一下:

```
class Person(object):
	gender = 'male' # 类属性
	def __init__(self,name,age):  # 实例属性
		self.__name = name
		self.__age = age

	def set_name(self,name):
		self.__name = name

	def get_name(self):
		return self.__name

p = Person('p','23')
p.set_name('ljm')
print(p.get_name())
print(p.gender) # p实例没有gender属性，先找person类的类属性

p.gender = 'female'
print(p.gender)
print(Person.gender) # 上面更改了gender属性值，但不影响Person类的gender值

# 运行结果
>>ljm
>>male
>>female
>>male

```
从上面的例子可以看出，在编写程序的时候，千万不要把实例属性和类属性使用相同的名字，因为相同名称的实例属性将屏蔽掉类属性，但是当你删除实例属性后，再使用相同的名称，访问到的将是类属性。

# I/O编程

## 文件读写

### 只读模式打开

```
file = open('/Users/ljm/test.txt', 'r')
```

read()方法可以读取文件的内容，把内容读进内存用'str'对象表示

为了保证无论是否出错都能正确地关闭文件,使用rry.....finally
```
try:
    f = open('/path/to/file', 'r')
    print(f.read())
finally:
    if f:
        f.close()
```
如果每打开一个文件都像上面那样写，就有些繁琐了，python引入了with语句来自动帮我们调用close()方法
```
with open('/path/to/file', 'r') as f:
    print(f.read())
```
- read(size):一次读取指定大小的字节数的内容
- readline():每次读取一行
- readlines()：一次读取所有内容，并返回一个list

### 读取二进制文件

前面讲的是默认读取文本文件，要读取二进制文件，如图片，视频等，要使用'rb'模式打开
```
f = open('/Users/ljm/test.jpg', 'rb')
f.read()
```

### 字符编码

如果打开一个非UTF-8编码的文件，需要给open()方法传入encoding参数。

```
with open ('/Users/ljm/gbk.txt','r',encoding='gbk') as file:
file.read()
```
遇到有些编码不规范的文件，可能遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略
```
with open ('/Users/ljm/gbk.txt','r',encoding='gbk',errors='ignore') as file:
file.read()

```

### 写文件

写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件
```
with open ('/User/ljm/w.txt','w') as file:
file.write('hello world')
```

### StringIO&ByteIO

#### StringIO

```
from io import BytesIO as StringIO # python2环境

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')
print(f.getvalue())

```
#### BytesIO

StringIO操作字符串，
```
#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, sys
from io import BytesIO

b = BytesIO()
b.write('李江明')

print(b.getvalue())

bt = BytesIO('youhujia李江明')
print(bt.read())

```

## 操作文件和目录

python内置的是os模块直接调用操作系统提供的接口函数

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

print(os.name)

```

如果是posix，说明操作系统是Linux、Unix、或者是Mac Os X;如果是nt,则是windows系统

```
>>> os.uname()
('Darwin', 'jiangmingdeMacBook-Pro.local', '16.6.0', 'Darwin Kernel Version 16.6.0: Fri Apr 14 16:13:31 PDT 2017; root:xnu-3789.60.24~4/RELEASE_X86_64', 'x86_64')
```
使用os.uname()获取系统更多详细信息
uname在windows系统不支持，说明os模块的某些函数是和操作系统相关的。

### 环境变量

在操作系统中定义的环境变量，全部保存在os.envrino这个变量中。
```
>>> os.environ
{'LESS': '-R', 'LC_CTYPE': 'zh_CN.UTF-8', 'TERM_PROGRAM_VERSION': '3.0.15', 'LOGNAME': 'jiangmingli', 'USER': 'jiangmingli', 'PATH': '/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin', 'HOME': '/Users/jiangmingli', 'ZSH': '/Users/jiangmingli/.oh-my-zsh', 'TERM_PROGRAM': 'iTerm.app', 'LANG': 'zh_CN.UTF-8', 'TERM': 'xterm-256color', 'Apple_PubSub_Socket_Render': '/private/tmp/com.apple.launchd.sAwp1QDlFv/Render', 'COLORFGBG': '7;0', 'SHLVL': '1', 'SECURITYSESSIONID': '186a7', 'XPC_FLAGS': '0x0', 'ITERM_SESSION_ID': 'w0t3p0:81B932C6-460F-46F5-9D51-B52792E50D9D', '_': '/usr/local/bin/python', 'TERM_SESSION_ID': 'w0t3p0:81B932C6-460F-46F5-9D51-B52792E50D9D', 'XPC_SERVICE_NAME': '0', 'SSH_AUTH_SOCK': '/private/tmp/com.apple.launchd.jOhqISjPuT/Listeners', 'SHELL': '/bin/zsh', 'ITERM_PROFILE': 'Default', 'TMPDIR': '/var/folders/4k/yh2x2d150s73pjpqh0tnp_xw0000gn/T/', 'LSCOLORS': 'Gxfxcxdxbxegedabagacad', 'OLDPWD': '/Users/jiangmingli', '__CF_USER_TEXT_ENCODING': '0x1F5:0x19:0x34', 'PWD': '/Users/jiangmingli', 'PAGER': 'less', 'COMMAND_MODE': 'unix2003'}

```
如果要获取某个环境变量值，使用os.environ.get('key')获取

```
>>> os.environ.get('LOGNAME')
'jiangmingli'

```

### 操作文件和目录

- os.path.abspath('.'): 获取当前路径的绝对路径
- os.path.join('/user/jiangmingli','/python'): 将两个路径拼接
- os.path.split('/user/jiangmingli/test.python'): 路径拆分，后一部分总是表示最后一级别的文件或者目录
- os.path.splitext('/user/jiangmingli/test.python'): 可以直接获取扩展名
- os.rename('test.py','learn.py'):对文件重命名
- os.remove('learn.py'):删除文件
- 获取当前目录下所有的目录

```
 [x for x in os.listdir('.') if os.path.isdir(x)]
```
- 获取当前目录下所有的pyhon文件
```
[x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
```

### 序列化

我们把变量从内存中变成可存储或传输的过程称之为序列化，在Python中叫pickling;反过来，把变量内容从序列化的对象重新读到内存里称之为反序列化，即unpickling

Python提供了==pickles==模块来实现序列化

#### 序列化
```
import pickle

d = dict(name='ljm',age='23',addrdess="北京昌平")
pickle.dumps(d)

f = open('/Users/jiangmingli/myfile/python-learn/io/dumps.txt','wb')
pickle.dump(d,f)

```
#### 反序列化

```
import pickle

f = open('/Users/jiangmingli/myfile/python-learn/io/dumps.txt','rb')
d = pickle.load(f)
print(d)
f.close()
```

### JSON
python的JSON模块提供了完善的python对象到JSON对象的转换

- 将pyton对象转化为json对象

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import simplejson as json

d = dict(name='ljm',age='23',addrdess="北京昌平")
print(json.dumps(d))

```

- 将python对象序列化写入文件

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import simplejson as json
f = open('/Users/jiangmingli/myfile/python-learn/io/file/ljm.json','wb')
json.dump(d,f)

```

- 文件里的内容反序列化成python对象

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import simplejson as json
f = open('/Users/jiangmingli/myfile/python-learn/io/file/ljm.json','rb')

d = json.load(f)
print(d)

```
### Json高阶

将一个类转化成json对象

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

import simplejson as json

class Student(object):
    def __init__(self,age,name,score):
        self.age = age
        self.name = name
        self.score = score

# 先将student对象转成dict
def student_to_dict(student):
    return {
        "name":student.name,
        "age":student.age,
        "score":student.score
    }
stu = Student(23,'ljm',100)
print(json.dumps(stu,default=student_to_dict))

```
## 正则表达式

### re模块

python提供的re模块，包括所有正则表达式的功能。

- 写法
```
s = r'ABC\-001'
```
- 判断是否匹配正则
```
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')

```

## python常用内建模块

### datetime是python处理日期和时间的标准库

- 获取当前日期和时间

```
#!/usr/bin/python
# -*- coding: utf-8 -*-

from datetime import datetime

now = datetime.now()
print(now)

```
- 获取指定日期和时间

```
dt = datetime(1993,7,9,11,11)
print(dt)

```
- 将datetime类型转换成timestamp

```
dt = datetime(1993,7,9,11,11)
tsp = dt.timestamp()
```

- timestamp转换成datetime

```
tsp = 1499820667.0
dt = datetime.fromtimestamp(tsp)

```
- str转换成datetime

```
dt = datetime.strptime('1993-07-09 11:11:11','%Y-%m-%d %H:%M:%S')
print(dt)

```
- datetime转换成str

```
dt = datetime.now()
str_time = dt.strftime(dt)
print(str_time)

```
