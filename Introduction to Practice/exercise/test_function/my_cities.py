# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/12/07
"""
from test_function.city_functions import get_city_country
# 调用函数
print("Enter 'q' to quit at any time.")

while True:
    city = input("\nPlease gives me your city name: ")
    if city == 'q':
        break

    country = input("\nPlease gives me your country name: ")
    if country == 'q':
        break

    population = input("\nPlease gives me the population of your city(You can also skip the step): ")

    if population:
        city_info = get_city_country(city, country, population)
    else:
        city_info = get_city_country(city, country)
    print(f"\nYour city information: {city_info}.")
