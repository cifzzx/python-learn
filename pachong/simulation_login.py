import urllib
import urllib2

# POST
# values = {"username": "ljm", "password": "123"}
# data = urllib.urlencode(values)
# url = "http://127.0.0.1:5000/sigin"
# request = urllib2.Request(url, data)
# response = urllib2.urlopen(request)
# print response.read()

# GET
values = {"username": "ljm", "password": "123"}
data = urllib.urlencode(values)
url = "http://127.0.0.1:5000/sigin/get"
response = urllib2.urlopen(url+'?'+data)
print response.read()
