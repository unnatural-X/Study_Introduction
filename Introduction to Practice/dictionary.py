# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/11/28
"""
# alien_0 = {'color': 'green', 'points': 5}  # 键值对
# print(alien_0)
# print(alien_0['color'])  # 访问字典中的值
# # 添加键值对
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)
# # 修改字典中的值
# alien_0['color'] = 'yellow'
# print(alien_0['color'])  # 访问修改后的值
# # 删除键值对
# del alien_0['color']  # del语句永久性地删除键值对
# print(alien_0)

# 存储众多对象地同一种信息
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
# language = favorite_languages['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# .get()取值
# alien_0 = {'color': 'green', 'speed': 'slow'}
# color_value = alien_0['color']
# print(color_value)
# point_value = alien_0.get('points')  # .get()访问不存在的键不会出错,返回值为None
# print(point_value)

# 遍历字典所有键值对
# favorite_languages = {
#     'jen': 'python',
#     'sarah': 'c',
#     'edward': 'ruby',
#     'phil': 'python'
# }
# for name, language in favorite_languages.items():
#     print(f"{name.title()}'s favorite language is {language.title()}")

# 遍历所有键
# for name in favorite_languages.keys():  # .keys()返回一个所有键的list
#     print(name.title())
# for name in sorted(favorite_languages.keys()):  # 排序输出
#     print(name.title())

# 遍历所有值
# for language in favorite_languages.values():
#     print(language.title())
# for language in set(favorite_languages.values()):  # .set()剔除重复元素，生成集合
#     print(language.title())

# 字典和列表嵌套
# # 列表中的元素为字典
# alien_0 = {'color': 'green', 'points': 5}
# alien_1 = {'color': 'blue', 'points': 6}
# alien_2 = {'color': 'black', 'points': 7}
# aliens = [alien_0, alien_1, alien_2]
# for alien in aliens:
#     print(alien)

# 字典中的值为列表
# favorite_languages = {
#     'jen': ['python', 'c'],
#     'sarah': ['c', 'c++'],
#     'edward': ['ruby', 'java'],
#     'phil': ['python', 'c']
# }
# for name, language in favorite_languages.items():
#     print(name)
#     print(language)

# 字典与字典嵌套
persons = {
    'mary': {'gender': 'female', 'age': '18'},
    'daniel': {'gender': 'male', 'age': '18'},
    'wall': {'gender': 'male', 'age': '18'}
}
for name, info in persons.items():
    print(name)
    print(info)
