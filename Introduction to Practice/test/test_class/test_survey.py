# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/12/08
"""
import unittest
from survey import AnonymousSurvey

# class TestAnonymousSurvey(unittest.TestCase):
#     """用于测试AnonymousSurvey类"""
#
#     def test_store_single_response(self):
#         """测试单个答案能否被正确储存"""
#
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#
#         my_survey.store_response('English')
#         self.assertIn('English', my_survey.responses)  # my_survey.responses是一个列表，因此此处用assertIn断言
#
#     def test_store_three_response(self):
#         """测试三个答案能否被正确存储"""
#
#         question = "What language did you first learn to speak?"
#         my_survey = AnonymousSurvey(question)
#
#         responses = ['English', 'Chinese', 'Japanese']
#         for response in responses:
#             my_survey.store_response(response)
#
#         for response in responses:
#             self.assertIn(response, my_survey.responses)


class TestAnonymousSurvey(unittest.TestCase):
    """用于测试AnonymousSurvey类"""

    def setUp(self):  # 首先创建实例等对象，并将其作为self属性，可省去在每个测试方法中创建实例等对象
        """ 创建一个调查对象和一组答案，供后续的测试方法使用"""

        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Chinese', 'Japanese']

    def test_store_single_response(self):
        """测试单个答案能否被正确储存"""

        # question = "What language did you first learn to speak?"  # 利用setUp()方法后，无须再次创建实例等对象
        # my_survey = AnonymousSurvey(question)

        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_response(self):
        """测试三个答案能否被正确存储"""

        # question = "What language did you first learn to speak?"
        # my_survey = AnonymousSurvey(question)

        # responses = ['English', 'Chinese', 'Japanese']
        for response in self.responses:
            self.my_survey.store_response(response)

        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
