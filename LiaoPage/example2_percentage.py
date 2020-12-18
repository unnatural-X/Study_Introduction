# -*- coding: utf-8 -*-
s1 = float(input('please input your score in the last exam:'))
s2 = float(input('please input your score in this exam:'))
r = ((s2-s1)/s1)*100
print('The improvement percentage of your score：%.1f' % r, '%')
