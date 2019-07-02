ass ="a   s    "

print("'"+ass.rstrip()+"'");

# 列表

bicycles = ['trek','cannondale','redline','specialized']

print(bicycles)

message = "My first bicycle was a " + bicycles[0].title() + "."

print(message)

# 创建列表

numbers = list(range(1,6))

print(numbers)  
# # 最小值
print(min(numbers))

# # 列表解析

squares1 = []

for value in range(1,11):
	square = value**2
	squares1.append(square)

	print(squares1)

# # 结果相同但是代码长度不同 

squares2 = [value**2 for value in range(1,11) ]

print(squares2)

#使用列表的一部分

# 切片

players = ['charles','martina','michael','florence','eli']

print(players[0:3])    #输出前面的三位

print(players[-3:])    #输出最后三位的数据

print("Here are the first three players on my team: ")

for player in players[:3]:
    print(player.title())

#  # 复制列表

copy_players = players[:]

print("Copy players:\n"+str(copy_players))

# 此方法赋值列表 列表之间不存在包含的关系
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]


my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)

# 此方法是将两个变量  同时指向了 同一个列表
my_foods = ['pizza', 'falafel', 'carrot cake']
# #这行不通
friend_foods = my_foods
my_foods.append('cannoli')
friend_foods.append('ice cream')
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)


# =============元组
# ：：：Python将不能改变的值称为不可变的，而不可变的列表被称为元组

dimensions = (200,50)

dimensions[0] = 123   # 元组中的值不可修改

print(dimensions[0])

# 遍历元组中的所有值

for dimension in dimensions:
	print(dimension)

# 修改 元组变量
# 虽然不能修改元组的元素，但可以给存储的变量赋值
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)


dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)


# if 语句

# in  检查特定的值 是否包含在列表中


requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)

print('pepperoni' in requested_toppings)

#  not in  检查特定值是否 不包含在列表中
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
if user not in banned_users:
	print(user.title() + ", you can post a response if you wish.")

# 检查特殊元素
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
	print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

# 如果比萨店的青椒用完了， 该如何处理呢？ 
# 为妥善地处理这种情况， 可在for 循环中包含一条if 语句：
requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
for requested_topping in requested_toppings:
  if requested_topping == 'green peppers':
		print("Sorry, we are out of green peppers right now.")
  else:
		print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")

# 确定列表不是空的
requested_toppings = []
if requested_toppings:
	for requested_topping in requested_toppings:
		print("Adding " + requested_topping + ".")
		print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")

# 使用多个列表
# 定义了两个列表， 其中第一个列表包含比萨店供应的配料， 而第二个列表包含顾客点的配料。 
# 这次对于requested_toppings 中的每个元素， 都检查它是否是比萨店供应的配料，
# 再决定是否在比萨中添加它

available_toppings = ['mushrooms', 'olives', 'green peppers',
					'pepperoni', 'pineapple', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
 	if requested_topping in available_toppings:
	    print("Adding " + requested_topping + ".")
 	else:
	    print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")



# ====  字典 ===

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']

print("You just earned "+ str(new_points) + " Points!")

# ====添加键--值对

print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25

print(alien_0)

#  修改字典中的值

print("The alien is " + alien_0['color'] + ",")

alien_0['color'] = 'yellow'

print("The alien is now " + alien_0['color'] + ",")

# 根据判断进行赋值

alien_0 = {'x_position': 0,'y_position':25,'speed':'medium'}

print("Original x = position: " + str(alien_0['x_position']))

# # 向右移动外星人
# # 据外星人当前速度决定将其移动多远

if alien_0['speed'] == 'slow':
	x_increment = 1
elif alien_0['speed'] == 'medium':
	x_increment = 2
else:
	# 这个外星人的速度一定很快
	x_increment = 3

# # 新位置等于老位置加上增量
alien_0['x_position'] = alien_0['x_position'] + x_increment

print("New x = position :" + str(alien_0['x_position'])) 

# 删除键——值对

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

# # 删除后
del alien_0['points']
print(alien_0)

# 有类似对象组成的字典

favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'Python',
	}

print("Jen's favorite language is " + favorite_languages['jen'].title() + ".")

# 遍历字典
user_0 = {
	'username' : 'efermi',
	'first' : 'enrico',
	'last' : 'fermi',
	}

for key, value in user_0.items():
	print("\nKey:" + key)
	print("Value:" + value)

