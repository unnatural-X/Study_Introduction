# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/12/07
"""
import unittest
from test_function.city_functions import get_city_country

class CityTestCase(unittest.TestCase):
    """测试get_city_country函数"""

    def test_city_country(self):

        city_info = get_city_country('santiago', 'chile')
        self.assertEqual(city_info, 'Santiago, Chile')

    def test_city_country_population(self):

        city_info = get_city_country('santiago', 'chile', '5000000')
        self.assertEqual(city_info, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
