# -*- coding:utf-8 -*-
"""
Editor: Daniel Xu
Date:20201210
"""
from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

die = Die()  # 创建一个D6

results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 统计各个点数出现的数目
frequencies = []
for value in range(1,die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# print(frequencies)

# 使用plotly来分析结果绘制直方图，对结果可视化
x_values = list(range(1, die.num_sides+1))
data = [Bar(x=x_values, y=frequencies)]  # 用Bar类生产直方图的数据集

x_axis_config = {'title': '点数'}
y_axis_config = {'title': '点数的频率'}  # 以字典元素配置坐标轴
my_layout = Layout(title='掷一个D6 1000次的结果', xaxis=x_axis_config, yaxis=y_axis_config)  # 返回一个指定图表布局和配置的对象

offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')  # 包含数据和布局对象的字典(绘制直方图)，文件名(存储地址)

