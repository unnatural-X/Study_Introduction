# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/12/03
一组用于表示电动汽车的类
"""
from car import Car  # 在一个模块中导入另一个模块

class Battery:
    """一次模拟电动汽车电频的尝试"""

    def __init__(self, battery=75):  # 可选形参
        """初始化电频的属性"""

        self.battery_size = battery
        self.battery_range = 260

    def describe_battery(self):
        """打印一条描述电频容量的信息"""

        print(f"This car has a {self.battery_size}-KWh battery.")

    def get_range(self):
        """打印一条消息，指出电频的续航里程"""
        if self.battery_size == 75:
            self.battery_range = 260
        elif self.battery_size == 100:
            self.battery_range = 315

        print(f"This car can go about {self.battery_range} miles on a full charge.")


class ElectricCar(Car):  # ElectricCar类依赖于父类，因此须在这个模块中导入Car类
    """电动汽车的独特之处"""

    def __init__(self, make, model, year):  # 方法__init__接受创建父类实例所需的信息
        """
        初始化父类的属性
        初始化电动汽车的属性
        """

        super().__init__(make, model, year)  # super()是一个特殊函数，能够调用父类的方法
        self.battery = Battery(75)  # 将新的电池类实例化用作属性

    def fill_gas_tank(self, oil_volume):  # 由于电动车没有油箱，因此可在子类中定义一个与父类同名的方法来进行代替
        """电动车没有汽车油箱"""             # 在继承时重写父类的方法，可使子类保留从父类继承而来的精华，并剔除不需要的糟粕

        print("This car doesn't need a gas tank!")