favorite_languages = {
	'jen' : 'python',
	'sarah' : 'c',
	'edward' : 'ruby',
	'phil' : 'Python',
	}

for name,language in favorite_languages.items():
	print(name.title() + "'s favorite language is " + language.title() + ".")

print("遍历字典中的所有键")

for name in favorite_languages.keys():
	print(name.title())
# 根据键获取指定的 值

friends = ['phil','sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		print(" Hi " + name.title() + ", I see your favorite language is " +
			favorite_languages[name].title() + "!" )

# 按顺序遍历字典中的所有键

# 按顺序遍历字典中的所有键
# 字典总是明确地记录键和值之间的关联关系， 但获取字典的元素时， 获取顺序是不可预测的。 
# 这不是问题， 因为通常你想要的只是获取与键相关联的正确的值。
# 要以特定的顺序返回元素， 一种办法是在for 循环中对返回的键进行排序。
#  为此， 可使用函数sorted() 来获得按特定顺序排列的键列表的副本
# 使用sorted() 用来为结果排序

for name in sorted(favorite_languages.keys()):
	print(name.title() + ",thank you for  taking the poil.")

# 遍历字典中的所有值

print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

# 处理值 中相同的内容  使用set集合用来给 结果去除 重复的值
# set集合中的值 不允许重复 ？？？？？
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

# 嵌套
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]
for alien in aliens:
	print(alien)

# # 创建一个用于储存外星人的空列表

aliens = []

# # 创建30个绿色的外星人
for alien_number in range(30):
	new_alien = {'color' : 'green' , 'points' : 5, 'speed' : 'slow'}
	aliens.append(new_alien)

# # 将前三个的数据修改一下
for alien in aliens[:3]:
	if alien['color'] == 'green':
		alien['color'] = 'yellow'
		alien['speed'] = 'medium'
		alien['points'] = 10


# # 显示前5个外星人
for alien in aliens[:5]:
	print(alien)
print("...")
# # 显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))


# 在字典中储存列表

# 储存所点披萨的信息

pizza = {
	'crust' : 'thick',
	'toppings' : ['mushrooms','extra cheese'],
}

# # 概述所点的披萨
print("You ordered a " + pizza['crust'] + "-crust pizza " 
	+ "with the following toppings:")

for topping in pizza['toppings']:
	print("\t" + topping)

favorite_languages = {
	'jen' : ['python', 'ruby'],
	'sarah' : ['c'],
	'edward' : ['ruby', 'go'],
	'phil' : ['python', 'haskell']
}

for name, languages in favorite_languages.items():
	print('\n' + name.title() + "'s favorite languages are :")
	for language in languages:
	 	print("\t" + language.title())

# 在字典中储存字典

users = {
	'arinstein' : {
		'first' : 'albert',
		'last' : 'einstein',
		'location' : 'princeton',
	},
	'mcurie' : {
		'first' : 'marie',
		'last' : 'curie',
		'location' : 'paris',
	},
}

for username, user_info in users.items():
	print("\nUsername:" + username)
	full_name = user_info['first'] + " " + user_info['last']
	location = user_info['location']

	print("\tfull name : " + full_name.title())
	print("\tLocation: " + location.title() )

# 第七章  用户输入和while循环
# ???? ？？？？？？？？？？？？？？？ 为什么使用input进行数据的获取 却没有相应的数据反应
height = input("How tall are you, in inches? ")
height = int(height)

if height >= 36:
	print("\nYou're tall enough to ride!")
else:
	print("\nYou'll be able to ride when you're a little order.")

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
	message = input(prompt)

	if message != 'quit':
		print(message)

# 使用标志

prompt = "\nTell me something, and I will reqeat it back to you："
prompt = "\nEnter 'quit' to end the program."

active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)

# 使用break退出循環

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
	city = input(prompt)

	if city == 'quit':
		break
	else:
		print("I'd love to go to " + city.title() + "!")


# 在循環中使用continue
# 要返回到循环开头， 并根据条件测试结果决定是否继续执行循环， 可使用continue 语句，
# 它不像break 语句那样不再执行余下的代码并退出整个循环
current_number = 0

while current_number < 10:
	current_number += 1
	if current_number % 2 == 0:
		continue

	print(current_number)


# 避免无线使用循环
x = 1
while x <= 5:
	print(x)
	x += 1

