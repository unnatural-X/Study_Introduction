# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/12/03
"""
import json

# 读取整个文件
# with open('pi_digits.txt') as file_object:  # 函数open()接受一个参数(当前目录下文件的名称)
#     # 若和.py文件不在一个目录下，使用相对或绝对文件路径
#     # 返回一个表示文件的对象，赋给file_object；无需考虑关闭，python会在合适的时候自动将其关闭
#     content = file_object.read()  # 利用方法read()读取全部内容
# print(content)

# 逐行读取
# filename = 'pi_digits.txt'
#
# with open(filename) as file_object:
#     for line in file_object:
#         # print(line)
#         print(line.rstrip())  # 去除多余的空白行

# 创建一个包含文件各行的列表
# filename = 'pi_digits.txt'
#
# with open(filename) as file_object:  # open返回的文件对象file_object只在with 代码块内可用
#     lines = file_object.readlines()  # 使用list存储文本内容便于后面使用
#
# for line in lines:
#     print(line.rstrip())
#
# # 使用文件的内容
# pi_string = ''
# for line in lines:
#     pi_string += line.rstrip()
#
# print(pi_string)
# print(len(pi_string))

# -----------------------------------------------------------------------------------------------
# 写入文件
# file_name = 'programming.text'

# with open(file_name, 'w') as file_object:
    # 'w'以写入模式打开文件；‘r’: 读取模式；‘a’ 附加模式；‘r+’ 读写模式；省略模式实参：读取模式
    # file_object.write("I love programming.")  # 只能写入字符串，其他数据类型需转换
    # 在文本中写入内容，如文本不存在，则新建文本；如文本存在，先清空已有内容再写入
    # file_object.write("I love creating new games.")  # write()在写入多行时不会自动添加换行符

    # 写入多行，需在字符串末尾添加换行符
    # file_object.write("I love programming.\n")
    # file_object.write("I love creating new games.\n")  # 还可以用空格、制表符和空行等设置内容格式

# -----------------------------------------------------------------------------------------------
# 附加文件
# file_name = 'programming.text'
#
# with open(file_name, 'a') as file_object:
#     file_object.write("I also love finding meaning in large datasets.\n")  # 在附加模式下写入的内容会附加于文件末尾
#     file_object.write("I love creating apps that can run on a browser.\n")  # 不会覆盖文件的内容

# 存储数据
# numbers = [2, 3, 4, 5, 6, 7]
#
# filename = 'numbers.json'  # 存储数据的文件名
# with open(filename, 'w') as f:  # 以写入模式打开文件
#     json.dump(numbers, f)  # 将数字列表写入文件numbers.json中

# 读取数据
filename = 'numbers.json'

with open(filename, 'r') as f:
    numbers = json.load(f)

print(numbers)
