# _*_ coding:utf-8 _*_
# --------------example--------------
import functools
int2 = functools.partial(int, base=2)
a = int2('1000000')
print(a)
b = int2('1000000', base=10)
print(b)
kw = {'base': 2}
c = int('1000000', **kw)
print(c)
max2 = functools.partial(max, 10)
d = max2(5, 6, 7)
print(d)
