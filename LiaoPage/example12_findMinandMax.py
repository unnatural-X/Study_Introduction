# -*- coding: utf-8 -*-
# Find the minimum and the maximum
def minmax(n):
    if len(n) == 0:
        return None
    else:
        x1 = n[0]
        x2 = n[0]
        for x in n:
            if x < x1:
                x1 = x
            elif x > x2:
                x2 = x
        return x1, x2


# 测试
if minmax([]) is not None:
    print('测试失败!')
elif minmax([7]) != (7, 7):
    print('测试失败!')
elif minmax([7, 1]) != (1, 7):
    print('测试失败!')
elif minmax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
