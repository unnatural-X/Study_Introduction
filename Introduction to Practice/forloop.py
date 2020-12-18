# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/11/27
"""
# for 循环
# 注意for末尾的冒号和缩进
# magicians = ['alice', 'david', 'tom']
# for magician in magicians:
#     print(f'{magician.title()}, that was a great trick.')
#     print(f"I can't wait to see your next trick, {magician.title()}.\n")
# print('Thank you, that was a great magic show!')

#  利用for循环创建list
#  range()函数和list()函数
# squares = []  # 空列表
# for value in range(1, 5):  # range()不包括最后一个值
#     square = value ** 2
#     squares.append(square)
# print(squares)

#  列表解析
#  注意与上一种由空列表创建list的区别
# squares = [value ** 2 for value in range(1, 5)]
# print(squares)

# 最值和求和等简单操作
# print(max(squares))
# print(min(squares))
# print(sum(squares))

# list切片
# squares = [value ** 2 for value in range(1, 5)]
# print("Here are the first three number in the list； ")
# for square in squares[0:3]:  # 设置正确的索引
#     print(square)

# list复制
squares = [value ** 2 for value in range(1, 5)]
copy_squares1 = squares[:]  # 用切片复制生成两个不同的list
# 检查
squares.append(25)
copy_squares1.append(36)
print(squares)
print(copy_squares1)

copy_squares2 = squares  # 直接拿list名称幅值，两个名称指向同一个list
squares.append(25)
copy_squares2.append(36)
print(squares)
print(copy_squares2)
