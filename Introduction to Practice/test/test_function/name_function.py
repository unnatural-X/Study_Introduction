# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/12/07
"""

# def get_formatted_name(first, last):
def get_formatted_name(first, last, middle=''):  # 对函数进行修改
    """返回一个整洁的姓名。"""

    if middle:  # 非空为真
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

