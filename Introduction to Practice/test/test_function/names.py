# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/12/07
"""
from test_function.name_function import get_formatted_name

print("Enter 'q' to quit at any time.")

while True:
    first = input("\nPlease gives me a first name: ")
    if first == 'q':
        break

    last = input("\nPlease gives me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\nNeatly formatted name: {formatted_name}.")
