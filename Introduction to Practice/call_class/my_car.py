# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/12/03
"""
# 调用时导入整个模块
# import car  # 导入car模块
# import electric_car  # 导入electric_car模块
# my_new_car = car.Car('audi', 'a4', '2019')
# print(my_new_car.get_descriptive_name())
#
# # 修改属性odometer_reading的值(比较推荐用方法修改)
# # my_new_car.odometer_reading = 23  # 直接修改属性的值
# # my_new_car.update_odometer(13)  # 通过方法修改属性为指定的值
# my_new_car.update_odometer(23)
# my_new_car.increment_odometer(10)  # 通过方法对属性的值进行递增
# my_new_car.read_odometer()
# my_new_car.fill_gas_tank(10)
#
# my_tesla = electric_car.ElectricCar('tesla', 'model s', '2019')
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()  # 调用有关电池的属性或方法
# my_tesla.battery.get_range()
# --------------------------------------------------------------------------------
# 调用时导入具体的类
from car import Car  # 从car模块中导入Car类
from electric_car import ElectricCar   # 从electric_car模块导入ElectricCar类

my_new_car = Car('audi', 'a4', '2019')
print(my_new_car.get_descriptive_name())

# 修改属性odometer_reading的值(比较推荐用方法修改)
# my_new_car.odometer_reading = 23  # 直接修改属性的值
# my_new_car.update_odometer(13)  # 通过方法修改属性为指定的值
my_new_car.update_odometer(23)
my_new_car.increment_odometer(10)  # 通过方法对属性的值进行递增
my_new_car.read_odometer()
my_new_car.fill_gas_tank(10)

my_tesla = ElectricCar('tesla', 'model s', '2019')
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()  # 调用有关电池的属性或方法
my_tesla.battery.get_range()
