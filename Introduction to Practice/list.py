# _*_ coding:utf-8 _*_
# L1 = ['Hello', 'World', 18, 'Apple', None]
# # obtain string and lower
# L2 = [x.lower() for x in L1 if isinstance(x, str)]
# print(L2)
# # test
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')

# bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# print(bicycles)  # 输出包含方括号
# # 访问list元素
# print(bicycles[0])  # 输出某个索引位置处的元素，从0开始
# print(bicycles[-1])  # -1 代表最后一个元素，以此类推
#
# # 修改、添加和删除元素
# # 修改
# bicycles[0] = 'ducati'  # 修改索引处的元素
# print(bicycles)
#
# # 添加
# bicycles.append('yamaha')  # 在list末尾添加元素
# print(bicycles)
# bicycles.insert(0, 'trek')  # 在索引处插入新元素
# print(bicycles)
#
# # 删除
# del bicycles[0]  # del语句，删除索引处的元素，且无法再访问
# print(bicycles)
#
# # bicycles.pop()  # pop()弹出最后一个元素,且能继续使用这个元素
# popped_bicycles = bicycles.pop(0)  # 可弹任意索引处的元素
# print(bicycles)
# print(popped_bicycles)
#
# bicycles.remove('yamaha')  # remove()移除第一个指定的值
# print(bicycles)

# 排序
# cars = ['bmw', 'audi', 'toyoda', 'subaru']
# cars.sort()  # sort()永久排序，相反排序：reverse = ture
# print(cars)

# cars = ['bmw', 'audi', 'toyoda', 'subaru']
# print("Here is the original list: ")
# print(cars)
#
# print("\nHere is the sorted list: ")
# print(sorted(cars))  # 函数sorted()临时排序，不改变原有顺序
#
# print("\nHere is the original list again: ")
# print(cars)

cars = ['bmw', 'audi', 'toyoda', 'subaru']
print(cars)
cars.reverse()  # reverse()按list顺序反转, 前面是按字母顺序
print(cars)

print(len(cars))   # len()获取list长度