# 这个循环将没完没了地运行！
x = 1
while x <= 5:
	print(x)

# 使用while 循环来处理列表和字典

# 在列表之移动元素===============

# 首先，创建一个待验证用户列表
# 和一个用于储存已验证用户的空列表

unconfirmed_users = ['alice','brian','candace']
confirmed_users = []

# 验证每一个用户，直到没有为验证用户为止
# 将每个经过验证的列表都移动到已验证用户列表中
while unconfirmed_users:
	current_user = unconfirmed_users.pop()

	print("Verifying user: " + current_user.title()) 
	confirmed_users.append(current_user)

# 显示所有已验证的用户
print("\nThe following users have been confimed:")
for confirmed_user in confirmed_users:
	print(confirmed_user.title())

# ==================

# 刪除包含特定值的所有列表元素

pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)

# # 使用用户输入来填充字典

responses = {}

# # 设置一个标志，指出调查是否继续
polling_active = True

while polling_active:
	# 提示输入被调查的名字个和回答
	name = input("\nWhat is your name?")
	response = input("Which mountain would you like to climb someday?")

	# 将答卷储存在字典中
	responses[name] = response

	# 看看是否还有人要参与调查
	repeat = input("Would you like to let another person respond? (yes/no)")
	if repat == 'no':
		polling_active = False

# 调查结束，显示结果
print("\n=== Poll Results ===")
for name,response in response.items():
	print(name + " would like to climb " + response + ".")

# ++++++++++++++++++++++++++++++++++++++++++++函数

# 定义函数

def greet_user():
	"""显示简单的问候语"""
	print("Hello!")

greet_user()

# 向函数传递信息
def greet_user(username):
	"""显示简单的问候语"""
	print("Hello, " + username.title() + "!")

greet_user('zhang')


# 实参和形参
# 在函数greet_user() 的定义中， 变量username 是一个形参 ——函数完成其工作所需的一项信息。
# 在代码greet_user('jesse') 中， 值'jesse' 是一个实参 。
# 实参是调用函数时传递给函数的信息。 我们调用函数时， 将要让函数使用的信息放在括号内。
# 在greet_user('jesse') 中， 将实参'jesse' 传递给了函数greet_user() ， 这个值被存储在形参username 中。

def describe_pet(animal_type, pet_name):
	"""显示宠物的信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'harry')

# 调用函数多次
# 位置实参的顺序和重要

# 关键字实参
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# 默认值   默认值放在后边 放在前边会出现: SyntaxError: non-default argument follows default argument
def describe_pet(pet_name, animal_type='dog'):
	"""显示宠物的信息"""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet(pet_name='harry')

describe_pet(pet_name='hatty',animal_type='hamster')

#等效的函数调用

#一条名为Willie的小狗
describe_pet('Wille')
describe_pet(pet_name='willie')

# 一直名为Harry的仓鼠
describe_pet('harry','hamster')
describe_pet(pet_name='harry',animal_type='hamster')
describe_pet(animal_type='hamster',pet_name='harrt')

describe_pet()

# 返回值
def get_formatted_name(first_name,last_name):
	"""返回整洁的姓名"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi','hendrix')

print(musician)

# 让参数变成可选的
# 只要同时提供名、 中间名和姓， 这个函数就能正确地运行。 
# 它根据这三部分创建一个字符串， 在适当的地方加上空格， 并将结果转换为首字母大写格式：
def get_formatted_name(first_name,middl_name,last_name):
	"""返回整洁的姓名"""
	full_name = first_name + ' ' + middl_name + ' '+last_name
	return full_name.title()

musician = get_formatted_name('john','lee','hooker')
print(musician)

# 然而， 并非所有的人都有中间名， 但如果你调用这个函数时只提供了名和姓， 它将不能正确地运行。
# 为让中间名变成可选的， 可给实参middle_name 指定一个默认值——空字符串， 并在用户没有提供中间名时不使用这个实参。
# 为让get_formatted_name() 在没有提供中间名时依然可行， 可给实参middle_name 指定一个默认值——空字符串，
# 并将其移到形参列表的末尾

def get_formatted_name(first_name,last_name,middle_name=''):
	"""返回整洁的姓名"""
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

musician = get_formatted_name('jimi','hendrix')
print(musician)

musician = get_formatted_name('john','hooker','lee')
print(musician)

