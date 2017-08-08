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

### 设置Headers

请求头里包含了很多信息，如文件编码、压缩格式、请求的agent（请求者）等。

```
import urllib
import urllib2

url = "http://www.server.com/login"
uset_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5)"
values = {"username": "ljm", "password": "xxx"}
header = {"User-Agent": uset_agent}
data = urllib.urlencode(values)
request = urllib2.Requst(url, data, header)
response = urllib2.urlopen(requst)
page = response.read()

```
这样就设置了一个headers。

对付`防盗链`,服务器会识别headers中的referer是不是它自己，如果不是，有的服务器也不会响应，所以还可以在headers中加入referer

```
header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5)", "Referer": "http://www.server.com/login"
}
```

另外headers的一些属性，需要特别注意一下:

- User-Agent: 有些服务器或者proxy会通过该值来判断是否是浏览器发出来的请求。
- Content-type: 在使用REST接口时，服务器会检查该值，用来确定HTTP Body中的内容该怎么解析。
- application/xml: 在xml RPC，如RESTful/SOAP调用时使用。
- application/json: 在Json RPC调用时使用。
- application/x-www-form-urlencoded ： 浏览器提交 Web 表单时使用。

在使用服务器提供的RESTful或SOAP服务时，Content-type设置错误会导致服务器拒绝服务。

### Proxy（代理）设置

urllib2默认会使用环境变量http_proxy来设置HTTP Proxy。假如一个网址它会检测某一段时间某个IP的访问次数，如果访问次数过多，就会禁止你访问。所以可以设置一些代理服务器来搞事情，每隔一段时间，换个代理服务器请求，网站君却不知道谁在搞事情。

```
import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http": "http://some-proxy.com:8080"})
null_proxy_handler = urllib2.ProxyHandler({})

if enable_handler:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

```

### timeout设置

urlopen 的timeout参数，可以设置等待多久超时，为了解决一些网站实在过慢而造成的影响。

```
import urllib2

response = urllib2.urlopen("http://www.baidu.com", timeout=10)
```

```
import urllib2

response = urllib2.urlopen("http://www.baidu.com", data, 10)
```

### 使用HTTP的PUT和DELETE方法

http 协议有六种请求方法，get,head,put,delete,post,options，我们有时候需要用到 PUT 方式或者 DELETE 方式请求。

```
import urllib2
request = urllib2.Requst(url, data=data)
request.get_method = lambda: 'PUT' # or 'DELETE'
response = urllib2.urlopen(request)
```

### 使用DebugLog

可以通过下面的方法把DebugLog打开，这样收发包的内容就会在屏幕上打印出来，方便调试，这个也不太常用，仅提一下

```
import urllib2
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')
```