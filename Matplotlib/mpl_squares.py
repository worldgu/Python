import matplotlib.pyplot as plt

# 绘制简单的折线图
# squares = [1, 4, 9, 16, 25]
# plt.plot(squares)

# # plt.plot() 打开matplotlib查看器， 并显示绘制的图形
# plt.show()

# 修改标签文字和线条粗细

input_values = [1, 2, 3, 4, 5, 6]
squares = [1, 4, 9, 16, 25,1]
# 线的粗细
# plt.plot(squares, linewidth = 5)    图形不够准确

plt.plot(input_values, squares, linewidth = 5)

# 设置图标标题， 并给坐标轴 加上标签
plt.title("Square numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize = 14)

# 设置可读标记的大小
plt.tick_params(axis = 'both', labelsize = 14)

plt.show()