# 返回字典
# 函数可返回任何类型的值， 包括列表和字典等较复杂的数据结构。
# 例如， 下面的函数接受姓名的组成部分， 并返回一个表示人的字典：
def build_person(first_name,last_name):
	"""返回一个字典，其中包含有关一个人的信息"""
	person = {'frist': first_name,'last': last_name}
	return person

musician = build_person('jimi', 'hendrix')
print(musician)

# 结合使用函数和weile循环

def get_formatted_name(first_name, last_name):
	"""返回整洁的姓名"""
	full_name = first_name + ' ' + last_name
	return full_name.title()

while True:
	print("\nPlease tell me your name:")
	print("(enter 'q' at any time to quit)")

	f_name = input("First name:")
	if f_name == 'q':
		break

	l_name = input("Last name:")
	if l_name == 'q':
		break

	formatted_name = get_formatted_name(f_name,l_name)
	print("\nHello," + formatted_name + "!")

# =======传递列表===============
def greet_users(names):
	"""向列表中的每位用户都发出简单的问候"""
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

usernames = ['hannah','ty','margot']
greet_users(usernames)

# ==========在函数中修改列表===================★★★★★★★★★★★★★★

# ---------------------------------不使用函数进行》需要打印的设计存储在一个列表中， 打印后移到另一个列表中。
# 首先创建一个列表，其中包含一些要打印的设计
unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []

# 模拟打印每个设计，直到没有未打印的设计为止
# 打印每个设计后，都将其移动到列表completed_models中
# 列表的pop()方法，用户移除列中的数据(默认是最后一个)
while unprinted_designs:
	current_design = unprinted_designs.pop()

	# 模拟根据设计制作3D打印模型的过程
	print("Printing model: " + current_design)
	completed_models.append(current_design)

# 显示打印好的所有模型
print("\nThe following model have been printed:")
for completed_model in completed_models:
	print(completed_model)

# ===============使用函数进行编写
# 编写两个函数， 每个都做一件具体的工作。 大部分代码都与原来相同， 只是效率更高。 
# 第一个函数将负责处理打印设计的工作， 而第二个将概述打印了哪些设计：
def print_models(unprintes_designs,completed_models):
	"""
	模拟打印每个设计，直到没有未打印的设计为止
	打印每个设计后，都将其移到列表completed_models中
	"""
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		
		#模拟根据设计制作3D打印模型的过程
		print("Printing model: " + current_design)
		completed_models.append(current_design)

def show_completed_models(completed_models):
	"""显示打印好的所有模型"""
	print("\nThe following models have been printed:")
	for completed_model in completed_models:
		print(completed_model)


unprinted_designs = ['iphone case','robot pendant','dodecahedron']
completed_models = []


print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# ★★★★★★★★★★★★★禁止函数修改列表★★★★★★★★★★★★
# 如下只是将列表的副本传递给函数，副本在函数中的操作并不影响列表本身
function_name(list_name[:])     
print_models(unprinted_designs[:],completed_models)


# ★★★★★★★★★★★★★传递任意数量的实参★★★★★★★★★★★★

def make_pizze(*toppings):
	"""打印顾客的所有配料"""
	print(toppings)

make_pizze('pepperoni')
make_pizze('mushrooms','green peppers','extra cheese')


# ★★★★★★★★★★★★结合使用位置实参和任意数量实参★★★★★★★★★★★★

def make_pizza(size,*toppings):
	"""概述要制作的披萨"""
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings:")
	for topping in toppings:
		print("-" + topping)

make_pizza(16,'pepperoni')
make_pizza(12,'mushrooms','green peppers','extra cheese')



# ★★★★★★★★★★★★使用任意数量的关键字实参★★★★★★★★★★★★

def build_profile(first,last,**user_info):
	"""创建一个字典，其中包含我们知道的有关用户的一切"""
	profile = {}
	profile['first_name'] = first
	profile['last_name'] = last
	for key,value in user_info.items():
		profile[key] = value
	return profile

user_info = build_profile('albert', 'einstein',lacation='princetion',field='physics')

print(user_info)


# ★★★★★★★★★★★★将函数存储在模块中★★★★★★★★★★★
# 1.导入整个模块     
				import pizza

# 2.导入特定的函数  
				from module_name import function_name
				from module_name import function_0,function_1,function_2

# 使用as给函数指定别名
					from module_name inport funciton_name as f_name

