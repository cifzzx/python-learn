# python 爬虫学习
原文[地址](http://wiki.jikexueyuan.com/project/python-crawler-guide/understand-the-basic.html)

## Urllib库的基本使用

```
import urllib2
response  = urllib2.urlopen("http://www.baidu.com")
print response.read()
```
这样两行代码就把百度首页的源码就拔下来了！！！

分析这两行代码

```
response  = urllib2.urlopen("http://www.baidu.com")
```
首先调用的是urllib2的urlopen方法，出入一个url，协议是HTTP协议。当然也可以是FTP、FILE、HTTPS，只是代码一种访问控制协议。urlopen一般接受三个参数：`urlopen(url, data, timeout)`。

第一个参数 url 即为 URL，第二个参数 data 是访问 URL 时要传送的数据，第三个 timeout是设置超时时间。

第一个参数是必需的，第二、三个参数可以不传，data默认为`None`，timeout默认是`socket._GLOBAL_DEFAULT_TIMEOUT`。

在执行`urlopen`方法后，返回一个response对象，返回的信息就保存在里面。response对象有个`read`方法，可以返回获取到的内容。

如果不调用`read`方法，打印出来是response对象。

### 构造Request

其实上面的`urlopen`的参数可以传入一个Reques请求，它其实就是一个Request类的实例。构造是需传入url，data等内容。so，上面的代码可以这么写:

```
import urllib2
request = urllib2.Request("http://www.baidu.com")
response  = urllib2.urlopen(request)
print response.read()
```
效果完全一样，只是加了一个中间变量：`Request`，推荐这种写法，因为在构建请求时还需加入好多内容，通过构建一个Request对象，服务器响应请求得到应答，这样显得逻辑上清晰。

### POST、GET 数据传送

模拟登录。把用户名和密码传送到一个url，然后得到服务器处理后的响应，这该怎么办，下面就来揭晓。

数据传送分为`POST`和`GET`，这两种方式有什么区别，`GET`方式是直接以链接的形式访问，链接中包含了所有的参数。POST不会在网址上显示所有的参数。

这里就要用到我们在上面说到的data参数，我们传送的数据就是这个data:
- POST 方式

```
import urllib
import urllib2

values = {"username": "ljm", "password": "123"}
data = urllib.urlencode(values)
url = "http://127.0.0.1:5000/sigin"
request = urllib2.Request(url, data)
response = urllib2.urlopen(request)
print response.read()
```

这里在本地搭建了一个简单的服务器，返回一个简单的网页内容.

- GET 方式

```
import urllib
import urllib2

# GET
values = {"username": "ljm", "password": "123"}
data = urllib.urlencode(values)
url = "http://127.0.0.1:5000/sigin/get"
response = urllib2.urlopen(url+'?'+data)
print response.read()
```