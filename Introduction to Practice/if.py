# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/11/28
"""
# cars = ['audi', 'bmw', 'subaru', 'toyoda']
# for car in cars:
#     if car == 'bmw':  # !=, 数字的大小比较，and, or, in, not in等关键字
#         print(car.upper())
#     else:
#         print(car.title())

# if-elif-else结构
# age = 12
# if age < 4:
#     price = 0
# elif age < 18:
#     price = 25
# elif age < 65:
#     price = 40
# elif age >= 65:  # 最后一个条件慎用else，因其保罗万象，不如elif明确
#     price = 20
# print(f"Your admission cost is ${price}.")

# 使用多个list
available_toppings = ['mushrooms', 'olives', 'green pepper', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("Finished making your Pizza!")
