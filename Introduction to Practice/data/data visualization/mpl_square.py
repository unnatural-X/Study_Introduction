# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/12/10
"""
import matplotlib.pyplot as plt  # 导入pyplot模块，并指定别名为plt

input_value = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
fig, ax = plt.subplots()  # 调用subplots()函数，可在图中绘制多个图表;fig生成一张图片
ax.plot(squares, label='LineWidth=0.5')  # 绘制图表，无横坐标默认从0开始
ax.plot(input_value, squares, linewidth=4, label='LineWidth=3')

# 设置图表标题并给坐标轴加上标签
ax.set_title("Square", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square", fontsize=14)
# plt.axis([0, 6, 0, 30])  # 坐标轴范围
# 设置刻度标记的大小
ax.tick_params(axis='both', labelsize=14)
plt.legend()  # 显示前面的label
plt.savefig("square_plot.png", bbox_inches='tight')  # 保存图片
plt.show()

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]


plt.figure()
plt.plot(x_values, y_values, linewidth=4, label='square')

# 设置图表标题并给坐标轴加上标签
plt.title("Square", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square", fontsize=14)
plt.legend()
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.show()  # 显示图表

yy_values = [x**3 for x in x_values]

plt.figure()
plt.plot(x_values, yy_values, linewidth=4, label='Cubic')

# 设置图表标题并给坐标轴加上标签
plt.title("Cubic", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cubic", fontsize=14)
plt.legend(frameon=False)  # 去除图例框
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig('Cubic_plot.png', bbox_inches='tight')
plt.show()  # 显示图表