# 导入模块中的所有函数
					from module_name import *


# *************************第九章   类******************

# 创建Dog类   ------------着重注意 init  两边的下划线都是两个 一个的话会报  TypeError: object() takes no parameters
class Dog():
# 	"""一次模拟小欧股的简单尝试"""

	def __init__(self,name,age):
		"""初始化属性name和age"""
		self.name  = name
		self.age = age

	def sit(self):
		"""模拟小狗被命令时蹲下"""
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		"""模拟小狗被命令时打滚"""
		print(self.name.title() + " rolled over!")


# 根据类创建实例
my_dog = Dog('willie','1')

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")

# 访问属性    my_dog.name

# 调用方法

my_dog.sit()
my_dog.roll_over()

# 创建多个实例

your_dog = Dog('lucy', 3)
print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog is " + str(your_dog.age) + " years old.")
your_dog.sit()


# ******************使用类和实例

class Car():
	"""一次模拟汽车的简单尝试"""
	def __init__(self, make, model, year):
		"""初始化描述汽车的属性"""
		self.make = make
		self.model = model
		self.year = year

	def get_descriptive_name(self):
		"""返回整洁的描述性信息"""
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())

# 给属性设定默认值
class Car():
		def __init__(self, make, model, year):
			"""初始化描述汽车的属性"""
			self.make = make
			self.model = model
			self.year = year
			self.odometer_reading = 0

		def update_odometer(self,mileage):
			"""将里程表读取数设置为指定的值"""
			self.odometer_reading = mileage
		
		#较为严谨的改变属性值的方法
		def update_odometer(self, mileage):
			"""
			将里程表读数设置为指定的值
			禁止将里程表读数往回调
			"""
			if mileage >= self.odometer_reading:
				self.odometer_reading = mileage
			else:
				print("You can't roll back an odometer!")

		def increment_odometer(self,miles):
			"""将里程表读数增加指定的量"""
			self.odometer_reading += miles

		def get_descriptive_name(self):
			"""返回整洁的描述性信息"""
			long_name = str(self.year) + ' ' + self.make + ' ' + self.model
			return long_name.title()

		def read_odometer(self):
			"""打印一条指出汽车里程的消息"""
			print("This car has " + str(self.odometer_reading) + " miles on it.")

		

my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

# 修改属性值

# 1.直接修改属性的值
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
# 2.通过方法修改属性的值
my_new_car.update_odometer(-1)
my_new_car.read_odometer()

# 3.通过方法对属性的值进行递增
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive_name())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()


# *******************继承

# 1.子类的方法 __init__()

class ElectricCar(Car):
	"""电动汽车的独特之处"""
	def __init__(self,make,model,year):
		"""初始化父类的属性"""
		super().__init__(make,model,year)
		# super(ElectricCar, self).__init__(make, model, year)   python2.7中的继承

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())

# ///////////////////给子类定义属性和方法

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	
	def __init__(self, make, model, year):
		"""
		电动汽车的独特之处
		初始化父类的属性， 再初始化电动汽车特有的属性
		"""
		super().__init__(make, model, year)
		self.battery_size = 70

	def describe_battery(self):
		"""打印一条描述电瓶容量的消息"""
		print("This car has a " + str(self.battery_size) + "-kWh battery.")

	# 重写父类的方法
	def fill_gas_tank():
		"""电动汽车没有油箱"""
		print("This car doesn't need a gas tank!")


my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()


# ……………………………………………………………将实例用作属性…………………………………………………………
class Battery():
		"""一次模拟电动汽车电瓶的简单尝试"""

		def __init__(self, battery_size=70):
			"""初始化电瓶的属性"""
			self.battery_size = battery_size

		def describe_battery(self):
			"""打印一条描述电瓶容量的消息"""
			print("This car has a " + str(self.battery_size) + "-kWh battery.")

class ElectricCar(Car):
	"""Represent aspects of a car, specific to electric vehicles."""
	
	def __init__(self, make, model, year):
		"""
		电动汽车的独特之处
		初始化父类的属性， 再初始化电动汽车特有的属性
		"""
		super().__init__(make, model, year)
		self.battery = Battery()


my_tesla = ElectricCar('tesla','model s',2016)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()


# @@@@@@@@@@@@@@@@@@@第十章  文件和异常 @@@@@@@@@@@@@@@@@@@@

