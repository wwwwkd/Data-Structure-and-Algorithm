import traceback
class Dog:
	dogbook = {"黄色":30, "黑色":20, "白色":0}

	def __init__(self, name, color, weight):
		self.name = name
		self.color = color
		self.weight = weight
		#此处省略若干行，应该更新dogbook的数量

    #实例方法: 定义时,必须把self作为第一个参数，可以访问实例变量，只能通过实例名访问
	def bark(self):
		print("{},叫了起来".format(self.name))

    #类方法：定义时,必须把类作为第一个参数，可以访问类变量，可以通过实例名或类名访问
	@classmethod
	def dog_num(cls):
		num = 0
		for v in cls.dogbook.values():
			num = num + v
		return num

    #静态方法：不强制传入self或者cls, 他对类和实例都一无所知。不能访问类变量，也不能访问实例变量；可以通过实例名或类名访问
	@staticmethod
	def total_weights(dogs):
		total = 0
		for o in dogs:
			total = total + o.weight
		return total

# 1. 类对象，调用类方法
print("类对象，调用类方法：共有 {} 条狗".format(Dog.dog_num()))
print('-'*20)
# 2. 实例化对象，调用实例方法
d1 = Dog("大黄", "黄色", 10)
d1.bark()
print('-'*20)
# 3. 实例化对象，调用类方法
print("实例化对象，调用类方法：共有 {} 条狗".format(d1.dog_num()))
print('-'*20)

d2 = Dog("旺财", "黑色", 8)
d2.bark()
print('-'*20)

# 4. 实例对象，调用静态方法
print("实例对象，调用静态方法：狗一共重{}".format(d1.total_weights([d1, d2])))
print('-'*20)

# 5. 类对象，调用静态方法
print("类对象，调用静态方法：狗一共重{}".format(d1.total_weights([d1, d2])))
print('-'*20)

# 6. 类对象调用实例方法
try:
    Dog.bark()
except:
    info = traceback.format_exc()
    print(info)
else:
    print('no error')
finally:
    print('-'*20)