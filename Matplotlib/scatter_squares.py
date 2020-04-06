import matplotlib.pyplot as plt
# 使用scatter()  绘制散点图 并设置其样式


x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# edgecolor = 'none' 删除数据点的轮廓
# c = 'red' 或者使用GBK进行设置 c = (0, 0, 0.8) 设置点的颜色

# plt.scatter(x_values, y_values, c = (0, 0, 0.8), edgecolor = 'none', s =40)

# 模块pyplot 内置了一组颜色映射。 要使用这些颜色映射， 
# 你需要告诉pyplot 该如何设置数据集中每个点的颜色。
# 下面演示了如何根据每个点的 y 值来设置其颜色：
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues, edgecolor = 'none', s =40)


# 这个点表较好
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]

# plt.scatter(x_values, y_values, s =100)

# plt.scatter(2, 4, s=200)  单点  并设置大小

# 设置标题斌人给坐标轴加上标签
plt.title("Square Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# 设置刻度标记的大小
plt.tick_params(axis = 'both',which = 'major', labelsize = 14)

# plt.show()
# 自动保存图标  将plt.show() 的调用替换为对 plt.savefig()  的调用
# bbox_inches = 'tight' 第二个参数  指定将图标杜宇的空白区域裁剪掉 不想裁剪 不写第二个参数即可
# show  在前  再执行savefig  保存的图片好像没有图片？？？
# plt.savefig('sauares_plot.png', bbox_inches = 'tight')