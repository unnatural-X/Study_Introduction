# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/12/02
"""
# import pizza  # 将当前文件夹设为资源文件夹后，导入整个模块
#
# pizza.make_pizza(16, 'pepperoni')  # 用“模块名+.+函数名”来调用模块里面的函数
# pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

from pizza import make_pizza  # 导入模块里面的某个函数

make_pizza(16, 'pepperoni')  # 直接用“函数名”来调用模块里面的函数，无须用“模块名+.”
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