# 关键字with 不在需要访问文件后将其关闭
# 此为通过先对路径进行查找
with open('pi_disits.txt') as file_object:
	contents = file_object.read()
	print(contents)

# 绝对路径通常比相对路经长，因此将其存储在一个变量中
file_path = 'G:\PythonSpace\Test\pi_disits.txt'
with open(file_path) as file_object:
	contents = file_object.read()
	print(contents)


#     逐行读取
Python rstrip() 删除 string 字符串末尾的指定字符（默认为空格）.
filename = 'pi_disits.txt'
with open(filename) as file_object:
	for line in file_object:
		print(line.rstrip())

# 创建一个包含文件各行内容的列表
filename = 'pi_disits.txt'
with open(filename) as file_object:
		lines = file_object.readlines()

for line in lines:
	print(line.rstrip())


#>>>>>>>>>>使用文件的内容
filename = 'pi_disits.txt'
with open(filename) as file_object:
		lines = file_object.readlines()

pi_string = ''

for line in lines:
	pi_string += line.strip()

# # 包含原来位于每行左边的空格， 为删除这些空格， 可使用strip() 而不是rstrip() ：
print(pi_string)
print(len(pi_string))


# >>>>>>>>>>>包含一百位的大型文件   只需改变读取的文件就可以了
filename = 'pi_disits.txt'
with open(filename) as file_object:
		lines = file_object.readlines()

pi_string = ''

for line in lines:
	pi_string += line.strip()

# # 为防止控制台一直翻滚  只截取前50位进行输出显示
print(pi_string[:52] + "...")  
print(len(pi_string))

# 圆周率包含你的生日吗？

# pi_million_digits.txt 包含一百万位的文件
fliename = 'pi_million_digits.txt'

with open(filename) as file_object:
	lines = file_object.readines()

pi_sting = ''
for line in lines:
	pi_string += line.rstrip()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
	print("Your birthday appears in the first million digits of pi!")
else:
	print("Your birthday does not appear in the first million digits of pi.")


# 可使用方法replace() 将字符串中的特定单词都替换为另一个单词。???????
message = "I really like dogs."
message.replace('dogs','cat')
print(message)

# 数据可视化

# >>>>>>>>绘制简单的折线图

import matplotlib.pyplot as plt

squares = [1,4,9,16,25]
plt.plot(squares)
plt.show()

#  10.2   写入文件
# 打开文件时， 
# 可指定读取模式 （'r' ） 、 写入模式 （'w' ） 、 附加模式 （'a' ） 
# 或让你能够读取和写入文件的模式（'r+' ） 。
# 如果你省略了模式实参， Python将以默认的只读模式打开文件。

filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming")

# >>>>>>>>>>>写入多行


filename = 'programming.txt'

with open(filename, 'w') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")


# >>>>>>>>>>>附加到文件

filename = 'programming.txt'

with open(filename, 'a') as file_object:
	file_object.write("I love programming.\n")
	file_object.write("I love creating new games.\n")

# >>>>>>>>>10.3   异常
# Python使用被称为异常 的特殊对象来管理程序执行期间发生的错误。
# 每当发生让Python不知所措的错误时， 它都会创建一个异常对象。 
# 如果你编写了处理该异常的代码， 程序将继续运行；
# 如果你未对异常进行处理， 程序将停止， 并显示一个traceback， 其中包含有关异常的报告。

#  10.3.1  处理ZeroDivisionError异常

print(5/0)
# 10.3.2  使用try-except代码块
try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

# >>>>>>>>>>>>>使用异常避免崩溃

print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number：")
	if second_number == 'q':
		break
	answer = int(first_number)/int(second_number)
	print(answer)

# >>>>>>>>>>>>else 代码块
print("Give me two numbers and I'll divide them.")
print("Enter 'q' to quit.")

while True:
	first_number = input("\nFirst number: ")
	if first_number == 'q':
		break
	second_number = input("Second number：")
	try:
		answer = int(first_number)/int(second_number)
	except ZeroDivisionError:
		print("You can't drivide by 0 !")
	else:
		print(answer)

# >>>>>>>处理FileNotFoundErrot异常
filename = 'alice.txt'

# FileNotFoundError: [Errno 2] No such file or directory: 'alice.txt'
with open(filename) as f_obj:
	contents = f_obj.read()


filename = 'alice.txt'
try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file " + filename + " does not exist."
	print(msg)

