# -*- coding: utf-8 -*-
# calculate product
# define function
def product(*n):
    if len(n) == 0:
        print('please enter one number at least') 
    else:
        mul = 1
        for x in n:
            mul = mul*x
        return mul


# input data
print('please enter the number of data,and space is used as an interval')
list1 = list(map(float, input().split()))  # input many data once
print('product %s=' % list1, product(*list1))
