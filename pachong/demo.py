import urllib3

response = urllib3.urlopen("http://www.baidu.com")
print(response.read())