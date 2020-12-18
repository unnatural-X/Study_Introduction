# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/12/02
"""
# 创建和使用类
# class Dog:  # 关键字class, 类名首字母大写+冒号
#     """一次模拟小狗的简单尝试"""
#
#     def __init__(self, name, age):  # __init__前后双下划线(特殊方法)，创建实例时自动调用；self形参必不可少，且位于最前面
#         """初始化属性name和age"""     # self指代想要创建的实例本身
#
#         self.name = name  # 用其他形参初始化类的属性
#         self.age = age
#
#     def sit(self):  # 普通方法，无须加下划线
#         """模拟小狗收到命令时蹲下"""
#
#         print(f"{self.name} is now sitting.")
#
#     def roll_over(self):  # 普通方法，无须加下划线
#         """模拟小狗收到命令时打滚"""
#
#         print(f"{self.name} rolled over!")
#
#
# # 根据类创建实例
# my_dog = Dog('Willie', '6')  # 创建实例
# your_dog = Dog('Judy', '7')
#
# print(f"My dog's name is {my_dog.name}.")  # 访问属性
# print(f"My dog is {my_dog.age} years old.")
# my_dog.sit()  # 调用方法
# my_dog.roll_over()
#
# print(f"\nYour dog's name is {your_dog.name}.")
# print(f"Your dog is {your_dog.age} years old.")
# your_dog.sit()
# your_dog.roll_over()

# ----------------------------------------------------------------------------------
# # 给属性指定默认值，修改属性的值
# class Car:
#     """一次模拟汽车的简单尝试"""
#
#     def __init__(self, make, model, year):
#         """初始化汽车的属性"""
#
#         self.make = make
#         self.model = model
#         self. year = year
#         self.odometer_reading = 0  # 设置属性默认值，无须通过形参来定义
#         self.gas_volume = 0
#
#     def get_descriptive_name(self):
#         """返回整洁的描述性信息"""
#
#         long_name = f"{self.year} {self.make} {self.model}"
#         return long_name.title()
#
#     def read_odometer(self):
#         """打印一条带有汽车里程的信息"""
#
#         print(f"This car has {self.odometer_reading} miles on it.")
#
#     def update_odometer(self, mileage):
#         """将里程表读数设置为指定的值"""
#         if mileage >= self.odometer_reading:  # 禁止回调里程数，只能增加
#             self.odometer_reading = mileage
#         else:
#             print("You can't roll back an odometer!")
#
#     def increment_odometer(self, mileage):
#         """将里程数增加指定的量"""
#
#         if mileage >= 0:  # 如果增量为负数，提示输入错误
#             self.odometer_reading += mileage
#         else:
#             print(F"Error! The increment {mileage} is negative.")
#
#     def fill_gas_tank(self, oil_volume):  # 增加一个显示加油的方法
#         """显示汽车邮箱加了多少油"""
#
#         if oil_volume >= 0:
#             self.gas_volume += oil_volume
#             print(f"The gas tank has added {self.gas_volume}-litre oil.")
#         else:
#             print(f"Error! The {self.gas_volume} must be positive.")


# my_new_car = Car('audi', 'a4', '2019')
# print(my_new_car.get_descriptive_name())
#
# # 修改属性odometer_reading的值(比较推荐用方法修改)
# # my_new_car.odometer_reading = 23  # 直接修改属性的值
# # my_new_car.update_odometer(13)  # 通过方法修改属性为指定的值
# my_new_car.update_odometer(23)
# my_new_car.fill_gas_tank(10)
# my_new_car.increment_odometer(10)  # 通过方法对属性的值进行递增
# my_new_car.read_odometer()

# ----------------------------------------------------------------------------
# 子类的继承
# class ElectricCar(Car):  # 创建子类，父类必须包含在当前文件，且位于子类前面；必须在圆括号内指定父类的名称
#     """电动汽车的独特之处"""
#
#     def __init__(self, make, model, year):  # 方法__init__接受创建父类实例所需的信息
#         """
#         初始化父类的属性
#         初始化电动汽车的属性
#         """
#
#         super().__init__(make, model, year)  # super()是一个特殊函数，能够调用父类的方法
#         self.battery = Battery(75)  # 将新的电池类实例化用作属性
#
#     def fill_gas_tank(self, oil_volume):  # 由于电动车没有油箱，因此可在子类中定义一个与父类同名的方法来进行代替
#         """电动车没有汽车油箱"""             # 在继承时重写父类的方法，可使子类保留从父类继承而来的精华，并剔除不需要的糟粕
#
#         print("This car doesn't need a gas tank!")


# my_tesla = ElectricCar('tesla', 'model s', '2019')
# print(my_tesla.get_descriptive_name())
# my_tesla.fill_gas_tank(10)

# 当类中的属性和方法太多时，可将类中的一部分提取出来，作为一个独立的小类，然后在原来的类中将实例作为属性
# class Battery:  # 此处把ElectricCar中有关电瓶的属性和方法提取出来，定义了一个新类(注意没有继承任何类)
#
#     """一次模拟电动汽车电频的尝试"""
#
#     def __init__(self, battery=75):  # 可选形参
#         """初始化电频的属性"""
#
#         self.battery_size = battery
#         self.battery_range = 260
#
#     def describe_battery(self):
#         """打印一条描述电频容量的信息"""
#
#         print(f"This car has a {self.battery_size}-KWh battery.")
#
#     def get_range(self):
#         """打印一条消息，指出电频的续航里程"""
#         if self.battery_size == 75:
#             self.battery_range = 260
#         elif self.battery_size == 100:
#             self.battery_range = 315
#
#         print(f"This car can go about {self.battery_range} miles on a full charge.")


# my_tesla = ElectricCar('tesla', 'model s', '2019')
# print(my_tesla.get_descriptive_name())
# my_tesla.battery.describe_battery()  # 调用有关电池的属性或方法
# my_tesla.battery.get_range()
