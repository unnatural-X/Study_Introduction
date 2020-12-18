# -*- coding: utf-8 -*-
# input your height and weight
s1 = input('please input your height(m):')
height = float(s1)
s2 = input('please input your weight(kg):')
weight = float(s2)
#  calculate BMI
BMI = weight/(height*height)
# output the results
print('Your BMI is: %.1f' % BMI)
if BMI < 18.5:
    print('过轻')
elif BMI < 25:
    print('正常')
elif BMI < 28:
    print('过重')
elif BMI < 32:
    print('肥胖')
else:
    print('严重肥胖')
