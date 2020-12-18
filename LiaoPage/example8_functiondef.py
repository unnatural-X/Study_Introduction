# -*- coding: utf-8 -*-
# the solution of quadratic equation

import math  # import the math package


def quadratic(a, b, c):  # define the function
    if a==0:
        print('The coefficient of the quadratic term cannot be zero')
    elif b*b-4*a*c < 0:
        print('The equation doesn\'t have solutions')
    elif b*b-4*a*c == 0:
        x = -b/(2*a)
        return (x,)  # 单个返回值时是一个数，改为元组可用len()
    else:
        x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
        return x1, x2


# input the coefficient data
a0 = float(input('please input the coefficient of the quadratic term:'))
b0 = float(input('please input the coefficient of the first term:'))
c0 = float(input('please input the coefficient of the zero term:'))
rs = quadratic(a0, b0, c0)  # function call
if rs is None:
    pass
elif len(rs) == 1:
    print('This equation has one solution: x=%s' % rs)
else:
    print('This equation has two solutions: x1=%s x2=%s' % (rs[0], rs[1]))
