# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/12/10
"""
import matplotlib.pyplot as plt

# 画散点图
x0_values = [1, 2, 3, 4, 5]
y0_values = [1, 4, 9, 16, 25]

plt.figure()
plt.scatter(x0_values, y0_values, s=100)


x_values = range(1, 1001, 1)
y_values = [x**2 for x in x_values]
# 设置图表标题并给坐标轴加上标签
plt.title("Square", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square", fontsize=14)
# plt.axis([0, 6, 0, 30])  # 坐标轴范围
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig("scatter_plot.png")
plt.show()

plt.figure()
plt.scatter(x_values, y_values, s=10)

# 设置图表标题并给坐标轴加上标签
plt.title("Square", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square", fontsize=14)
# plt.axis([0, 1100, 0, 1100000])
# 设置刻度标记的大小
plt.tick_params(axis='both', labelsize=14)

plt.savefig("square_plot.png", bbox_inches='tight')
plt.show()  # 显示图表
