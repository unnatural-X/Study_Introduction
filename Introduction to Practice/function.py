# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/12/01
"""
# function的结构
# def greet_user(username):  # 定义：关键字def, 函数名及其形参
#     """显示简单的问候语"""  # 文档字符串注释, 紧跟定义
#     print(f"Hello,{username.title()}!")  # 函数体
#
#
# greet_user('jesse')  # 函数调用，函数名加与形参对应的实参

# 传递实参
# def describe_pet(animal_type, pet_name):
#     """显示宠物的信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"\nMy {animal_type}'s name is {pet_name.title()}")
#
#
# describe_pet('hamster', 'harry')  # 位置实参, 与顺序有关
# describe_pet('hamster', pet_name='harry')  # 位置形参位于关键字形参之前
# describe_pet(animal_type='hamster', pet_name='harry')  # 关键字实参，与顺序无关
# describe_pet(pet_name='harry', animal_type='hamster')

# 设置形参默认值，简化函数调用
# def describe_pet(pet_name, animal_type='dog'):  # 设置animal_type默认值(当dog较多时), 默认值形参位于末尾
#     """显示宠物的信息"""
#     print(f"\nI have a {animal_type}.")
#     print(f"\nMy {animal_type}'s name is {pet_name.title()}.")
#
#
# # describe_pet('harry')  # 位置形参调用，可省略animal_type形参
# # describe_pet(pet_name='harry')  # 关键字实参调用，可省略animal_type形参
#
# describe_pet('willie', 'cat')  # 给animal_type提供实参，会覆盖默认值
# describe_pet('willie', animal_type='cat')  # 位置形参位于关键字形参之前
# describe_pet(pet_name='willie', animal_type='cat')

# --------------------------------------------------------------------------------
# 进行数据处理并返回值(任何类型的值)
# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# musician = get_formatted_name('jimi', 'hendrix')
# print(musician)

# 使用空默认值让实参可选
# def get_formatted_name(first_name, last_name, middle_name=''):
#     """返回整洁的姓名"""
#     if middle_name:  # middle_name非空为真
#         full_name = f"{first_name} {middle_name} {last_name}"
#     else:
#         full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# basketball_player = get_formatted_name('jimmy', 'bultler')
# soccer_player = get_formatted_name('messi', 'lionel')
# print(basketball_player)
# print(soccer_player)

# 返回字典
# def build_person(first_name, last_name, age=None):
#     """返回一个字典，包含一个人的有关信息"""
#     person = {'first': first_name, 'last': last_name}
#     if age:
#         person['age'] = age
#     return person
#
#
# # basketball_player = build_person('jimmy', 'bultler')
# basketball_player = build_person('jimmy', 'bultler', 28)
# print(basketball_player)

# 结合函数和while循环
# def get_formatted_name(first_name, last_name):
#     """返回整洁的姓名"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title()
#
#
# while True:  # 无限循环
#     print("\nPlease tell me your name.")
#     print("(enter 'q' at any time to quit)")
#
#     f_name = input("Your first name: ")
#     if f_name == 'q':  # 输入q退出循环
#         break
#     l_name = input("Your last name: ")
#     if l_name == 'q':  # 输入q退出循环
#         break
#     formatted_name = get_formatted_name(f_name, l_name)  # while循环里面调用get_formatted_name函数
#     print(f"\nHello, {formatted_name}")

# 传递列表
# def print_models(unprinted_designs, completed_models):
#     """
#     模拟每个打印，直到没有未打印的设计为止
#     打印每个设计后，都将其移至列表completed_models中
#     """
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing design: {current_design}")
#         completed_models.append(current_design)
#
#
# def show_completed_models(completed_models):
#     """显示所有打印好的模型"""
#     print("\nThe following models have been printed:")
#     for completed_model in completed_models:
#         print(completed_model)
#
#
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
#
# # print_models(unprinted_designs, completed_models)  # 打印模型
# print_models(unprinted_designs[:], completed_models)  # 打印模型, 利用切片复制列表调用，不会改变原列表
# show_completed_models(completed_models)  # 显示已打印模型
#
# print(unprinted_designs)

# ---------------------------------------------------------------------------
# 传递任意数量的实参
# def make_pizza(*toppings):  # *toppings生成名为toppings的空元组，用以存储所有接收到的实参
#     """概述要制作的披萨"""
#     print("\nMaking a pizza with the following toppings:")
#     print(toppings)  # toppings 是元组
#     for topping in toppings:
#         print(f"- {topping}")
#
#
# make_pizza('pepperoni')
# make_pizza('mushrooms', 'green peppers', 'extra cheese')

# 结合使用位置形参和任意数量形参
# def make_pizza(size, *toppings):  # 同样位置形参放在最前面
#     """概述要制作的披萨"""
#     print(f"\nMaking a {size}-inch pizza with the following toppings:")
#     print(toppings)  # toppings 是元组
#     for topping in toppings:
#         print(f"- {topping}")
#
#
# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

# 使用任意数量的关键字形参
# def build_profile(first, last, **user_info):  # 创建一个名为user_info的空字典，用以存储所有接受的名称值对
#     """创建一个字典，包含我们知道的有关用户的一切"""
#     user_info['first_name'] = first
#     user_info['last_name'] = last
#     return user_info
#
#
# user_profile = build_profile('albert', 'einstein', location='princeton', field='physics')
# # 先将关键词实参存储到user_info中，再存储名字
# print(user_profile)

