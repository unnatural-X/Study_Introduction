# -*- coding: utf-8 -*-
n = 1
while n < 100:
    if n > 10:
        break  # n>11时跳出整个循环
    print(n)
    n = n+1
print('end')

k = 0
while k < 10:
    k = k+1
    if k % 2 == 0:
        continue  # 跳出本轮循环，后续的语句不执行，直接继续下一轮循环
    print(k)
print('end')
