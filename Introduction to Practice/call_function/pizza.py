# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/12/02
"""
def make_pizza(size, *toppings):
    """概述要制作的披萨"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    # print(toppings)  # toppings 是元组
    for topping in toppings:
        print(f"- {topping}")