# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/12/07
"""
# 使用测试用例对函数进行测试
import unittest  # 导入unittest模块
from name_function import get_formatted_name  # 导入要测试的函数

class NameTestCase(unittest.TestCase):  # 创建unittest.TestCase的子类进行测试
    """测试name_function函数"""

    def test_first_last_name(self):  # 创建方法对函数行为的不同方面进行测试; 方法名必须以test_打头，所有这样的方法都将自动运行
        """能够正确地处理像Janis Joplin这样的姓名吗？"""

        formatted_name = get_formatted_name('janis', 'joplin')  # 调用被测试函数
        self.assertEqual(formatted_name, 'Janis Joplin')  # 断言方法：比较输出结果和预期结果是否一致

    def test_first_last_middle_name(self):  # 新的测试
        """能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？"""

        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')


if __name__ == '__main__':  # 作为主程序执行
    unittest.main()