# >>>>>>>>>>>>>>10.3.6  分析文本
"""
Test 
"""
title = "Alice in wonderland"
print(title.split())

#确定文件中包含多少个单词 
filename = 'programming.txt'

try:
	with open(filename) as f_obj:
		contents = f_obj.read()
except FilenotFoundError:
	msg = "Sorry the file " + filename + " does not exist."
	print(msg)
else:
	# 计算文件大致包含多少个单词
	words = contents.split()
	num_words = len(words)
	print("The file " + filename + " has about " + str(num_words) + " words.")



# >>>>>>>>>>>>>>>>>>>使用多个文件

def count_words(filename):
	"""计算一个文件大致包含多少个单词"""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		msg = "Sorry the file " + filename + " does not exist."
		print(msg)
	else:
		# 计算大致包含多少个单词
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filename = 'alice.txt'
count_words(filename)


# >>>>>>>>>>失败时一声不吭

def count_words(filename):
	"""计算一个文件大致包含多少个单词"""
	try:
		with open(filename) as f_obj:
			contents = f_obj.read()
	except FileNotFoundError:
		pass
	else:
		# 计算大致包含多少个单词
		words = contents.split()
		num_words = len(words)
		print("The file " + filename + " has about " + str(num_words) + " words.")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_words(filename)

# >>>>>>>>>>>>>>>10.3.9  决定报告哪些错误



# >>>>>>>>>>>>>>>>存储数据

# JSON（JavaScript Object Notation） 格式最初是为JavaScript开发的，
# 但随后成了一种常见格式，被包括Python在内的众多语言采用

# <<<<<<<<<<<<<<<<<<10.4.1 使用json.dump() 和json.load()

# 第一个程序将使用json.dump() 来存储这组数字，
# 而第二个程序将使用json.load() 。
# 函数json.dump() 接受两个实参： 要存储的数据以及可用于存储数据的文件对象。 


import json

numbers = [2,3,5,6,11,13]

filename = 'numbers.json'
with open(filename,'w') as f_obj:
	json.dump(numbers, f_obj)


# 使用json.load() 将这个列表读取到内存中

import json

filename = 'numbers.json'
with open(filename) as f_obj:
	numbers = json.load(f_obj)

print(numbers)


# >>>>>>>>10.4.2   保存和读取用户生成的数据

#  先存储用户的名字
import json

username = input("What is your name？")

filename = 'username.json'
with open(filename,'w') as f_obj:
	json.dump(username,f_obj)
	print("We'll remember you when you come back, " + username + "!")

# 在编写一个程序，向其名字被储存的用户发出问候

import json

filename = 'username.json'

with open(filename) as f_obj:
	username = json.load(f_obj)
	print("Welcome back, " + username + "!")


# 将存储和输出 写为一个程序
# 我们需要将这两个程序合并到一个程序（remember_me.py） 中。 
# 这个程序运行时， 我们将尝试从文件username.json中获取用户名， 
# 因此我们首先编写一个尝试恢复用户名的try 代码块。 
# 如果这个文件不存在， 我们就在except 代码块中提示用户输入用户名，
 # 并将其存储在username.json中， 以便程序再次运行时能够获取它：

import json

# # 如果以前存储了用户名，就加载他
# # 否则，就提示用户输入用户名并存储它

# filename = 'usernamess.json'

# try:
# 	with open(filename) as f_obj:
# 		username = json.load(f_obj)
# except:
# 	username = input("What is your name?")
# 	with open(filename,'w') as f_obj:
# 		json.dump(username,f_obj)
# 		print("We'll remember you when you come back, " + username + "!")
# else:
# 	print("Welcome back, " + username + "!")



# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html)
# for link in bsObj.findAll("a"):
# 	if 'href' in link.attrs:
# 		print(link.attrs['href'])



# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# s = ''
# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html)
# for link in bsObj.findAll("a"):
# 	if 'href' in link.attrs:
#  		s += link.attrs['href'] + '\n'


# filename = 'programming.txt'

# with open(filename, 'w') as file_object:
# 	file_object.write(s)失败时一声不吭






# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def index():
# 	return '<h1>Hello World!</h1>'

# if __name__ == '__main__':
# 	app.run(debug=True)

numbers = ['1','2','3','4']
print(numbers)
#删除指定位置的元素
del numbers[0]
print(numbers)