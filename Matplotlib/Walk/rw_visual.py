import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个RandomWalk实例， 并将其包含的点都绘制出来
# rw = RandomWalk()
# rw.fill_walk()
# plt.scatter(rw.x_values, rw.y_values, s = 15)
# plt.show()
# 模拟多次随机漫步

# 只要成语处于活动状态，就不断地模拟随机漫步
# while True:
# 	# 创建一个RandomWalk实例， 并将其包含的点都绘制出来
# 	rw = RandomWalk()
# 	rw.fill_walk()
# 	plt.scatter(rw.x_values, rw.y_values,s=15)
# 	plt.show()

# 	keep_running = input("Make another Walk? (y/n):")
# 	if keep_running == 'n':
# 		break

# 设置随机漫步图的样式

# 给点着色
# 我们将使用颜色映射来指出漫步中各点的先后顺序， 并删除每个点的黑色轮廓， 让它们的颜色更明显。 
# 为根据漫步中各点的先后顺序进行着色， 我们传递参数c ， 并将其设置为一个列表， 其中包含各点的先后顺序。
#  由于这些点是按顺序绘制的， 因此给参数c 指定的列表只需包含数字1~5000

while True:
	# 创建一个RandomWalk实例， 并将其包含的点都绘制出来\
	# 增加点数
	rw = RandomWalk(50000)
	rw.fill_walk()


	# 设置绘图窗口的尺寸
	# 函数figure() 用于指定图表的宽度、 高度、 分辨率和背景色   单位为英寸
	# 如果你知道自己的系统的分辨率， 可使用形参dpi 向figure() 传递该分辨率
	plt.figure(dpi=999, figsize=(10, 6))

	point_numbers = list(range(rw.number_points))
	plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor = 'none',s=1)

	# 突出起点和终点
	plt.scatter(0, 0, c = 'green',edgecolor = 'none' , s = 100)
	plt.scatter(rw.x_values[-1],rw.y_values[-1], c='red', edgecolor='none',s=100)


	# 隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	plt.show()

	keep_running = input("Make another Walk? (y/n):")
	if keep_running == 'n':
		break