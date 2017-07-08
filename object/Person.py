
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
print(Person.gender) # 20行更改了gender属性值，但不影响Person类的gender值

		