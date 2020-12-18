# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/12/08
"""
from survey import AnonymousSurvey

# 定义一个问题，并创建一个调查
question = "What language did you first learn to speak?"
my_survey = AnonymousSurvey(question)

# 显示问题并存储答案
my_survey.show_question()
print("Enter 'q' to quit at any time.")
while True:
    response = input('Language: ')
    if response == 'q':
        break
    my_survey.store_response(response)

# 显示调查结果
print("\nThank you to everyone who participated in this survey.")
my_survey.show_results()

