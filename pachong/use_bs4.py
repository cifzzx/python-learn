import urllib2

from bs4 import BeautifulSoup

response = urllib2.urlopen("http://www.baidu.com")
html = response.read()

# create beautifulSoup
soup = BeautifulSoup(html)

# format output
# print soup.prettify()

# print soup.title
# print soup.head
# print soup.a
# print soup.p
# print type(soup.title)

# name property

# print soup.name
# print soup.head.name
# print soup.p.name

# attrs property

# print soup.attrs
# print soup.a.attrs
#
# print soup.a.get('href')

# update property

# soup.a['href'] = 'www.baidu.com'
# print soup.a.get('href')
#
# print soup.a
# delete property
# del soup.a['href']
# print soup.a

# -------------------------------------------------------------------------------------------------------------------- #
# NavigableString
print(soup.p)
print(soup.p.string)
print(type(soup.p.string))
