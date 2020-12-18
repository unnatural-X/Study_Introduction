# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/12/07
"""
# 测试函数练习
def get_city_country(city, country, population=''):
    """返回一个格式为'City, Country'的字符串"""

    if population:
        city_info = f"{city.title()}, {country.title()} - population {population}"
    else:
        city_info = f"{city.title()}, {country.title()}"
    return city_info
