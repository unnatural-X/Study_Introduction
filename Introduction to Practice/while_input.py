# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/11/30
"""
# Input
# 指定清晰的提示引导用户输入
# prompt = 'If you tell us who you are, we can personalize the messages you are'
# prompt += '\nWhat is your first name? '  # 当提示过长可将提示赋予一个变量
#
# name = input(prompt)  # input的输入为字符串
# print(f"Hello, {name.title()}!")

# 利用int()获取数字输入
# height = input("How tall are you in inches? ")
# height = int(height)
#
# if height >= 48:
#     print("\nYou're tall enough to ride!")
# else:
#     print("\nYou'll be able to ride when you're a little older.")
# ----------------------------------------------------------------------------
# While循环
# current_number = 1
# while current_number <= 5:
#     print(current_number)
#     current_number += 1  # 如遗漏此句会造成无线循环，Ctrl+C可关闭

# 利用flag(特别是导致循环结束的因素很多时尤为有用)
# prompt = "\nTell me something, and I will repeat it back to you."
# prompt += "\nEnter 'quit' to end this program."
# active = True  # flag
# while active:
#     message = input(prompt)
#
#     if message == 'quit':
#         active = False  # 输入quit时结束循环
#     else:
#         print(message)
# ---------------------------------------------------------------------
# break和continue 语句
# prompt = "\nTell me something, and I will repeat it back to you."
# prompt += "\nEnter 'quit' to end this program. "
# # break语句
# while True:
#     message = input(prompt)
#
#     if message == 'quit':
#         break  # 结束整个循环
#     else:
#         print(message)
# while True:
#     message = input(prompt)
#
#     if message == 'quit':
#         continue  # 结束当前循环，并返回循环的开头
#     else:
#         print(message)
# ----------------------------------------------------------------
# 使用while循环处理list和dictionary
# (1) 在列表之间移动元素,利用pop()和append()
# unconfirmed_users = ['alice', 'brian', 'candace']
# confirmed_users = []
#
# while unconfirmed_users:  # 以list名称为判断条件，意味着当这个list为空时停止循环
#     current_user = unconfirmed_users.pop()
#
#     print(f"Verifying user: {current_user.title()}")
#     confirmed_users.append(current_user)
#
# print("\nThe following users have been confirmed:")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# (2) 删除为特定值的所有元素
# pets = ['dog', 'cat', 'dog', 'goldfish', 'rabbit']
#
# while 'dog' in pets:  # 当为特定值的所有元素全被删除时停止循环
#     pets.remove('dog')
# print(pets)

# (3) 利用输入来填充字典
responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat's your name: ")  # 用户输入作为键
    response = input("\nWhich mountain would you like to climb someday?")  # 用户输入作为键对应的值

    responses[name] = response  # 对字典进行赋值

    repeat = input("Would you like to let another person respond?(yes/no) ")
    if repeat == 'no':
        polling_active = False  # 判断是否结束循环
print("\n---Poll Results---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response}.")
