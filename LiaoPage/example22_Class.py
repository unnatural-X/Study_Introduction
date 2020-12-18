# -*- coding:utf-8 -*-
"""
Author:Daniel Xu
Date:2020/08/24
"""
# --------------example------------------
# procedure-oriented
std1 = {'name': 'Michael', 'score': '98'}
std2 = {'name': 'Bob', 'score': '81'}


def print_score(std):
    print('%s: %s' % (std['name'], std['score']))


print_score(std1)
print_score(std2)


# object-oriented
class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


bart = Student('Bart Simpson', '59')
lisa = Student('Lisa Simpson', '87')
bart.print_score()
lisa.print_score()

print(bart.get_score())
print(lisa.get_score())

print(bart.get_name())
print(lisa.get_name())

bart.set_score(90)
lisa.set_score(88)
print(bart.get_score())
print(lisa.get_score())

# --------------example------------------


class Student2(object):
    def __init__(self, name, gender):
        self.__name = name
        self.__gender = gender

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender


# 测试:
bart = Student2('Bart', 'male')
if bart.get_gender() != 'male':
    print('测试失败!')
else:
    bart.set_gender('female')
    if bart.get_gender() != 'female':
        print('测试失败!')
    else:
        print('测试成功!')

# class attribute and instance attribute


class Student3(object):
    count = 0

    def __init__(self, name):
        self.__name = name
        # add a class attribute
        Student3.count += 1


# 测试:
if Student3.count != 0:
    print('测试失败!')
else:
    bart = Student3('Bart')
    if Student3.count != 1:
        print('测试失败!')
    else:
        lisa = Student3('Bart')
        if Student3.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student3.count)
            print('测试通过!')